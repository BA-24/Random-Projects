print('starting application...')

from pynput.keyboard import Key, Listener
import keyboard
import time
import os
import pymsgbox
import ctypes
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

    file = './profiles\\' + profile

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
            keys = keys + [r.lower().split()[0]]
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

    def calculate(string):
        string = list(string)
        arithmetics = ["+", "-", "*", "x", "^", "**", "/"] #supported arithmetics
        numberRequired = True
        for x in range(len(string)):
            if string[x] in arithmetics:
                if not numberRequired:
                    if string[x] == "x":
                        string[x] = "*"
                        numberRequired = True
                    elif string[x] == "*" and len(string) >= x+3 and string[x+1] == "*" and string[x+2] == "*" and (string[x] + string[x+1]) != "**":
                        pass
                    elif string[x] == "^":
                        string[x] = "**"
                        numberRequired = True
                    else:
                        numberRequired = True
                elif numberRequired:
                    string[x] = ""
            elif string[x].isdigit():
                numberRequired = False
            else:
                string[x] = ""
        string = "".join(string)
        if string[-1:] in arithmetics:
            if string[-2:] == "**":
                string = string[:-2]
            else:
                string = string[:len(string)-1]
        return eval(string)

    def numberCheck(string):
        for x in list(string):
            if x.isdigit(): return True
        return False

    def on_press(key):
        global check
        if check == True:
            a = 0
            key = str(key).lower()
            for x in keys:
                if x == key:
                    write(msg[a])
                a = a + 1
            if str(key).lower() == "key.delete":
                response = pymsgbox.prompt('enter equation')
                if response and numberCheck(response):
                    if "," in list(response):
                        responseList = response.split(",")
                        results = []
                        for response in responseList:
                            if numberCheck(response): results.append(str(calculate(response)))
                        ctypes.windll.user32.MessageBoxW(0, "results:\n" + "\n".join(results), "epic calculator", 0x0)
                    else:        
                        ctypes.windll.user32.MessageBoxW(0, "result: " + str(calculate(response)), "epic calculator", 0x0)

    def on_release(key):
        global check
        check = True

    print('application started')
    with Listener(on_press=on_press, on_release=on_release) as listener: listener.join()

elif file == None:
    while True:
        pass
