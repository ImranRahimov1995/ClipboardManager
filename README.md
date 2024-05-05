
# Clipboard Manager Documentation [Only Windows]

## Description

This Python script serves as a clipboard manager, enabling users to store and retrieve multiple text snippets from the clipboard using keyboard shortcuts. Often, the default clipboard functionality of operating systems allows storing only one item at a time, overwriting the previous content with each new copy operation. This script enhances clipboard functionality by providing a way to store multiple items and paste them as needed using customizable keyboard shortcuts.

## Problem

The default clipboard functionality in most operating systems is limited to storing only one item at a time. This limitation can be frustrating when users need to copy multiple text snippets and paste them at different times or locations. Additionally, copying new content often overwrites the previous content in the clipboard, making it inaccessible for later use.

## Installation

To use the Clipboard Manager script, you need to install the required Python libraries. You can do this using pip, the Python package manager. Open a terminal or command prompt and run the following command:

```bash
pip install pyperclip keyboard pyautogui
```

This command will install the necessary libraries: `pyperclip` for accessing the clipboard, `keyboard` for detecting keyboard input, and `pyautogui` for simulating keyboard and mouse actions.

## Usage

1. **Run the Script**: Execute the script in a Python environment. You can do this by running the script file with the Python interpreter.

2. **Copy Text to Clipboard**: Use the keyboard shortcut `Ctrl + [number]` to copy text to the clipboard and store it with the corresponding index. For example, pressing `Ctrl + 1` will copy the current selection to the clipboard and store it with index 1.

3. **Paste Text from Clipboard**: To paste text from the clipboard storage, use the keyboard shortcut `Ctrl + Alt + [number]`. This will paste the text from the corresponding index in the clipboard storage. For example, pressing `Ctrl + Alt + 1` will paste the text stored at index 1.

4. **Repeat as Needed**: Repeat the copy and paste operations as needed to manage multiple text snippets effectively.


