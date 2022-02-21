#! ./pdf_to_txt/
#This is only functional and I know is POORLY written. I've no time and I'm doing this just for needs.
import os
import click
import shutil
from pdf2image import convert_from_path
from natsort import natsorted # because python string sorts is kinda bad tbh
import deep_translator
import progressbar

def usrInput():
    usrInput.title = str(input("Select the name of the file here\n") or "NONE")
    usrInput.output_ocr_file = str(input("Select your .txt output name (without extension) \n") or "output_ocr_file") + ".txt"
    usrInput.deleteCache = True
    if not click.confirm('Delete folders?', default=True): # by default it will delete the folders
        usrInput.deleteCache = False

    usrInput.translate = False
    if click.confirm(" Translate?", default= False):
        usrInput.translate = True

    

def PDFtoPNG(): # convert pdf into multiple png's
    pbar = progressbar.ProgressBar(widgets=['Reading... ', progressbar.AnimatedMarker()]).start()
    # auto selection of pdf
    pdf_file = []
    for file in os.listdir('./'):
        if file.endswith(".pdf"):
            pdf_file.append(file)
    if usrInput.title == "NONE":
        usrInput.title = pdf_file[0]
    try: 
        #print('creating the input folder\n')
        os.mkdir('./.input')
    except FileExistsError: 
        #print('input folder already generated\n')
        pass

    images = convert_from_path(f'{usrInput.title}', 200)
    for i, image in enumerate(images):
        pbar.update(i)
        image.save(f'./.input/page_{i}.png')
    pbar.finish()


#this loop selects only the desired format type
def fileSelector():
    formattype = "png"
    fileSelector.listfiles = []
    for file in os.listdir('./.input'):
        if file.endswith("." + formattype):
            fileSelector.listfiles.append(file)

def genOutputfolder():
    try: 
        #print('creating the output folder\n')
        os.mkdir('./.output')
    except FileExistsError: 
        #print('output folder already generated\n')
        pass

# Tesseract main function
def ocrMain():
    pbar = progressbar.ProgressBar(widgets=['Writing...',progressbar.SimpleProgress(),progressbar.Percentage(), progressbar.Bar(),
               ' ', progressbar.ETA()], maxval=len(fileSelector.listfiles)).start()
    i = 0
    for element in fileSelector.listfiles:
        os.system('tesseract -l fra ' + './.input/'+ element + ' ./.output/' + element + '>/dev/null 2>&1') # the last part is for "disabling" output for tesseract
        pbar.update(i)
        i =i+1
    pbar.finish()

#translate from gogle
#there's a 5,000 character limit on google translator :(
def genOutputTrans():
    try: 
        #print('creating the output folder')
        os.mkdir('./.output_translated')
    except FileExistsError: 
        #print('output folder already generated')
        pass

def translateOpt():
    import inquirer as inq
    questions = [
        inq.List('lang',
                message="Select which language you want to use",
                choices=['spanish', 'english', 'french','italian', 'portuguese', 'german']
            ),
    ]
    answers = inq.prompt(questions)
    translateOpt.answers = answers


def translatefromGoogle():
    listtxt_trans = []
    for file in os.listdir('./.output'):
        if file.endswith('.txt'):
            listtxt_trans.append('./.output/' + file)
    pbar = progressbar.ProgressBar(widgets=['Translating...',progressbar.SimpleProgress(),progressbar.Percentage(), progressbar.Bar(),
            ' ', progressbar.ETA()], maxval=len(fileSelector.listfiles)).start()
    i = 0
    for file in natsorted(listtxt_trans):
        try:
            translated = deep_translator.GoogleTranslator(source='auto', target=translateOpt.answers['lang']).translate_file(file)
        except deep_translator.exceptions.NotValidLength: #if it's over 5.000, ignore that file and print an error
            translated = ""
            print("Page #", i ," is over 5.000 characters. Ignoring")
            pass
        output_translated = open(f'./.output_translated/{i}.txt', 'w')
        output_translated.write(translated)
        output_translated.close()
        pbar.update(i) 
        i = i+1 #sorry for this gibberish, but for some reason I can't find any better way
    pbar.finish()

#merge all into one txt (Translated)
def mergeALLtxt():
    listtxt = []
    for file in os.listdir('./.output'):
        if file.endswith('.txt'):
            listtxt.append('./.output/' + file)
    with open(usrInput.output_ocr_file,'wb') as wfd:
        for f in natsorted(listtxt): # Sorted all pages
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)

#merge all into one txt (Translated)
def mergeALLtxtTranslated():
    listtxt = []
    for file in os.listdir('./.output_translated'):
        if file.endswith('.txt'):
            listtxt.append('./.output_translated/' + file)
    with open(usrInput.output_ocr_file,'wb') as wfd:
        for f in natsorted(listtxt): # Sorted all pages
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)

def rmFolder(folder_name):
    if usrInput.deleteCache:
        try: 
            shutil.rmtree(folder_name)
        except FileNotFoundError: 
            print("Failed to delete", folder_name ,"Is already deleted or protected?")

def main():
    usrInput()
    if usrInput.translate:
        translateOpt()
    PDFtoPNG()
    fileSelector()
    genOutputfolder()
    ocrMain() #This ends the default program and asks the user for translation
    if usrInput.translate:
        genOutputTrans()
        translatefromGoogle()
        mergeALLtxtTranslated()
    else: mergeALLtxt()
    rmFolder('./.output')
    if usrInput.translate:
        rmFolder('./.output_translated')
    rmFolder('./.input')
    
if __name__ == "__main__":
    main()
