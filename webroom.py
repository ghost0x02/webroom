                                                                                                                                                                                                                                                                                                              ex.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ex.py                                                                                                                                                                                                                                                                                                                 
import socket 
import os
import time 
 
cyan = '\033[0;36m'
lightcyan = '\033[96m'
green = '\033[0;32m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'
blue = '\033[1;34m'

def main_menu():
    while True:
        os.system("clear")
        print(f"{red}\033]0;Webroom(GHOST0x02)\007")
        print(f"""{yellow}
           _________________________________________________________________________

█████   ███   █████ ██████████ ███████████     ███████████      ███████       ███████    ██████   ██████
░░███   ░███  ░░███ ░░███░░░░░█░░███░░░░░███   ░░███░░░░░███   ███░░░░░███   ███░░░░░███ ░░██████ ██████ 
 ░███   ░███   ░███  ░███  █ ░  ░███    ░███    ░███    ░███  ███     ░░███ ███     ░░███ ░███░█████░███ 
 ░███   ░███   ░███  ░██████    ░██████████     ░██████████  ░███      ░███░███      ░███ ░███░░███ ░███ 
 ░░███  █████  ███   ░███░░█    ░███░░░░░███    ░███░░░░░███ ░███      ░███░███      ░███ ░███ ░░░  ░███ 
  ░░░█████░█████░    ░███ ░   █ ░███    ░███    ░███    ░███ ░░███     ███ ░░███     ███  ░███      ░███ 
    ░░███ ░░███      ██████████ ███████████     █████   █████ ░░░███████░   ░░░███████░   █████     █████
     ░░░   ░░░      ░░░░░░░░░░ ░░░░░░░░░░░     ░░░░░   ░░░░░    ░░░░░░░       ░░░░░░░    ░░░░░     ░░░░░ 1.0-version 
                                                                                                         
             ______________________________________________________________________
                                CODED BY ENESXSEC-GHOST0x02
                                           LUKA
             ----------------------------------------------------------------------
""")
        print(f"""{red}
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                  DİKKAT:SİTE GİRDİKTEN SONRA 
                  CÜMLE SONUNA BOŞLUK BIRAKMA FİX YER 
               
                     İNSTAGRAM--:enesxsecit
                     İNSTAGRAM--:luka_developer

            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
              1.SPLOİT                    
              2.ANTİTOOL         
              3.HTTP-HEADER                   
              4.DİMİTRY KULLAN              
              5.NMSCRİPT 
            ====================================================================
""")
        option = input("root@Webroom:~ ")
        if option == "exit":
            break
        elif option == "1":
            os.system("clear")
            os.system("git clone https://github.com/ghost0x02/sploit")
            os.chdir("sploit")
            os.system("python3 sploit.py")



        elif option == "2":
            os.system("clear")
            os.system("git clone https://github.com/ghost0x02/antitool")
            os.chdir("antitool")
            os.system("python3 antitool.py")


        elif option == "3":
            os.system("clear")
            os.system("git clone https://github.com/hawk-unity/http-header")
            os.chdir('http-header')
            os.system("python3 headers.py")


        
        elif option == "4":
           os.system("clear")
           os.system("figlet dimitry")
           print("coded by enesxsec")           
           site = input("Hedef site gir: ")
           os.system(f"dmitry -w {site}")
           os.system(f"dmitry -i {site}")
           os.system(f"dmitry -n {site}")
           os.system(f"dmitry -s {site}")
           os.system(f"dmitry -e {site}")
           os.system(f"dmitry -p {site}")


        elif option == "5":
           os.system("clear")
           os.system("git clone https://github.com/lukacoder/nmappython")
           os.chdir('nmappython')
           os.system("python3 NMscript.py")          
main_menu()

