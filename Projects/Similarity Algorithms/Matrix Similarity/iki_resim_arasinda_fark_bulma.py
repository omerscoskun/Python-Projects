# region Imports

import cv2
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# endregion

# region Functions

def gorselMatrisiYazdir(gorsel):
    for i in gorsel:
        for pixel in i:
            print(pixel, end=" ")
        print("\n")

def pixelFark(pixel_1, pixel_2):
    fark = 0
    for i in range(3):
        fark += abs(pixel_1[i] - pixel_2[i]) / 255
    return fark 



# endregion

# region Main

gorsel_1 = cv2.imread("C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\matrix Similarity\\gorsel_1.png")
gorsel_2 = cv2.imread("C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\matrix Similarity\\gorsel_2.png")

print(gorsel_1.shape)
# Beklenen değer: (360,920,3)
print(gorsel_2.shape)
# Beklenen değer: (360,920,3)

# gorselMatrisiYazdir(gorsel_1) -> Beklenen değer: (360,920,3) 

yukseklik = gorsel_1.shape[0]
genislik = gorsel_1.shape[1]

fark = 0
for i in range(yukseklik):
    for j in range(genislik):
        fark += pixelFark(gorsel_1[i][j], gorsel_2[i][j])

farklilik_oran = 100 * fark / (genislik * yukseklik * 3)
print("İki görsel arasındaki farklılık oranı :" + str(farklilik_oran))



# endregion