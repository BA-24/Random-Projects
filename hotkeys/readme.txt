Welcome to python custom hotkeys.
Create a text file in the profiles folder with the name of your choice and enter your hotkeys in that text file.
The hotkeys are formatted like: key message_to_type
Example: a cool thing to write
When you put that in a text file in hotkeys.txt, save it, run hotkeys.py and select your profile, everytime you press a, it will press enter, write "a cool thing to write" and press enter again.

If you need to find what the different keys are called, change the print_keys at the top of the code to True instead of False.

numpad keys are entered like "numpad[number]", example: "numpad1 you pressed numpad 1".
Using numpad keys are slower that regular keys due to the code having to differentiate between a numpad number and a regular number.

You need the python pynput and keyboard modules to run this.

(I recommend testing the hotkeys in an empty notepad to test how and if it works. Also, make sure you don't trigger the hotkey inside the hotkey)
