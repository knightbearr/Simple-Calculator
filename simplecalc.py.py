# import TKinter
from tkinter import *

# masukan Tkinter, judul, icon, dll.
root = Tk() 
root.title("Simple Calc ^-^")
# root.iconbitmap(taruh file location) <-- jika ingin memakai icon

# atur layar tkinter
layar = Entry(root, width=40, borderwidth=10)
layar.grid(row=0, column=0, columnspan=3, pady=20)

# fungsi sistem tambah angka, hapus/clear, sama dengan/equal
def tambahAngka(angka):
    angkaPer = layar.get()
    layar.delete(0, END)
    layar.insert(0, str(angkaPer) + str(angka))

def hapus():
    layar.delete(0, END)

def samaDengan():
    angka_kedua = layar.get()
    layar.delete(0, END)

    if math == "tambah":
        layar.insert(0, angkaFirst + int(angka_kedua))

    if math == "kurang":
        layar.insert(0, angkaFirst - int(angka_kedua))

    if math == "kali":
        layar.insert(0, angkaFirst * int(angka_kedua))
   
    if math == "bagi":
        layar.insert(0, angkaFirst / int(angka_kedua))
   
# fungsi sistem tambah, kurang, kali, bagi
def tambah():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math = "tambah"

def kurang():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math = "kurang"

def kali():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math = "kali"

def bagi():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math = "bagi"


# buat button angka, atur font size atau size button sesuka kalian
button_1 = Button(root, text="1",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(1))
button_2 = Button(root, text="2",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(2))
button_3 = Button(root, text="3",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(3))
button_4 = Button(root, text="4",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(4))
button_5 = Button(root, text="5",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(5))
button_6 = Button(root, text="6",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(6))
button_7 = Button(root, text="7",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(7))
button_8 = Button(root, text="8",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(8))
button_9 = Button(root, text="9",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(9))
button_0 = Button(root, text="0",font=("Helevatica 10 bold"), padx=40, pady=20, command=lambda: tambahAngka(0))

# buat button Tambah, Bagi, Kurang, kali, Hapus, Sama Dengan
buttonTambah = Button(root, text="+", padx=40, pady=20, font=("Helevatica 10 bold"), command=tambah, fg="black", bg="orange")
buttonBagi = Button(root, text="/", padx=40, pady=20, font=("Helevatica 10 bold"), command=bagi, fg="black", bg="orange")
buttonKurang = Button(root, text="-", padx=41, pady=20, font=("Helevatica 10 bold"), command=kurang, fg="black", bg="orange")
buttonKali = Button(root, text="*", padx=41, pady=20, font=("Helevatica 10 bold"), command=kali, fg="black", bg="orange")
buttonHapus = Button(root, text="Clear", padx=74, pady=20, font=("Helevatica 10 bold"), command=hapus, fg="black", bg="grey")
buttonSamaDengan = Button(root, text="=", padx=87, pady=20, font=("Helevatica 10 bold"), command=samaDengan, fg="black", bg="grey")
    
# Kode ini untuk menaruh button di Layar dan posisikan sesuka kalian
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
buttonHapus.grid(row=4, column=1, columnspan=2)

buttonSamaDengan.grid(row=5, column=1, columnspan=2)
buttonTambah.grid(row=5, column=0)

buttonKurang.grid(row=6, column=0)
buttonKali.grid(row=6, column=1)
buttonBagi.grid(row=6, column=2)

# untuk menloop/menjalankan program tkinter ke layar
root.mainloop()


