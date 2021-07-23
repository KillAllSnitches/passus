import os, ctypes
from colorama import init, Style, Fore


init(convert=True)

orange = Fore.YELLOW
red = Fore.RESET
run = os.system
reset = Style.RESET_ALL

def logo():
    run('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("PASSUS | WiFi Password Recovery Tool")
    print("""
    
    """)
    print(orange, """        ███████████    █████████    █████████   █████████  █████  █████  █████████ 
        ░░███░░░░░███  ███░░░░░███  ███░░░░░███ ███░░░░░███░░███  ░░███  ███░░░░░███
         ░███    ░███ ░███    ░███ ░███    ░░░ ░███    ░░░  ░███   ░███ ░███    ░░░ 
         ░██████████  ░███████████ ░░█████████ ░░█████████  ░███   ░███ ░░█████████ 
         ░███░░░░░░   ░███░░░░░███  ░░░░░░░░███ ░░░░░░░░███ ░███   ░███  ░░░░░░░░███
         ░███         ░███    ░███  ███    ░███ ███    ░███ ░███   ░███  ███    ░███
         █████        █████   █████░░█████████ ░░█████████  ░░████████  ░░█████████ 
        ░░░░░        ░░░░░   ░░░░░  ░░░░░░░░░   ░░░░░░░░░    ░░░░░░░░    ░░░░░░░░░  
                                    
                                    github.com/vx-dev/passus

                                                                            """ + reset)


def menu():
    logo()
    print("""

    [""" + orange + """1""" + reset +"""] Show Saved Networks
    [""" + orange + """2""" + reset +"""] Grab Network Password
    [""" + orange + """3""" + reset +"""] Exit
    
    """)
    
    mode = input('Mode: ')
    
    if mode == '1':
        show()
    
    elif mode == '2':
        grabpass()
    
    elif mode == '3':
        exit


def show():
    logo()
    run('netsh wlan show profiles')
    close()


def grabpass():
    logo()
    
    ssid = input('Network Name: ')
    
    try:
        
        run('netsh wlan show profile name="' + ssid + '" key=clear | find /I "Key Content"')
        close()
    
    except:
        
        print('Please Make Sure You Entered the Network Name Correctly...')
        close()


def close():
    c = input('Press Any Key To Continue')
    
    if c == '1':
        menu()
    
    else:
        menu()
menu()