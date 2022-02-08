#! ./pdf_to_txt/
#This is only functional and I know is POORLY written. I've no time and I'm doing this just for needs.
import os
import click
import shutil
from pdf2image import convert_from_path
from natsort import natsorted # because python string sorts is kinda bad tbh
from deep_translator import GoogleTranslator

def usrInput():
    usrInput.title = str(input("Select the name of the file here ('input.pdf)\n") or "NONE")
    usrInput.output_ocr_file = str(input("Select your .txt output name (without extension) \n") or "output_ocr_file") + ".txt"
    usrInput.deleteCache = True
    if not click.confirm('Delete folders?', default=True): # by default it will delete the folders
        usrInput.deleteCache = False

    usrInput.translate = False
    if click.confirm(" Translate?", default= False):
        usrInput.translate = True

    

def PDFtoPNG(): # convert pdf into multiple png's
    # auto selection of pdf
    pdf_file = []
    for file in os.listdir('./'):
        if file.endswith(".pdf"):
            pdf_file.append(file)
    if usrInput.title == "NONE":
        usrInput.title = pdf_file[0]
    try: 
        print('creating the input folder')
        os.mkdir('./input')
    except FileExistsError: 
        print('input folder already generated')

    images = convert_from_path(f'{usrInput.title}', 200)
    for i, image in enumerate(images):
        image.save(f'./input/page_{i}.png')


#this loop selects only the desired format type
def fileSelector():
    formattype = "png"
    fileSelector.listfiles = []
    for file in os.listdir('./input'):
        if file.endswith("." + formattype):
            fileSelector.listfiles.append(file)

def genOutputfolder():
    try: 
        print('creating the output folder')
        os.mkdir('./output')
    except: 
        print('output folder already generated')

# Tesseract main function
def ocrMain():
    for element in fileSelector.listfiles:
        os.system('tesseract -l fra ' + './input/'+ element + ' ./output/' + element)

#translate from gogle
#there's a 5,000 character limit on google translator :(
def genOutputTrans():
    try: 
        print('creating the output folder')
        os.mkdir('./output_translated')
    except: 
        print('output folder already generated')

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
    print(type(answers))
    print(answers['lang'])


def translatefromGoogle():
    listtxt_trans = []
    for file in os.listdir('./output'):
        if file.endswith('.txt'):
            listtxt_trans.append('./output/' + file)
    i = 0
    for file in natsorted(listtxt_trans):
        translated = GoogleTranslator(source='auto', target=translateOpt.answers['lang']).translate_file(file)
        output_translated = open(f'./output_translated/{i}.txt', 'w')
        output_translated.write(translated)
        output_translated.close() 
        i = i+1 #sorry for this gibberish, but for some reason I can't find any better way

#merge all into one txt (Translated)
def mergeALLtxt():
    listtxt = []
    for file in os.listdir('./output'):
        if file.endswith('.txt'):
            listtxt.append('./output/' + file)
    with open(usrInput.output_ocr_file,'wb') as wfd:
        for f in natsorted(listtxt): # Sorted all pages
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)

#merge all into one txt (Translated)
def mergeALLtxtTranslated():
    listtxt = []
    for file in os.listdir('./output_translated'):
        if file.endswith('.txt'):
            listtxt.append('./output_translated/' + file)
    with open(usrInput.output_ocr_file,'wb') as wfd:
        for f in natsorted(listtxt): # Sorted all pages
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)


# delete all evidence
def rmEverything():
    if usrInput.deleteCache:
        try: 
            shutil.rmtree('./output')
        except FileNotFoundError: 
            print("Failed to delete the folder. Is already deleted or protected?")
        try: 
            shutil.rmtree('./output_translated')
        except FileNotFoundError: 
            print("Failed to delete the folder. Is already deleted or protected?")
        try: 
            shutil.rmtree('./input')
        except FileNotFoundError: 
            print("Failed to delete the folder. Is already deleted or protected?")

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
    rmEverything()
    
if __name__ == "__main__":
    main()
