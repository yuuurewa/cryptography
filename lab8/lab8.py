from PIL import Image
import numpy as np

def text_to_bits(text):
    return ''.join(format(ord(char), '08b') for char in text)

def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def embed_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    width, height = img.size

    message_bits = text_to_bits(message)
    message_len = len(message_bits)

    max_bits = width * height * 3
    if message_len > max_bits:
        raise ValueError("Message too long for this image!")

    bit_index = 0
    for i in range(width):
        for j in range(height):
            for k in range(3):  # R,G,B channels
                if bit_index < message_len:
                    pixels[j, i, k] = (pixels[j, i, k] & 0xFE) | int(message_bits[bit_index])
                    bit_index += 1
                else:
                    break

    Image.fromarray(pixels).save(output_path)
    print(f"Message embedded in {output_path}!")

def extract_lsb(image_path, message_len_bits):
    img = Image.open(image_path)
    pixels = np.array(img)
    width, height = img.size

    extracted_bits = []
    for i in range(width):
        for j in range(height):
            for k in range(3):
                if len(extracted_bits) >= message_len_bits:
                    break
                extracted_bits.append(str(pixels[j, i, k] & 1))
            else:
                continue
            break
        else:
            continue
        break

    return bits_to_text(''.join(extracted_bits))

image_path = "Car.bmp"
output_path = "encoded.bmp"
message = "Secret message!"

embed_lsb(image_path, message, output_path)

message_bits = text_to_bits(message)
extracted_message = extract_lsb(output_path, len(message_bits))
print("Extracted message:", extracted_message)