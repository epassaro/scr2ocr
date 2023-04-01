# scr2ocr

Screenshot to OCR utility

## Installation and usage

### Prerequisites

### GNU/Linux
It should work on any distribution with `xclip` installed. Wayland is not supported (see: https://github.com/python-pillow/Pillow/issues/6312)]

1. Download the zip file from the [**releases section**](https://github.com/epassaro/scr2ocr/releases/tag/latest)
  ```
  $ wget https://github.com/epassaro/scr2ocr/releases/download/latest/scr2ocr-linux-64.zip
  ```
2. Extract and execute the `src2ocr` binary file
  ```
  unzip scr2ocr-linux-64.zip
  cd scr2ocr
  ./scr2ocr
  ```
   > :warning: **NOTE:** Loading the JamSpell model for the first time could take a while, don't worry!

3. Resize the window to cover the area you want to capture and press the square button
4. Captured text should be automatically copied to your clipboard :tada:

### Windows
Currently not tested, JamSpell is not supported. **Please do not open issues about the Windows build!**

## Authors
- [@epassaro](https://github.com/epassaro)
- [@agostinaf](https://github.com/agostinaf)
- [@fitosb](https://github.com/fitosb)

## License
![This software is released under the MIT license](https://img.shields.io/github/license/epassaro/scr2ocr)
