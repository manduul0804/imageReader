import  cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# img1 = cv2.imread('1.jpg')
# text = pytesseract.image_to_string(img1)
unfiltered_text = ''

for x in range(1,8):
    print(x)
    img = cv2.imread(f'{x}.jpg')
    text = pytesseract.image_to_string(img)
    unfiltered_text += text

# print(unfiltered_text)
new_text_file = ''
num = 2
for line in unfiltered_text.splitlines():
    if (line[:2].isdigit()):
        print(f'{num}. ' + line)
        new_text_file += f'{num}. ' + line + '\n'
        num += 1

try:
    with open('list.txt', 'w') as f:
        f.write(new_text_file)
except FileNotFoundError:
    print("The 'docs' directory does not exist")