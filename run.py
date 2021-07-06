#!/usr/bin/python3
# This code write by Mr.nope
# Version 1.3.1
import os
import time
import sys
import random
import platform

class color:
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
    orange = '\033[33m'
    blue = '\033[96m'
    darkblue = '\033[34m'


opt = color.green + "\nOption/> " + color.white
opt_color = color.green + "\nEnter: " + color.white
system = platform.uname()[0]

def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
        print("\nSorry, Please Run This Programm on Windows or Linux, MacOS\n")
        sys.exit()
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    print("\n{1}.Start Make Matrix")
    print("{2}.Exit")
    choose = input(opt)
    if choose == '1':
        make()
    elif choose == '2':
        ext()
    else:
        main()
def make():
    cls()
    print("Make Matrix :) \n")
    print("\n------------------------------------------\n")
    print("Please, Usage Matrix Color: ")
    print("\n{1}.Exit")
    print("red | green | cyan | orange | white | darkblue")
    choose = input(opt_color)
    time.sleep(0.50)
    file_name = input("\nEnter File Name: ")
    time.sleep(1)
    if choose == 'red':
        print("\nCreating...\n")
        time.sleep(2)
        f = open(file_name + ".py","w")
        f.write("""
#!/usr/bin/python3

import os
import random
import sys
import time
red = '\033[91m'
def cls():
    os.system("clear")
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    s = "0987654321"
    x = 0
    while(x<=len(s)-1):
        print(red + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s))
        time.sleep(0.1)
        if(x==len(s)-1):
            x = 0
        x += 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cls()
        sys.exit()""")
        try1()
        f.close()
    elif choose == 'green':
        print("\nCreating...\n")
        time.sleep(2)
        a = open(file_name + ".py", "w")
        a.write("""
#!/usr/bin/python3

import os
import random
import sys
import time
red = '\033[92m'
def cls():
    os.system("clear")
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    s = "0987654321"
    x = 0
    while(x<=len(s)-1):
        print(red + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s))
        time.sleep(0.1)
        if(x==len(s)-1):
              x = 0
        x += 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cls()
        sys.exit()""")
        try1()
        a.close()
    elif choose == 'cyan':
        print("\nCreating...\n")
        time.sleep(2)
        r = open(file_name + ".py","w")
        r.write("""
#!/usr/bin/python3

import os
import random
import sys
import time
blue = '\033[96m'
def cls():
    os.system("clear")
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    s = "0987654321"
    x = 0
    while(x<=len(s)-1):
        print(blue + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s))
        time.sleep(0.1)
        if(x==len(s)-1):
              x = 0
        x += 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cls()
        sys.exit()
""")
        try1()
        r.close()
    elif choose == 'orange':
        print("\nCreating...")
        time.sleep(2)
        d = open(file_name + ".py","w")
        d.write("""
#!/usr/bin/python3

import os
import random
import sys
import time
orange = '\033[33m'
def cls():
    os.system("clear")
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    s = "0987654321"
    x = 0
    while(x<=len(s)-1):
        print(orange + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s))
        time.sleep(0.1)
        if(x==len(s)-1):
              x = 0
        x += 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cls()
        sys.exit()
""")
        try1()
        d.close()
    elif choose == 'white':
        print("\nCreating...\n")
        time.sleep(2)
        z = open(file_name + ".py","w")
        z.write("""
#!/usr/bin/python3

import os
import random
import sys
import time

def cls():
    os.system("clear")
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    s = "0987654321"
    x = 0
    while(x<=len(s)-1):
        print(random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s))
        time.sleep(0.1)
        if(x==len(s)-1):
              x = 0
        x += 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cls()
        sys.exit()
""")
        try1()
        z.close()
    elif choose == 'darkblue':
        print("\nCreating...\n")
        time.sleep(2)
        g = open(file_name + ".py","w")
        g.write("""
#!/usr/bin/python3

import os
import random
import sys
import time
darkblue = '\033[34m'
def cls():
    os.system("clear")
def main():
    os.system("printf '\033]2;Matrix\a'")
    cls()
    s = "0987654321"
    x = 0
    while(x<=len(s)-1):
        print(darkblue + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + random.choice(s) + " " + random.choice(s) + " " + random.choice(s) + " " + random.choice(s))
        time.sleep(0.1)
        if(x==len(s)-1):
              x = 0
        x += 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cls()
        sys.exit()
""")
        g.close()
        try1()
    elif choose == '1':
        main()
    else:
        make()
def ext():
    cls()
    print(color.green + "Exiting..." + color.white)
    sys.exit()
def try1():
    try_to_making = input("\nDo you want to try again? [y/n] ")
    if try_to_making == 'y':
        make()
    elif try_to_making == 'n':
        try2()
    else:
        try1()
def try2():
    try_to_menu = input("\nDo you want to back Main Menu? [y/n] ")
    if try_to_menu == 'y':
        main()
    elif try_to_menu == 'n':
        try3()
    else:
        try2()
def try3():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
        ext()
    else:
        ext()
if __name__ == '__main__':
    main()