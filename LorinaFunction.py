
import time
import sys
from random import randint
import questionary
import climage
from colorama import Fore, Style
import shutil
from pathlib import Path

IMAGE_HEADPAT = Path(getattr(sys, "_MEIPASS", Path(__file__).parent)) / "image" / "LorinaHeadPat.png"

import LorinaDialogue as ld
import LorinaUi as ui
import LorinaLibrary as ll

#Function___________________________

def FoundCards() :
    x = randint(0, len(ll.valeurs)-1)
    cards_value = ll.valeurs[x]
    cards_power = ll.power[x]
    y = randint(0, len(ll.symbole)-1)
    cards_symbole = ll.symbole[y]
    return cards_value, cards_symbole, cards_power

def NumberOneCardLover():
    if ll.ILovePlayingCard == False :
        ui.clear_screen()
        ui.LorinaTalkingRandom(ld.Lorina_loose_5)
        ui.clean_buffer()
        cardlover = questionary.select(
            "",
            choices=["Headpat", "Continue the game"]
        ).ask()
        if cardlover == "Continue the game" :
            ll.ILovePlayingCard = True
            ui.clear_screen()
            ui.LorinaTalkingRandom(ld.Lorina_continue)
    else :
        ui.clear_screen()
        ui.LorinaTalkingRandom(ld.Lorina_continue_2)
        cardlover = questionary.select(
            "",
            choices=["Headpat", "Continue the game"]
        ).ask()
        if cardlover == "Continue the game" :
            ll.ILovePlayingCard = True
            ui.clear_screen()
            ui.LorinaTalkingRandom(ld.Lorina_persist)
    if cardlover == "Headpat" :
        ui.clear_screen()
        print(Fore.LIGHTYELLOW_EX + "⌜" + Style.RESET_ALL, end="")
        for char in ("...Alas, Grimm is a gentleman with no interest in \nsuch indecent games.                              "):
            print(Fore.LIGHTBLUE_EX + char + Style.RESET_ALL, end="", flush=True)
            time.sleep(0.05)
            if char == "\n" :
                print("", end="")
                time.sleep(0.05)
        print(Fore.LIGHTYELLOW_EX + "⌟\n" + Style.RESET_ALL)
        time.sleep(2.5)
        taille = shutil.get_terminal_size(fallback=(80, 24))
        largeur = max(35, min(120, taille.columns - 2, int((taille.lines - 4) / 0.6))) + 2
        print(climage.convert(str(IMAGE_HEADPAT), width=largeur))
        time.sleep(2)
        sys.exit()

def LorinaWin():
    if ll.PV != 0 :
        ll.PV -= 1
    if ll.PV == 2 :
        ui.clear_screen()
        ui.LorinaTalkingRandom(ld.Lorina_win)
    elif ll.PV == 1 : 
        ui.clear_screen()
        ui.LorinaTalkingRandom(ld.Lorina_win_2)
    elif ll.PV == 0 : 
        ui.clear_screen()
        ui.LorinaTalkingRandom(ld.Lorina_win_3)
        ui.clear_screen()
        ui.LorinaTalking(ld.Lorina_end_game,0)
        print("\n")
        time.sleep(2)
        sys.exit()

def GrimmWin():
    if ll.NbBacon != 0 :
        ll.NbBacon -= 1
    if ll.NbBacon == 4 : 
        ui.clear_screen()
        ui.LorinaTalkingRandom(ld.Lorina_loose_1)
    elif ll.NbBacon == 3 :
        ui.clear_screen() 
        ui.LorinaTalkingRandom(ld.Lorina_loose_2)
    elif ll.NbBacon == 2 :
        ui.clear_screen() 
        ui.LorinaTalkingRandom(ld.Lorina_loose_3)
    elif ll.NbBacon == 1 :
        ui.clear_screen() 
        ui.LorinaTalkingRandom(ld.Lorina_loose_4)
    else :
        NumberOneCardLover()
