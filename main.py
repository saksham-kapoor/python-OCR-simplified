# pylint: skip-file
import re
import os
import webbrowser
from PIL import Image
import pytesseract
import cv2

# Set your tesseract.exe path here
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Specify Image Path/Name
img_name = "sample.jpg"

# Reading the image
img = cv2.imread(img_name)

# Converting the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create temporary image which will be fed to the tesseract engine
# file name has to be unique, therefore we have used OS
temp_img = "{}.jpg".format(os.getpid())

# Writing the image to the temporary image file
cv2.imwrite(temp_img, gray)

# Getting text from image
text = pytesseract.image_to_string(Image.open(temp_img))

# Finding the url using
urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', text)

# Deleting the temporary file
os.remove(temp_img)

# Export text from image to a text file (Optional)
text_file = open(f"{img_name}_text.txt", "w")
text_file.write(text)
text_file.close()

# Export urls from image to a text file (Optional)
urls_file = open(f"{img_name}_urls.txt", "w")
for url in urls:
    urls_file.write(url + "\n")

# Open Urls in the default browser
# If Multiple urls, it will open them in seperate tabs
flag = 0
for url in urls:
    if flag == 0:
        webbrowser.open(url)
    else:
        webbrowser.open_new_tab(url)
    flag = flag + 1
