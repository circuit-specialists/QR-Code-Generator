#!/usr/bin/env python3

import qrcode
import PIL
from PIL import Image
import io

# gui classess
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class URL2QR:
    def __init__(self):
        root = Tk()
        root.title('URL to QR Code')
        root.geometry('480x120')

        # Control Frame
        full_frame = Frame(root)

        # URL Input
        url_label = Label(full_frame, text="Input URL: ").pack(side=LEFT)
        self.url_input = Entry(full_frame)
        self.url_input.pack(side=LEFT)

        # Save Button
        save_button = Button(full_frame, text='Save',
                             command=self.createQR).pack(side=RIGHT, padx=5)

        # Pack Full Frame
        full_frame.pack()

        # Run man GUI threads
        root.mainloop()

    def createQR(self):
        url_string = self.url_input.get()
        filename = filedialog.asksaveasfilename()
        last_index = filename.rfind('/')

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url_string)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename + ".png")


if __name__ == "__main__":
    main_thread = URL2QR()
