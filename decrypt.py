from PIL import Image
import numpy as np

def extractPixels(img):
    img = np.array(img)
    img = img.reshape(-1, 3)
    pixels = [tuple(p) for p in img]
    return pixels

def decryptImageToText(path):
    
    img = Image.open(path)
    width, height = img.size
    pixels = np.ravel(extractPixels(img))
    data, byte = '', ''
    try:
        for p in pixels:
            if p % 2 == 0:
                byte += '0'
            else:
                byte += '1'
            if len(byte) == 8:
                byte = chr(int(byte, 2))
                if byte == '~':
                    print(data)
                data += byte
                byte = ''
    except:
        pass

def getData(data):
    binary_string = data

    binary_data = binascii.unhexlify('%0*X' % ((len(binary_string) + 3) // 4, int(binary_string, 2)))

    decoded_data = pickle.loads(base64.b64decode(binary_data))

    original_data = decoded_data["data"]
    name = decoded_data["metadata"]["name"]
    file_format = decoded_data["metadata"]["format"]

    output_file_path = Path(f"{name}.{file_format}")
    with output_file_path.open('wb') as new_file:
        new_file.write(original_data)

    exit()

decryptImageToText("encrypted.png")