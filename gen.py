import ctypes
import os
from pystyle import Colors, Colorate, Center
from time import sleep
from requests.exceptions import Timeout
import random as r
from datetime import datetime

#Banniere
ctypes.windll.kernel32.SetConsoleTitleW("Générateur v1.3")
os.system("cls")

banner = """

      __ ___ __  _ ___ ___  __ _____ ___ _  _ ___  
     / _] __|  \| | __| _ \/  \_   _| __| || | _ \ 
    | [/\ _|| | ' | _|| v / /\ || | | _|| \/ | v / 
     \__/___|_|\__|___|_|_\_||_||_| |___|\__/|_|_\  v1.0
                 By Eagle1337
                 
                 """

print(Center.XCenter(Colorate.Horizontal(Colors.red_to_yellow, banner, 1)))


six_fr = str(1)
sept_fr = str(2)
belgique = str(3)
allemagne = str(4)
tempsactuel = 0
file = 0

x = int(input("Combien de nombre veux-tu générer : "))

def checking_fr06():
        y = 0
        gen = [336]
        while y <= x-1:

                for i in range(1,9):
                        gen.append(r.randint(0, 9))
  
                for i in gen:
                        print(i, end="")
                        file.write(str(i))

                print("\n")
                file.write("\n")
                gen = [336]
                y+=1
        
def checking_fr07():
        y = 0
        gen = [337]
        while y <= x-1:

                for i in range(1,9):
                        gen.append(r.randint(0, 9))
  
                for i in gen:
                        print(i, end="")
                        file.write(str(i))

                file.write("\n")
                print("\n")
                gen = [337]
                y+=1

def checking_be32():
        y = 0
        gen = [32]
        while y <= x-1:

                for i in range(1,10):
                        gen.append(r.randint(0, 9))
  
                for i in gen:
                        print(i, end="")
                        file.write(str(i))

                file.write("\n")
                print("\n")
                gen = [32]
                y+=1

def checking_ge49():
        y = 0
        gen = [49]
        while y <= x-1:

                for i in range(1,12):
                        gen.append(r.randint(0, 9))
  
                for i in gen:
                        print(i, end="")
                        file.write(str(i))
                        
                file.write("\n")
                print("\n")
                gen = [49]
                y+=1

format = input("""\nFormat de numlist souhaité : 

\n[1] : 06 - FR
\n[2] : 07 - FR
\n[3] : 32 - BE
\n[4] : 49 - GE

\n>~#:""")

#Def

#Check menu du début
if format == (six_fr):

    print("\nTu as choisis le format 06-FR.\n")
    randy = str(r.randint(0, 9999999))
    file = open("result.txt","a")
    
    checking_fr06()
    file.close()
    new_name = (f"result_{randy}.txt")
    os.rename("result.txt", new_name)
    print("Fichier enregistré sous le nom :",new_name)

elif format == (sept_fr):

        randy = str(r.randint(0, 9999999))
        file = open("result.txt","a")
        print("\nTu as choisis le format 07-FR.\n")
        checking_fr07()
        file.close()
        new_name = (f"result_{randy}.txt")
        os.rename("result.txt", new_name)
        print("Fichier enregistré sous le nom :",new_name)
        
elif format == (belgique):

        randy = str(r.randint(0, 9999999))
        file = open("result.txt","a")
        print("\nTu as choisis le format 32-BE.\n")
        checking_be32()
        file.close()
        new_name = (f"result_{randy}.txt")
        os.rename("result.txt", new_name)
        print("Fichier enregistré sous le nom :",new_name)

elif format == (allemagne):

        randy = str(r.randint(0, 9999999))
        file = open("result.txt","a")
        print("\nTu as choisis le format 49-GE.\n")
        checking_ge49()
        file.close()
        new_name = (f"result_{randy}.txt")
        os.rename("result.txt", new_name)
        print("Fichier enregistré sous le nom :",new_name)

#Panel erreur
elif format == (""):
    print("\nErreur, tu n'as pas spécifié de numéro.")
else:
    print("Erreur : tu n'as pas spécifié un bon numéro")




