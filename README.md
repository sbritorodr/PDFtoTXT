# PDFtoTXT
Write all text info from a PDF, even if you can't copy-paste it manually or is from an image and translate it *on-the-fly*.

 <p style="text-align: center;font-size:1.35rem"> <b> Tested on <span style="color:#135BE3"> py</span><span style="color:#EBBE0D">thon 3.10</span> </b> </p>

# Requirements
## From a package manager (pacman, apt...)
* Tesseract
* plopper
## From pip
* pdf2image
* natsort
* deep_translator
* Inquirer
* progressbar

# Instalation
1. Clone this repo or download the latest PDFtoTXT.py file from [releases](https://github.com/sbritorodr/PDFtoTXT/releases)
```sh
$ git clone https://github.com/sbritorodr/pdf_to_txt.git
```


2. Install tesseract using any package manager. (pacman, apt, brew...)

```sh
$ sudo pacman -S tesseract plopper
```
3. Don't forget to add trained data to tesseract.
Download tessdata files: https://tesseract-ocr.github.io/tessdoc/Data-Files.html and place it in the folder said in the [tesseract documentation](https://tesseract-ocr.github.io/tessdoc/).
> download the language traineddata files required by you and place them in this tessdata directory (/usr/local/share/tessdata).


4. Install all pip requirements. Just copypaste this onto your terminal. Use pip3 instead if it doesn't work:
```sh
$ pip install -r requirements.txt
```
# Usage
1. Place `pdftotxt.py` where your pdf's are (Or move your pdf into the folder pdf2txt if you cloned the repo)
2. Execute the script under python3:

```sh
$ python3 pdftotxt.py
```
3. Follow up the instructions. By default, the program picks any pdf from the folder, disables translation and merges all into `./output_ocr_file.txt`
4. <span style="color:#AF0E0E">**You cannot translate your document if there's +5,000 characters on each page**</span>
5. If your desired language destination is not avaliable, you can add it by editing the script (lines 70 to 75). Check if it works and create a PR if you want to add this option to the main project:
```python
70    questions = [
71        inq.List('lang',
72                message="Select which language you want to use",
73                choices=['spanish', 'english', 'french','italian', 'portuguese', 'german'] # add here your language/s
74            ),
75    ]
```

# Uninstall
1. Delete `pdftotxt.py`
2. Delete all installed dependencies of pip, `tesseract` and `plopper`
```sh
$ pip uninstall -r requirements.txt
```
```sh
$ sudo pacman -Rs tesseract plopper
```
3. Remove all your tessdata files inside `/usr/local/share/tessdata` if the uninstall has not already deleted it.
