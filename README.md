# PDFtoTXT
Write all text info from a PDF, even if you can't copy-paste manually.
It also can translate on-the-fly.

**Tested on python 3.10**

# Requirements
* shutil
* pdf2image
* natsort
* deep_translator
* Inquirer
* Tesseract. Installed from a package manager

# Instalation
1. Clone this repo 
```sh
$ git clone https://github.com/sbritorodr/pdf_to_txt.git
```
2. Install tesseract. For Arch linux is avaliable on pacman.

```sh
$ sudo pacman -S tesseract
```
3. Don't forget to add trained data to tesseract. It is recommended to follow the [tesseract documentation](https://tesseract-ocr.github.io/tessdoc/).
Download tessdata files: https://tesseract-ocr.github.io/tessdoc/Data-Files.html 
> download the language traineddata files required by you and place them in this tessdata directory (/usr/local/share/tessdata).
> (From tesseract docs)

4. Install all pip requirements. Just copypaste this onto your terminal. Use pip3 instead if it doesn't work:
```sh
$ pip install shutil pdf2image natsort deep_translator inquirer
```
# Usage
1. Place `pdftotxt.py` where your pdf's are (Or move your pdf into the folder pdf2txt)
2. Execute the script under python3:

```sh
$ python3 pdftotxt.py
```
3. Follow up instructions.
4. **You can't translate if there's +5,000 characters on each page of your document**

# Uninstall
1. Delete pdftotxt.py
2. Delete all dependencies of pip and tesseract

```sh
$ pip uninstall shutil pdf2image natsort deep_translator inquirer
```
```sh
$ sudo pacman -Rs tesseract
```
3. Remove all your tessdata files inside `/usr/local/share/tessdata`

# Notes
install module [argos - translate](https://github.com/argosopentech/argos-translate) and implement this on the project. 
Either by adding a package in pip (argostranslate) and using the cli edition

You can make a fucking bodge and pipe cat "desired file to translate.txt" || argos-translate --from-lang fr --to-lang es > output.txt
Lol, that was horrible scripting but works.
