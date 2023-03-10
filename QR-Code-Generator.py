import qrcode
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title('QR code with Python')

def send():
    data = txt_line.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('imag.png')
    display = ImageTk.PhotoImage(Image.open('imag.png'))
    label = tk.Label(image=display)
    label.image = display
    return label.pack()


greeting = tk.Label(text='Hello, I make QR code for you.')
txt_line = tk.Entry()
button_one = tk.Button(text='show', command=send)
greeting.pack()
txt_line.pack()
button_one.pack()
window.mainloop()
