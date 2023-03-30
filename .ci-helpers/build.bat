@echo off

echo
echo Building 'scr2ocr'...
echo

pyinstaller -y -n scr2ocr --onedir --windowed scr2ocr.py --add-data="tesseract;tesseract"

Exit
