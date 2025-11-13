from PIL import Image
import struct
import os

fileName = input('Image file name (with extenstion): ')

def doStuff():
    img = Image.open(fileName).convert('RGBA')

    """
    ORIG_WIDTH = 32
    ORIG_HEIGHT = 32

    # Resize if image is wrong size
    if img.size != (ORIG_WIDTH, ORIG_HEIGHT):
        print(f"Warning: image size {img.size} does not match expected {ORIG_WIDTH}x{ORIG_HEIGHT}. Resizing...")
        img = img.resize((ORIG_WIDTH, ORIG_HEIGHT))
    """

    width, height = img.size

    # Flip vertically and get BGRA bytes
    pixels = img.transpose(Image.FLIP_TOP_BOTTOM).tobytes('raw', 'BGRA')

    # Build BITMAPINFOHEADER only (40 bytes)
    header = struct.pack(
        '<IIIHHIIIIII',
        40,             # header size
        width,          # width
        height * 2,     # height (XOR + AND masks)
        1,              # planes
        32,             # bits per pixel
        0,              # compression
        0x1080,         # biSizeImage
        0, 0, 0, 0      # unused fields
    )

    # Combine header + pixels
    data = header + pixels

    # Convert to hex string
    hex_str = ' '.join(f'{b:02X}' for b in data)

    newFileName = input('HEX file name: ')

    # Save to text file
    with open(newFileName + '.txt', 'w') as f:
        f.write(hex_str)

    print(f'Saved to {newFileName}.txt')


if os.path.exists(fileName):
    doStuff()
else:
    print("This file: [" + fileName + "] doesn't exist!")

input("Press Enter to close...")