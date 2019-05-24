# Run from desktop
from pdf2image import convert_from_path, convert_from_bytes
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image
import cv2
import numpy as np
from fpdf import FPDF
import matplotlib.pyplot as plt
import img2pdf
import shutil
import os

def convert(fn):
    FN = fn
    images = convert_from_path('390files/' + FN)

    # ex[0][0] is the first column of the first line, 
    # ex[0][0][0] is the red component of the first pixel, 
    # ex[0][0][1] is the green component, 
    # and ex[0][0][2] is the blue component.
    result = []
    i = 0
    for img in images:
        im = np.asarray(img)
        # im = im.copy()
        # black_pixels_mask = np.all(im == [0, 0, 0], axis=2)
        # non_black_pixels_mask = np.any(im != [0, 0, 0], axis=-1) 
        # im[black_pixels_mask] = [255,255,255]
        # im[non_black_pixels_mask] = [0, 0, 0]
        im = im.copy()
        red_mask = np.all(im >= [250, 0, 0], axis = -1)
        blue_mask = np.all(im >= [0, 101, 255], axis = -1)
        green_mask = np.all(im >= [0, 250, 0], axis = -1)
        # black_pixels_mask = np.all(im == [0, 0, 0], axis=-1)
        # non_black_pixels_mask = np.any(im != [0, 0, 0], axis=-1) 
        im[red_mask] = [255,255,255]
        im[blue_mask] = [255,255,255]
        im[green_mask] = [255,255,255]
        # im[black_pixels_mask] = [0, 0, 0]
        # im[non_black_pixels_mask] = [255,255,255]
        
        if not os.path.exists('390files/tmp/'):
            os.mkdir('390files/tmp/')
        plt.imsave("390files/tmp/"+str(i)+".jpg", im)
        result.append(str(i))
        i += 1

    # plt.imshow(im)
    # plt.show()

    with open("390files/no-sol/" + FN, "wb") as f:
        f.write(img2pdf.convert(['390files/tmp/' + i for i in sorted(os.listdir('390files/tmp/')) if i.endswith(".jpg")]))
    shutil.rmtree('390files/tmp/')
    print(FN + " Done.")

if __name__ == "__main__":
    files = [i for i in sorted(os.listdir('390files/')) \
    if i.startswith("test3") and i.endswith(".pdf")]
    for fn in files:
        print("start " + fn)
        convert(fn)
    # convert("test3_spring08.pdf")

