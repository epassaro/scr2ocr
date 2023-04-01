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

### macOS
Currently not tested. Not built. Use development install.

### Windows
Currently not tested, JamSpell is not supported. **Please do not open issues about the Windows build!**

## Development

1. Requires installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or a [Miniforge variant](https://github.com/conda-forge/miniforge/releases/latest) (we recommend **Mambaforge**)
2. Install the required packages in a new virtual environment using the lockfile meant for your platform
  ```
  $ mamba create -n mamba create -n scr2ocr --file conda-linux-64.lock
  ```
3. Activate the environment and install `jamspell` with `pip`
  ```
  $ mamba activate scr2ocr
  $ pip install jamspell==0.0.12
  ```
4. Place a JamSpell model file named `model.bin` inside the `jamspell` folder
5. Run the script
  ```
  $ python scr2ocr.py
  ```

## Authors
- [@epassaro](https://github.com/epassaro)
- [@agostinaf](https://github.com/agostinaf)
- [@fitosb](https://github.com/fitosb)

## License
![This software is released under the MIT license](https://img.shields.io/github/license/epassaro/scr2ocr)
