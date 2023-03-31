#!/usr/bin/env bash

set -e

echo

if [[ $(lsb_release -is) == "Ubuntu" ]]; then 
    echo "Building 'scr2ocr'..."; echo
    pyinstaller -y -n scr2ocr --onedir scr2ocr.py \
                --add-binary="tesseract-bin/tesseract:bin" \
                --add-binary="tesseract-bin/libtesseract.so.4:." \
                --add-binary="tesseract-bin/liblept.so.5:." \
                --add-data="tesseract-bin/spa.traineddata:tessdata" \
                --add-data="model.bin:jamspell"

else
    echo "Not an Ubuntu distro, skipping 'scr2ocr' build"

fi

exit 0
