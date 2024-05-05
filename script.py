import pyperclip
import keyboard
import pyautogui

clipboard_storage = {}

def copy(i):
    pyautogui.hotkey("ctrl","c")
    clipboard_storage[i] = pyperclip.paste()
  
def paste(i):
    
    if i in clipboard_storage:
            
        pyperclip.copy(clipboard_storage[i])
        text_to_paste = clipboard_storage[i]
        keyboard.write(text_to_paste)

for i in range(1,10):
    keyboard.add_hotkey(f"ctrl+{i}", copy, args=(i,))
    keyboard.add_hotkey(f'ctrl+alt+{i}',paste, args=(i,))


keyboard.wait('ctrl+esc')

