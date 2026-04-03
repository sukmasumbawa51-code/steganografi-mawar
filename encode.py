from PIL import Image

def encode_image(image_path, secret_message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
    binary_message += '1111111111111110'  # penanda akhir pesan

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = list(img.getpixel((col, row)))

                for n in range(3):
                    if index < len(binary_message):
                        pixel[n] = pixel[n] & ~1 | int(binary_message[index])
                        index += 1

                encoded.putpixel((col, row), tuple(pixel))

    encoded.save(output_path)
    print("Pesan berhasil disembunyikan!")

encode_image("gambar.png", "STI PRODI YANG DICINTAI", "stego.png")
