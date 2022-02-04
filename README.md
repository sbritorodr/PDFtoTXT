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
2. Install tesseract

```sh
$ sudo pacman -S tesseract
```


# Notes
install module [argos - translate](https://github.com/argosopentech/argos-translate) and implement this on the project. 
Either by adding a package in pip (argostranslate) and using the cli edition

You can make a fucking bodge and pipe cat "desired file to translate.txt" || argos-translate --from-lang fr --to-lang es > output.txt
Lol, that was horrible scripting but works.
