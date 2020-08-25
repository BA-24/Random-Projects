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

    def calculate(string, calculate=True):
        string = list(string)
        arithmetics = ["+", "-", "*", "x", "^", "**", "/"] #supported arithmetics
        numberRequired = True
        for x in range(len(string)):
            if string[x] == " ":
                string[x] = ""
            if string[x] == "x":
                string[x] = "*"
            if string[x] == "^":
                string[x] = "**"
        string = "".join(string)
        if calculate:
            try:
                return eval(string)
            except NameError:
                return "invalid characters used: " + str(string)
            except SyntaxError:
                return "invalid syntax: " + str(string)
            except Exception as e:
                return "unknown error: " + str(e)
        else:
            return string

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
                response = pymsgbox.prompt('enter equation', "epic calculator")
                if response and numberCheck(response):
                    if "," in list(response):
                        responseList = response.split(",")
                        results = [[], []]
                        for response in responseList:
                            if numberCheck(response):
                                results[0].append(str(calculate(response)))
                                results[1].append(str(calculate(response, False)))
                        ctypes.windll.user32.MessageBoxW(0, "calculated equations:\n" + "\n".join(results[1]) + "\nresults:\n" + "\n".join(results[0]), "epic calculator", 0x0)
                    else:        
                        ctypes.windll.user32.MessageBoxW(0, "calculated equation:\n" + str(calculate(response, False)) + "\nresult:\n" + str(calculate(response)), "epic calculator", 0x0)

    def on_release(key):
        global check
        check = True

    print('application started')
    with Listener(on_press=on_press, on_release=on_release) as listener: listener.join()

elif file == None:
    while True:
        pass
