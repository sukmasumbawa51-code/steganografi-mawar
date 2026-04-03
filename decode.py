from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    binary_data = ""
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for n in range(3):
                binary_data += str(pixel[n] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    message = ""
    for byte in all_bytes:
        if byte == "11111110":
            break
        message += chr(int(byte, 2))

    return message

secret = decode_image("stego.png")
print("Pesan tersembunyi:", secret)
