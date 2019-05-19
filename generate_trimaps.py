import os
from PIL import Image

image = Image.new('RGB', (640, 480))

# TODO create folder annotations/trimaps/

for filename in os.listdir('annotations/xmls'):
  filename = os.path.splitext(filename)[0]
  image.save('annotations/trimaps/' + filename + '.png')