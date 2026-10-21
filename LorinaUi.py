import time
import os
from colorama import Fore, Style
from random import randint

import LorinaLibrary as ll

def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

import sys

def clean_buffer():
    try:
        # Solution pour Windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        # Solution pour macOS et Linux
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


#Affichage________________

def LorinaTalking (dialogue,choix,OnlyOne=False) :
    if not OnlyOne :
        for i in range(len(dialogue)-choix):
            clear_screen()
            print(Fore.LIGHTRED_EX + "Lorina :" + Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + "        ⌜" + Style.RESET_ALL, end="")
            for char in dialogue[i] :
                print(Fore.LIGHTRED_EX + char + Style.RESET_ALL, end="", flush=True)
                time.sleep(0.05)
                if char == "\n" :
                    print("         ", end="")
                    time.sleep(0.05)
            print(Fore.LIGHTYELLOW_EX + "⌟\n" + Style.RESET_ALL)
    else :
        clear_screen()
        print(Fore.LIGHTRED_EX + "Lorina :" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "        ⌜" + Style.RESET_ALL, end="")
        for char in dialogue:
            print(Fore.LIGHTRED_EX + char + Style.RESET_ALL, end="", flush=True)
            time.sleep(0.05)
            if char == "\n" :
                print("         ", end="")
                time.sleep(0.05)
        print(Fore.LIGHTYELLOW_EX + "⌟\n" + Style.RESET_ALL)

def LorinaTalkingRandom (dialogue) :
    random = randint(0, len(dialogue)-1)
    Lorina_sentence = dialogue[random]
    Affichage(Lorina_sentence)

def Affichage(Lorina_sentence) :
    Lorina_status = Fore.LIGHTYELLOW_EX + "⌜" + Style.RESET_ALL + Fore.LIGHTRED_EX +"Lorina : "+ ll.bacon[ll.NbBacon] + Style.RESET_ALL + Fore.LIGHTYELLOW_EX +"⌟" + Style.RESET_ALL
    Grimm_status = Fore.LIGHTYELLOW_EX + "⌜" + Style.RESET_ALL + Fore.LIGHTGREEN_EX +"Grimm : "+ ll.life[ll.PV] + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "⌟" + Style.RESET_ALL
    print(Lorina_status)
    lorina_card= Fore.LIGHTRED_EX + "🂠" + " -> " + ll.lorina_value + ll.lorina_symbole + Style.RESET_ALL
    print(lorina_card)
    print(Fore.LIGHTYELLOW_EX + "\n                         ⌜" + Style.RESET_ALL ,Fore.LIGHTRED_EX + Lorina_sentence + Style.RESET_ALL, Fore.LIGHTYELLOW_EX + "⌟\n" + Style.RESET_ALL)
    grimm_card = Fore.LIGHTGREEN_EX + "🂠" + " -> " + ll.grimm_value + ll.grimm_symbole + Style.RESET_ALL
    print(grimm_card)
    print(Grimm_status + "\n")