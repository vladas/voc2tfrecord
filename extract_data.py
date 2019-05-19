import os
from zipfile import ZipFile
from shutil import copy



fileName = 'dataset.zip'
ds = ZipFile(fileName)
ds.extractall()
#os.remove(fileName)
print('Extracted zip file ' + fileName)

image_files=os.listdir('images')
im_files=[x.split('.')[0] for x in image_files]
with open('annotations/trainval.txt', 'w') as text_file:
  for row in im_files:
    text_file.write(row + '\n')