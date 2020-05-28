Welcome to python custom hotkeys.
Put your custom hotkeys in hotkeys.txt
The hotkeys are formatted like: key message_to_type
Example: a cool thing to write
When you put that in hotkeys.txt, save it, and run hotkeys.py, everytime you press a, it will press enter, write "a cool thing to write" and press enter again.

If you need to find what the different keys are called, change the print_keys at the top of the code to True instead of False.

You need the python pynput and keyboard modules to run this.

(I recommend testing the hotkeys in an empty notepad to test how and if it works. Also, make sure you don't trigger the hotkey inside the hotkey)