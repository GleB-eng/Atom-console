from termcolor import colored
import random
import time
from tqdm import tqdm
import os
import webbrowser
import subprocess
# ----------------------------------------------------------------------------------------------------------------------
for i in tqdm(range(100)):
    time.sleep(0.05)
print(('                                 \x1b[1;31;40m' + 'CONSOLE' + '\x1b[0m'))
print(colored("Write a \"help\""" in the console to see the entire list of commands", 'yellow'))
# ----------------------------------------------------------------------------------------------------------------------
while True:
    command = input(colored("&%& ", 'white'))
    if command == "help":  # Команда help
        print(colored("atom     calculator", 'blue'))
        print(colored("exit     fibonacci", 'blue'))
        print(colored("random   psgn", 'blue'))          # КОМАНДА HELP
        print(colored("clear    txt", 'blue'))
        print(colored("time     image", 'blue'))
        print(colored("date     get", 'blue'))
        print(colored("dnld     vid", 'blue'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == 'random':  # команда RANDOM
        try:
            number1 = float(input(colored("from  ", 'white')))
            number2 = float(input(colored("before  ", 'white')))
            print(random.randint(number1, number2))
        except ValueError:
            try:
                print(colored("please enter a NUMBER", 'red'))
                number1 = float(input(colored("from  ", 'white')))
                number2 = float(input(colored("before  ", 'white')))
                print(colored(random.randint(number1, number2, 'cyan')))
            except ValueError:
                try:
                    print(colored("this is the last warning, please enter a NUMBER", 'red'))
                    number1 = float(input(colored("from  ", 'white')))
                    number2 = float(input(colored("before  ", 'white')))
                    print(random.randint(colored(number1, number2, 'cyan')))
                except ValueError:
                    print(colored("YOU DON'T ENTER THE NUMBER!!!", 'red'))

# ----------------------------------------------------------------------------------------------------------------------
    if command == "exit":  # команда exit
        exit()
# ----------------------------------------------------------------------------------------------------------------------
    if command == "clear": # Команда clear
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("") # нужно для очищения консоли
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
# ----------------------------------------------------------------------------------------------------------------------
    if command == "time":  # Команда time
        import datetime
        now = datetime.datetime.now()
        print(colored(now.strftime("%H:%M:%S"), 'cyan'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "date": # Команда date
        import datetime
        now = datetime.datetime.now()
        print(colored("This year: %d" % now.year, 'cyan'))
        print(colored("This month: %d" % now.month, 'cyan'))
        print(colored("This day: %d" % now.day, 'cyan'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "dlnd smiles":
        for i in tqdm(range(100)):
            time.sleep(0.2)
        print(colored("Write a \"help\""" in the console to see the entire list of commands", 'yellow'))
        from smiles import classic
        from smiles import not_know1, cool_guy, dead_sm, classic_mustache, \
            wtf_smile, weapon, not_know2, panda, classic_with_money, \
            fighter, pretty, crying, kissing, fin_and_jake, spider, fear

        while True:
            command_n_smile = input(colored("=)  ", 'green'))
            if command_n_smile == "classic":
                print(colored(classic, 'red'))
            if command_n_smile == "not know1":
                print(not_know1)
            if command_n_smile == "cool guy":
                print(cool_guy)
            if command_n_smile == "dead":
                print(dead_sm)
            if command_n_smile == "classic mustache":
                print(classic_mustache)
            if command_n_smile == "wtf":
                print(wtf_smile)
            if command_n_smile == "weapon":
                print(weapon)
            if command_n_smile == "not know2":
                print(not_know2)                                   # КОНСОЛЬ SMILES
            if command_n_smile == "panda":
                print(panda)
            if command_n_smile == "fighter":
                print(fighter)
            if command_n_smile == "pretty":
                print(pretty)
            if command_n_smile == "classic with money":
                print(classic_with_money)
            if command_n_smile == "crying":
                print(crying)
            if command_n_smile == "kissing":
                print(kissing)
            if command_n_smile == "fin and jake":
                print(fin_and_jake)
            if command_n_smile == "spider":
                print(spider)
            if command_n_smile == "fear":
                print(fear)
            if command_n_smile == "help":
                print(colored("COMMANDS:   not know1, cool guy, dead, classic mustache, ", 'blue'))
                print(colored("wtf, weapon, not know2, panda, classic with money, ", 'blue'))
                print(colored("fighter, pretty, crying, kissing, fin and jake, spider, fear, help, exit", 'blue'))
            if command_n_smile == "exit":
                break
# ----------------------------------------------------------------------------------------------------------------------
    if command == "dlnd":
        print(colored("please enter the name of the file you want to run: here are the working files", 'red'))
        print(colored("smiles", 'red'))
        print(colored("write dlnd and file name", 'red'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "calculator":              # КАЛЬКУЛЯТОР НА 2 ЧИСЛА
        for i in tqdm(range(5)):
            time.sleep(0.2)
        print(colored("                             Calculator", 'yellow'))
        print(colored("you can exit the calculator by writing exit in the select line", 'red'))
        while True:
            try:
                first_number = float(input(colored("first number   +=-  ", 'white')))
                second_number = float(input(colored("second number +=-  ", 'white')))
                do = input(colored("select / + * -   ", 'white'))
                if do == "/":
                    print(colored(first_number / second_number, 'yellow'))
                if do == "+":
                    print(colored(first_number + second_number, 'yellow'))
                if do == "*":
                    print(colored(first_number + second_number, 'yellow'))
                if do == "-":
                    print(colored(first_number - second_number, 'yellow'))
                if do == "exit":
                    break
            except ValueError:
                print(colored("please enter a NUMBER", 'red'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "fibonacci":      # ЧИСЛА ФИБОНАЧЧИ
        def fibonacci(max):
            a, b = 0, 1
            while a < max:
                yield a
                a, b = b, a + b
        for n in fibonacci(100):
            print(colored(n, 'cyan'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "psgn":                    # PASSWORD GENERATOR
        print(colored("PASSWORD GENERATOR", 'yellow'))
        print(colored("you can exit the calculator by writing exit in the input line", 'red'))
        print(colored("press enter to next password", 'red'))
        while True:
            from psw_gen import passw_generator
            print(colored( passw_generator(), 'cyan'))
            a = input()
            if a == "exit":
                break
# ----------------------------------------------------------------------------------------------------------------------
    if command == "txt":
        print(colored("you can exit the txt by writing exit in the input line", 'red'))
        print()
        print(colored("if you need to open a file from another directory just write the full path to it", 'red'))
        while True:
            try:
                file = input("/\\\/  ")
                if file == "exit":
                    break                                 # КОМАНДА TXT
                txt = open(file, 'r')
                file_contents = txt.read()
                print(file_contents)
            except FileNotFoundError:
                print(colored("FILE NOT FOUND!!!", 'red'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "image":
        print(colored("you can exit the txt by writing exit in the input line", 'red'))
        print(colored("if you need to open a file from another directory just write the full path to it", 'red'))
        while True:
            try:
                image = input(colored("::>  ", 'white'))                      # КОМАНДА IMAGE
                if image == "exit":
                    break
                webbrowser.open(image, 'r')
            except FileNotFoundError:
                print(colored("file NOT found!!!", 'red'))
            except UnicodeDecodeError:
                print(colored("IT'S NO TXT FILE", 'red'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "get":
        print(colored("you can exit the txt by writing exit in the input line", 'red'))
        print()
        print(colored("if you need to open a file from another directory just write the full path to it", 'red'))
        while True:
            try:
                code = input(colored("##  ", 'white'))
                if code == "exit":
                    break                               # КОМАНДА GET
                prgcode = open(code, 'r')
                code_file_contents = prgcode.read()
                print(code_file_contents)
            except FileNotFoundError:
                print(colored("FILE NOT FOUND!!!", 'red'))
            except UnicodeDecodeError:
                print(colored("IT'S NO CODE FILE", 'red'))
# ----------------------------------------------------------------------------------------------------------------------
    if command == "vid":
        subprocess.call("", shell=True)