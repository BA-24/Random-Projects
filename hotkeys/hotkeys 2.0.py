print('starting application...')

from pynput.keyboard import Key, Listener
import keyboard
import time
import os
from os import path
check = True

#checks for profile folder
if path.exists('./profiles'):
    print('profile folder found. select profile:')
    profiles = os.listdir('./profiles')
    for x in range(len(profiles)):
        print(str(x+1) + '. ' + profiles[x])
    loop = True
    while loop:
        try:
            profile = profiles[(int(input())) - 1]
            loop = False
        except ValueError:
            print('Please enter a number')

    file = './profiles/' + profile

else:
    try:
        f = open('hotkeys.txt')
        f.close()
        print('hotkeys.txt found.')
        file = 'hotkeys.txt'
    except:
        print('no hotkey files found.')
        file = None
        
    
        

if file != None:

    #gets detection keys
    f = open(file, 'r')
    keys = []
    for r in f:    
        if r != '\n':
            keys = keys + [r.split()[0]]
    f.close()

    #gets messages
    f = open(file, 'r')
    msg = []
    for r in f:    
        if r != '\n':
            msg = msg + [r.replace( ((r.split()[0]) + ' '), '', 1).replace('\n', '', 1)]
    f.close()

    def write(message, latency=0.1):
        keyboard.press_and_release('enter')
        time.sleep(latency)
        keyboard.write(message)
        keyboard.press_and_release('enter')

    def on_press(key):
        global check
        if check == True:
            a = 0
            for x in keys:
                if x == str(key):
                    write(msg[a])
                a = a + 1

    def on_release(key):
        global check
        check = True

    print('application started')
    with Listener(on_press=on_press, on_release=on_release) as listener: listener.join()

elif file == None:
    while True:
        pass
