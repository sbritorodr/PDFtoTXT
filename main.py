#This is only functional and I know is POORLY written. I've no time and I'm doing this just for needs.
import os
import shutil
from pdf2image import convert_from_path

title = str(input("Select the name of the file here ('foo.pdf)\n") or "foo.pdf")
deleteCache = False
if str(input('Delete cache? y/n \n')) == 'n':
    deleteCache = False
# parse pdf into multiple png's


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




#this loop selects only the desired format type
formattype = "png"
listfiles = []
for file in os.listdir('./input'):
    if file.endswith("." + formattype):
        listfiles.append(file)


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

with open('output_ocr_file.txt','wb') as wfd:
    for f in listtxt:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd)

# delete all evidence
if deleteCache:
    try: shutil.rmtree('./output')
    except: print("Failed to delete the folder. Is already deleted or protected?")
    try: shutil.rmtree('./input')
    except: print("Failed to delete the folder. Is already deleted or protected?")


# Google Translator has a char limit of 5,000, so we need to split the txt files again,
# translate each text individually and re-merge all into one



#translate from gogle
#there's a 5,000 character limit on google translator :(

# from deep_translator import GoogleTranslator

# translated = GoogleTranslator(source='auto', target='es').translate_file('output_file.txt')
# output_translated = open('output_file.txt')
# output_translated.write(translated)
# output_translated.close() 
