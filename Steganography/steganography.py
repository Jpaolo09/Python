from PIL import Image

img = Image.open("Capture.png")
pixels = list(img.getdata())