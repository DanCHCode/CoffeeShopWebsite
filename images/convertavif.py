from PIL import Image
import pillow_avif, os, re

for filename in os.listdir("coffeeshop2/images/"):
    if re.match(r".+\.avif", filename):
        filename2 = re.findall(r"(.+)\.avif", filename)[0]
        print(filename2)
        img = Image.open("coffeeshop2/images/" + filename)
        img.save("coffeeshop2/images/" + filename2 + ".jpg")


# img = Image.open('kimono.avif')
# img.save('kimono.jpg')

# #import PIL
# #print(PIL.__version__)
