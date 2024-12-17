# Window for app

from tkinter import *
# import other necessery modules
import random
import time
import datetime

# creating root object
root = Tk()

# defining size of window
root.geometry("1280x6000")

# setting up the title of window
root.title("HIDDEN WRITING")

Tops = Frame(root, width=1600, relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700,
           relief=RAISED)
f1.pack(side=LEFT)
# --------------------------------------------------------------------------------
# TIME and Date

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="CRYPTOGRAPHY \n Vigenère cipher",
                bg="Black", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Red",
                bd=10, anchor='w')

lblInfo.grid(row=1, column=0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
# ---------------------------------------------------------------------------------
# Labels

lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=0, column=0)

txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="light blue", justify='left')

txtMsg.grid(row=0, column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="KEY", bd=16, anchor="w")

lblkey.grid(row=1, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="light blue", justify='left')

txtkey.grid(row=1, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=2, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="light blue", justify='left')

txtmode.grid(row=2, column=1)

lblService = Label(f1, font=('arial', 16, 'bold'),
                   text="The Result-", bd=16, anchor="w")

lblService.grid(row=1, column=2)

txtService = Entry(f1, font=('arial', 16, 'bold'),
                   textvariable=Result, bd=10, insertwidth=4,
                   fg="white", bg="black", justify='left')

txtService.grid(row=1, column=3)

import sys


def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return sys.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = sys.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


sys.exit()


def qExit():
    root.destroy()


def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))


btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('Algerian', 18, 'bold'), width=8,
                  text="CONVERT", bg="white",
                  command=Ref).grid(row=15, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('Algerian', 18, 'bold'),
                  width=8, text="Reset", bg="green",
                  command=Reset).grid(row=15, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('Algerian', 18, 'bold'),
                 width=8, text="Close", bg="red",
                 command=qExit).grid(row=15, column=3)
root.mainloop()