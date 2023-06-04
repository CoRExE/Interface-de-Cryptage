from tkinter import *
from random import *

# generation et paramétrage de la fenêtre
window = Tk()
window.title("Cryptage")
window.geometry("480x300")
window.minsize(480, 300)
window.iconbitmap(r"cadenaIcon.ico")
window.config(bg='grey')

# for vigenere
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


# program
def helping():
    print('This program is for Encrypting your messages\nOnly Crypt !')
    print('The first button is Caesar Crypt, take your word(s) and decade with a integer key')
    print('')
    print('The Second button is a Vigenere Crypt\nIt takes your word(s) and a string key')
    print('')
    print('For Bin and Hex, no key required')
    print('')
    print('Clear is to Remove all things present on Entry Areas')
    print('')
    print('Have a great time !')
    clean()
    input_area.insert(0, "Look on")
    output_area.insert(0, "the Shell")


def clean():
    input_area.delete(0, END)
    key_area.delete(0, END)
    output_area.delete(0, END)


def caesar_crypt():
    """
    Put a word(s) on Input area and a numbers\n(Min<->Max : -25<->25)
    \nAnd click the first button\n
    The program Take you two information and convert your word(s) with 'ORD()'
    """
    msg_ori = input_area.get()
    msg_ori.lower()
    if input_area.get() == '':
        input_area.insert(0, "Saisissez un mot ou une phrase")
        return
    if key_area.get() == '' or int(key_area.get()) == 0:
        key_area.insert(0, "Entrez une valeur numérique")
        output_area.insert(0, "différente de 0")
        return
    else:
        decade = int(key_area.get())
    cacheTempo = []
    for ag in range(len(msg_ori)):
        if msg_ori[ag] == " ":
            ag = +1
        else:
            cacheTempo.append(ord(msg_ori[ag]))
    for eg in range(len(cacheTempo)):
        if cacheTempo[eg] + decade > 122:
            cacheTempo[eg] = chr((cacheTempo[eg] + decade) - 26)
        elif cacheTempo[eg] + decade < 97:
            cacheTempo[eg] = chr((cacheTempo[eg] + decade) + 26)
        else:
            cacheTempo[eg] = chr(cacheTempo[eg] + decade)
    clean()
    output_area.insert(0, cacheTempo)


def helping_caesar():
    clean()
    input_area.insert(0, "Test")
    key_area.insert(0, 3)
    help(caesar_crypt)


def vigenere_crypt():
    """
    Vigenere is more complicate, He take your word(s) and your Word(key)\n
    Only word don't put SPACE in
    He convert two this two object in integer with list reference\n
    And add one by one the identity numbers\n
    Finaly, he reconvert in string
    """
    if input_area.get() == '':
        input_area.insert(0, "Saisissez un mot ou une phrase")
        return
    if key_area.get() == '':
        key_area.insert(0, "Entrez un mot ou une phrase")
        return
    msg_ori = input_area.get()
    msg_ori.lower()
    key = key_area.get()
    key.lower()
    cacheTempo = []
    for ig in range(len(msg_ori)):
        if msg_ori[ig] == " ":
            ig = +1
        else:
            cacheTempo.append(msg_ori[ig])
    keylist = []
    item = 0
    for og in range(len(cacheTempo) + 1):
        if item >= len(key):
            item = 0
        else:
            keylist.append(key[item])
            item += 1
    for yg in range(len(alphabet)):
        for ah in range(len(cacheTempo)):
            if cacheTempo[ah] == alphabet[yg]:
                cacheTempo[ah] = yg
            if keylist[ah] == alphabet[yg]:
                keylist[ah] = yg
    finish = []
    for eh in range(len(cacheTempo)):
        if cacheTempo[eh] + keylist[eh] >= 26:
            finish.append(cacheTempo[eh] + keylist[eh] - 26)
        else:
            finish.append(cacheTempo[eh] + keylist[eh])
    for ih in range(len(finish)):
        finish[ih] = alphabet[finish[ih]]
    clean()
    output_area.insert(0, finish)


def helping_vigenere():
    clean()
    input_area.insert(0, "Test")
    key_area.insert(0, "Hey")
    help(vigenere_crypt)


def binary_crypt():
    """
    This crypt no required key\n
    Binary take your word(s), convert in integer and binary after with 'BIN()'
    """
    cache_tempo = input_area.get()
    cache_tempo.lower()
    pil = []
    finish = []
    item = []
    for aj in range(len(cache_tempo)):
        for ej in range(len(alphabet)):
            if cache_tempo[aj] == alphabet[ej]:
                pil.append(ej)
    print(pil)
    for ij in range(len(pil)):
        temp = bin(pil[ij])
        print(temp)
        for oj in range(len(temp)):
            if oj <= 1:
                oj += 1
            else:
                item.append(temp[oj])
        finish.append(item)
        item = []
    clean()
    output_area.insert(0, finish)


def helping_bin():
    clean()
    input_area.insert(0, "Just a message")
    help(binary_crypt)


def hexa_crypt():
    """
    This crypt no required key\n
    Hexa take your word(s), convert in integer and Hexadecimal with 'HEX()'
    """
    cache = input_area.get()
    cache.lower()
    fin = []
    bib = []
    for uj in range(len(cache)):
        for yj in range(len(alphabet)):
            if cache[uj] == alphabet[yj]:
                bib.append(yj)
    print(bib)
    for ak in bib:
        temp = hex(ak)
        print(temp)
        for ek in range(len(temp)):
            if ek <= 1:
                ek += 1
            else:
                fin.append(temp[ek])
    clean()
    output_area.insert(0, fin)


def helping_hex():
    clean()
    input_area.insert(0, "A simple message")
    help(hexa_crypt)


# central_frame
frame = Frame(window, bg='grey')

# frame_de_droite
right_frame = Frame(frame, bg='grey')

# frame_de_gauche
left_frame = Frame(frame, bg='grey')

# titre de texte à crypter
title_input = Label(left_frame, text="Input :", bg='grey', fg='blue')
title_input.pack()

# Titre_de_l'entrer
input_area = Entry(left_frame, font=("Arial", 15), bg='grey', fg='black', bd=2)
input_area.pack()

# titre de la clé
title_key = Label(left_frame, text="Key :", bg='grey', fg='red')
title_key.pack()

# zone de la clé
key_area = Entry(left_frame, font=("Arial", 15), bg='grey', fg='red', bd=2)
key_area.pack()

# associer image caesar
caesar_image = PhotoImage(file=r"caesar.png")

# associer image vigenere
vigenere_image = PhotoImage(file=r"vigenere.png")

# bouton_caesar
caesar = Button(right_frame, image=caesar_image, command=caesar_crypt)
caesar.pack()

# bouton_vigenere
vigenere = Button(right_frame, image=vigenere_image, command=vigenere_crypt)
vigenere.pack(padx=1, pady=1)

# bouton_binaire
binary = Button(right_frame, text="BIN", command=binary_crypt)
binary.pack()

# bouton_hexa
hexa = Button(right_frame, text="HEX", command=hexa_crypt)
hexa.pack()

# bouton clear
clear = Button(right_frame, text="Clear", command=clean)
clear.pack()

# titre de l'output
title_output = Label(left_frame, text="Output:", bg='grey', fg='green')
title_output.pack()

# zone de résultat de cryptage
output_area = Entry(left_frame, font=("Arial", 15), bg='grey', fg='blue', bd=2)
output_area.pack()

# Menu de base
menu_bar = Menu(window)
# App section
app_menu = Menu(menu_bar, tearoff=0)
app_menu.add_command(label="Clear Area", command=clean)
app_menu.add_command(label="Exit", command=window.destroy)
menu_bar.add_cascade(label="App", menu=app_menu)

# Help section
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Do you need help ?", command=helping)
help_menu.add_command(label="caesar", command=helping_caesar)
help_menu.add_command(label="Vigenere", command=helping_vigenere)
help_menu.add_command(label="Binary", command=helping_bin)
help_menu.add_command(label="Hexa", command=helping_hex)
menu_bar.add_cascade(label="Help", menu=help_menu)

# add menu
window.config(menu=menu_bar)

# insertion des sous frames
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)

# insertion de la fenêtre parente
frame.pack(expand=YES)

window.mainloop()
