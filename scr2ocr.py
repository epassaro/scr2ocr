#!/usr/bin/env python

import os
import sys
import platform
from tkinter import Tk, Button

import jamspell
import pyperclip
import pytesseract
from PIL import ImageGrab

REFRESH = 100  # in milliseconds
WIDTH, HEIGHT = (280, 100)
ALPHA = 0.55
FLAGS = r'--oem 3 --psm 6 -l spa'

cwd = os.path.dirname(__file__)
conda = os.path.exists(os.path.join(sys.prefix, "conda-meta"))

if platform.system() == "Windows":
    corr = None

    if not conda:
        pytesseract.pytesseract.tesseract_cmd = os.path.abspath(os.path.join(cwd, "tesseract", "tesseract.exe"))
        os.environ["TESSDATA_PREFIX"] = os.path.abspath(os.path.join(cwd, "tessdata"))

else:
    print("\nLoading JamSpell model...", end="")
    corr = jamspell.TSpellCorrector()   
    
    if corr.LoadLangModel(os.path.join(cwd, "jamspell", "model.bin")):
        print(" done")

    else:
        print(" not found")

    if not conda:
        pytesseract.pytesseract.tesseract_cmd = os.path.abspath(os.path.join(cwd, "bin", "tesseract"))
        os.environ["TESSDATA_PREFIX"] = os.path.abspath(os.path.join(cwd, "tessdata"))
        os.environ["LD_LIBRARY_PATH"] = cwd

def capture(corr=None):
    x, y = root.winfo_x(), root.winfo_y()
    w, h = root.winfo_width(), root.winfo_height()

    img = ImageGrab.grab(bbox=(x, y, x+w, y+h))
    text = pytesseract.image_to_string(img, config=FLAGS)

    if corr:
        text = corr.FixFragment(text)

    pyperclip.copy(text)


if __name__ == "__main__":
    root = Tk()
    root.title("scr2ocr")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.attributes("-type", "utility")

    # Linux transparency workaround, try `root.wm_attributes('-transparentcolor', root["bg"])` on Windows
    root.wait_visibility(root)
    root.wm_attributes("-alpha", ALPHA)

    button = Button(root, command=lambda: capture(corr=corr), relief="groove", borderwidth=2)
    button.pack(side="top", expand=True)

    root.mainloop()
