from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_message = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="Arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Arial 10", bg="White", relief=GROOVE, wrap=WORD, bd=0)
        text2.insert(END, decrypt_message)
        text2.place(x=10, y=40, width=380, height=150)
    elif password == "":
        messagebox.showerror("Decryption", "Please input the password")
    else:
        messagebox.showerror("Decryption", "Invalid password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Arial 10", bg="White", relief=GROOVE, wrap=WORD, bd=0)
        text2.insert(END, encrypt_message)
        text2.place(x=10, y=40, width=380, height=150)
    elif password == "":
        messagebox.showerror("Encryption", "Please input the password")
    else:
        messagebox.showerror("Encryption", "Invalid password")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("375x430")

    image_icon = PhotoImage(file="C:/Users/Dell/Desktop/key.png")
    screen.iconphoto(False, image_icon)

    screen.title("ENDECRYPT")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("Arial", 13)).place(x=10, y=10)
    global text1
    text1 = Text(font="Arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    global code
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=('arial', 25), show='0').place(x=10, y=200)
    Button(text='ENCRYPT', height=2, width=23, bg='#ed3833', fg='white', bd=0, command=encrypt).place(x=10, y=340)
    Button(text='DECRYPT', height=2, width=23, bg='#00bd56', fg='white', bd=0, command=decrypt).place(x=199, y=340)
    Button(text='RESET', height=2, width=50, bg='#1089ff', fg='white', bd=0, command=reset).place(x=10, y=380)

    screen.mainloop()

main_screen()
