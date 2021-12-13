import os
import shutil
from pdf2image import convert_from_path
# split pdf to png
title = str(input("Select the name of the file here ('foo.pdf) ") or "tema14.pdf")

pdf_file = []
for file in os.listdir('./'):
    if file.endswith(".pdf"):
        pdf_file.append(file)
try: 
    print('creating the input folder')
    os.mkdir('./input')
except: 
    print('input folder already generated')

images = convert_from_path(f'{title}', 200)
for i, image in enumerate(images):
    image.save(f'./input/save_{i}.png')

#os.system('for i in *.png; do tesseract -l fra $i  ${i%.*}; done')

#formattype = str(input("Enter your desired format type (ej. 'png') here: \n") or "png") #must not have dots
formattype = "png"
listfiles = []

#this loop selects only the desired format type
for file in os.listdir('./input'):
    if file.endswith("." + formattype):
        listfiles.append(file)

#print(listfiles)

try: 
    print('creating the output folder')
    os.mkdir('./output')
except: 
    print('output folder already generated')


for element in listfiles:
    os.system('tesseract -l fra ' + './input/'+ element + ' ./output/' + element)


#merge all into one txt
listtxt = []
for file in os.listdir('./output'):
    if file.endswith('.txt'):
        listtxt.append('./output/' + file)

with open('output_file.txt','wb') as wfd:
    for f in listtxt:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd)

#delete all evidence

try: shutil.rmtree('./output')
except: print("Failed to delete the folder. Is already deleted or protected?")
try: shutil.rmtree('./input')
except: print("Failed to delete the folder. Is already deleted or protected?")