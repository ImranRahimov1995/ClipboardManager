import subprocess
import keyboard
import platform
import time


class Clipboard:
    def copy_to_clipboard(self, text):
        raise NotImplementedError

    def paste_from_clipboard(self):
        raise NotImplementedError


class WindowsClipboard(Clipboard):
    def copy_to_clipboard(self, text):
        process = subprocess.Popen(
            ['powershell.exe', '-command', f'Set-Clipboard -Value "{text}"']
        )
        process.communicate()

    def paste_from_clipboard(self):
        process = subprocess.Popen(
            ['powershell.exe', '-command', 'Get-Clipboard'],
            stdout=subprocess.PIPE
        )
        output, _ = process.communicate()
        return output.decode('utf-8').strip()


class ClipboardManager:
    def __init__(self):
        self.clipboard_storage = {}
        self.system_clipboard = self._get_system_clipboard()
        self.setup_hotkeys()

    def _get_system_clipboard(self):
        system = platform.system()
        clipboards = {
            'Windows': WindowsClipboard()
        }
        return clipboards.get(system)

    def copy(self, slot):
        try:
            self._simulate_keypress("ctrl+c")
            time.sleep(0.1)
            self.clipboard_storage[slot] = (
                self.system_clipboard.paste_from_clipboard()
            )
            print(f"Copied to slot {slot}")
        except Exception as e:
            print(f"Error copying to slot {slot}: {e}")

    def paste(self, slot):
        if slot in self.clipboard_storage:
            try:
                text = self.clipboard_storage[slot]
                self.system_clipboard.copy_to_clipboard(text)
                self._simulate_keypress("ctrl+v")
                print(f"Pasted from slot {slot}")
            except Exception as e:
                print(f"Error pasting from slot {slot}: {e}")

    def _simulate_keypress(self, keys):
        keyboard.send(keys)

    def setup_hotkeys(self):
        for i in range(1, 10):
            keyboard.add_hotkey(f"ctrl+{i}", self.copy, args=(i,))
            keyboard.add_hotkey(f'ctrl+alt+{i}', self.paste, args=(i,))
        print("Clipboard manager running. Press [Ctrl+Esc] to exit.")

    def run(self):
        try:
            while True:
                keyboard.wait('ctrl+esc')
                break
        except Exception as e:
            print(f"Error in main loop: {e}")


if __name__ == "__main__":
    manager = ClipboardManager()
    manager.run()
