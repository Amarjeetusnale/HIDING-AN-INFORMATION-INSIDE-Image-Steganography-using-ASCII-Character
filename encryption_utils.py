
from PIL import Image # Ensure you have Pillow installed: pip install Pillow

def encode_message(img, message):
    binary = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # Delimiter
    data = iter(img.getdata())
    new_pixels = []

    for pixel in data:
        r, g, b = pixel[:3]
        new_pixel = list(pixel)

        for i in range(3):
            if binary:
                new_pixel[i] = new_pixel[i] & ~1 | int(binary[0])
                binary = binary[1:]
            else:
                break

        new_pixels.append(tuple(new_pixel))

        if not binary:
            break

    new_pixels.extend(data)
    img.putdata(new_pixels)
    return img

def decode_message(img):
    data = ''
    for pixel in img.getdata():
        for color in pixel[:3]:
            data += str(color & 1)

    binary_values = [data[i:i+8] for i in range(0, len(data), 8)]
    message = ''
    for binary in binary_values:
        char = chr(int(binary, 2))
        message += char
        if message[-2:] == '~~':  # Delimiter
            break
    return message[:-2]
