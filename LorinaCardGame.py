#Import____________________
import sys, time
import questionary
from colorama import Fore, Style

import LorinaLibrary as ll 
import LorinaDialogue as ld
import LorinaUi as ui
import LorinaFunction as lf

#Start Game_________________
def start_game():
    ui.clear_screen()

    ui.LorinaTalking(ld.Lorina_start_game,3)

    ui.clean_buffer()
    choice = questionary.select(
        "",
        choices=["Play Cards", "Don't Play"]
    ).ask()

    if choice == "Play Cards":
        ui.LorinaTalking(ld.Lorina_start_game[2],0,True)
    elif choice == "Don't Play": 
        ui.LorinaTalking(ld.Lorina_start_game[1],0,True)
        time.sleep(2)
        sys.exit()
    else :
        ui.LorinaTalking(ld.Lorina_start_game[3],0,True)
        time.sleep(2)
        sys.exit()


#Main Game__________________
def main():
    ui.LorinaTalking(ld.Lorina_explain,0)
    ui.clear_screen()

    while ll.END != True :
        ui.clear_screen()
        Lorina_status = Fore.LIGHTYELLOW_EX + "⌜" + Style.RESET_ALL + Fore.LIGHTRED_EX +"Lorina : "+ ll.bacon[ll.NbBacon] + Style.RESET_ALL + Fore.LIGHTYELLOW_EX +"⌟" + Style.RESET_ALL
        print(Lorina_status)
        if not ll.cheater:
            ll.lorina_value, ll.lorina_symbole, ll.lorina_power = lf.FoundCards()
        lorina_card= Fore.LIGHTRED_EX + "🂠" + " -> " + ll.lorina_value + ll.lorina_symbole + Style.RESET_ALL 
        print(lorina_card)
        print(Fore.LIGHTYELLOW_EX + "\n                         ⌜" + Style.RESET_ALL ,Fore.LIGHTRED_EX + ld.Lorina_high_low[0] + Style.RESET_ALL, Fore.LIGHTYELLOW_EX + "⌟\n" + Style.RESET_ALL)
        if not ll.cheater:
            ll.grimm_value, ll.grimm_symbole, ll.grimm_power = lf.FoundCards()
        grimm_card = Fore.LIGHTGREEN_EX + "🂠" + " -> " + "?" + Style.RESET_ALL
        print(grimm_card)
        Grimm_status = Fore.LIGHTYELLOW_EX + "⌜" + Style.RESET_ALL + Fore.LIGHTGREEN_EX + "Grimm : "+ ll.life[ll.PV] + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "⌟" + Style.RESET_ALL
        print(Grimm_status + "\n")
        ll.cheater = False

        ui.clean_buffer()
        highlow = questionary.select(
            "",
            choices=["High", "Low"]
        ).ask()
        
        if highlow == "High" :
            ui.clear_screen()
            ui.Affichage("Let's see the result! ♪")
            if ll.lorina_power < ll.grimm_power :
                lf.GrimmWin()

            elif ll.lorina_power > ll.grimm_power :
                lf.LorinaWin()

            elif ll.lorina_power == ll.grimm_power :
                ui.clear_screen()
                ui.LorinaTalkingRandom(ld.Lorina_draw)

        elif highlow == "Low" :
            ui.clear_screen()
            ui.Affichage("Let's see the result! ♪")
            if ll.lorina_power < ll.grimm_power :
                lf.LorinaWin()

            elif ll.lorina_power > ll.grimm_power :
                lf.GrimmWin()

            elif ll.lorina_power == ll.grimm_power :
                ui.clear_screen()
                ui.LorinaTalkingRandom(ld.Lorina_draw)

        else :
            ui.clear_screen()
            ll.cheater = True
            print(Lorina_status)
            print(lorina_card)
            print(Fore.LIGHTYELLOW_EX + "\n                         ⌜" + Style.RESET_ALL ,Fore.LIGHTRED_EX + "Hey! Stop trying to cheat!" + Style.RESET_ALL, Fore.LIGHTYELLOW_EX + "⌟\n" + Style.RESET_ALL)
            print(grimm_card)
            print(Grimm_status + "\n")

if __name__ == "__main__":
    start_game()
    main()