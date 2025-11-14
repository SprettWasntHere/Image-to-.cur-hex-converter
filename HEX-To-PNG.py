import binascii
from PIL import Image
import os

fuck = input('HEX filename: ')

def doStuff():
    with open(fuck) as text_file:
        contents = text_file.read()

    hex_data = contents

    data = binascii.unhexlify(hex_data.replace(' ', '').replace('\n', ''))

    # Extract width and height from known header offsets in the HEX/BMP file.
    width = int.from_bytes(data[4:8], 'little')
    height = int.from_bytes(data[8:12], 'little') // 2  # Height might be doubled depending on format, so //2

    # .cur header offset. Change if your format has a different offset.
    pixel_data = data[40:]
    img_bytes = pixel_data[:width * height * 4]

    img = Image.frombuffer('RGBA', (width, height), img_bytes, 'raw', 'BGRA', 0, 1)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)

    fileName = input('Image file name?: ')
    img.save(fileName + '.png')
    print(f'Saved {width}x{height} PNG to ' + fileName + '.png')

if os.path.exists(fuck):
    doStuff()
else:
    print("This file: [" + fuck + "] doesn't exist!")


input('Done! Press enter to close... ')
