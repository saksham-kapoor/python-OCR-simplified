# Python OCR (Extracting URLs from images)

This tutorial aims to teach you how to use existing resources like tesseract, cv2, etc. to create a simple yet powerful OCR (optical character recognition system). We have added a new feature to the traditional OCR, i.e it can identify URLs in an image and also opens them in the web browser.

_Tutorial written by Saksham Kapoor. Get in touch_ [here.](https://www.linkedin.com/in/saksham-kapoor/)

## What We Will Accomplish

![Final OCR System](https://raw.githubusercontent.com/saksham-kapoor/python_ocr_simplified/master/readme_images/final.jpg)

### Excited? Let's gooo!

## Prerequisites

- Make sure you have python installed on your computer.
- Knowledge of basic python syntax.

## Step 1 - Install pytesseract OCR for windows [from here.](https://github.com/UB-Mannheim/tesseract/wiki)

- During the installation, use the default destination path.
- Copy the destination path as we'll need it soon.
- After the installation is complete, search for **environment variables** in the windows search bar.
- Click on **Edit the environment variables** search result.
- Click on **Environment Variables**, then under the heading **System Variables** click **Path** and then click **_Edit_**.
- Click **New**, then paste the path that we just copied.

### <ins>Check if the installation was successful</ins>

- Open windows powershell, type
  ```powershell
      tesseract
  ```
- If you see something like this, it was successfully installed

  ```
  Usage:
  C:\Program Files\Tesseract-OCR\tesseract.exe --help | --help-extra | --version
  C:\Program Files\Tesseract-OCR\tesseract.exe --list-langs
  C:\Program Files\Tesseract-OCR\tesseract.exe imagename outputbase [options...] [configfile...]

  OCR options:
  -l LANG[+LANG]        Specify language(s) used for OCR.
  NOTE: These options must occur before any configfile.

  Single options:
  --help                Show this help message.
  --help-extra          Show extra help for advanced users.
  --version             Show version information.
  --list-langs          List available languages for tesseract engine.

  ```

- However, if not, please read the instructions carefully and try again.

## Step 2 (Optional) - Tesseract Demo (Create Pdf from Image)

1. Download _sample.jpg_ from this repo (You can use any image).
2. Put it in a new folder.
3. Open terminal and **_cd_** to the new folder
   ```
   > cd Desktop/NewFolderName/
   ```
4. In the terminal type write the following command -
   ```
   > tesseract sample.jpg output pdf
   ```
5. Now check the folder, you will have a new pdf named **output.pdf** generated from the _sample.jpg_

## Step 3 - Install the following python packages-

1.  **pillow** (helps us to deal with images in python)
2.  **pytesseract** (creates a link between python and the tesseract OCR engine that we just installed)
3.  **opencv-python** (OpenCV - Open Source Computer Vision Library, is an open source computer vision and machine learning software library. We'll use it to read images.)

```powershell
    pip install pillow
    pip install pytesseract
    pip install opencv-python
```

## Step 4 - Create New Python file

I have named it _main.py_

## Step 5 - Import Required Python Modules

```python
    from PIL import Image
    import pytesseract
    import cv2
    import re
    import os
    import webbrowser
```

Usage :

1. **_re_** : Used to define a regular expression (regex) which will help us to search a url in the image text.
2. **_webbrowser_** : Used to open pages on the browser.
3. **_os_** : We will use this is generate a unique id and also manage files in the directory.
4. **_cv2_** : We will use this to read and convert the image to gray scale.

## Step 6 - Basic Config

```python
  # Set your tesseract.exe path here
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

  # Specify Path/Name of image you want to read
  img_name = "sample.jpg"
```

## Step 7 - Reading Text and URL from the Image

```python
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

```

## Step 8 (Optional) - Storing Text and URLs in '.txt' files

```python
  # Export text from image to a text file (Optional)
  text_file = open(f"{img_name}_text.txt", "w")
  text_file.write(text)
  text_file.close()

  # Export urls from image to a text file (Optional)
  urls_file = open(f"{img_name}_urls.txt", "w")
  for url in urls:
      urls_file.write(url + "\n")

```

## Step 9 - Opening the urls in your default web browser

```python
  # Open Urls in the default browser
  # If Multiple urls, it will open them in seperate tabs
  flag = 0
  for url in urls:
      if flag == 0:
          webbrowser.open(url)
      else:
          webbrowser.open_new_tab(url)
      flag = flag + 1

```

## Step 10 - Test it out

A sample photo has been provided in this repo.
Download/Clone the repo and run python script. It should just as expected.

### Run Python Scripts on windows -

- Open Script in any text editor, change img_name to the image of your choice.
- Open Windows Powershell.
- Change directory to the folder containing image and the script.

```powershell
  cd ./Desktop/FolderName
```

- Run script

```powershell
  python main.py
```

## Step 11 - Star and Share this tutorial :)

---

You can reach out to me at sakshamkapoor1729@gmail.com

### Hope you like this project!
