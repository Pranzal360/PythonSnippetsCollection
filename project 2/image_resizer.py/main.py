# install pillow,import
# open the image we want to resize using python
# print the current size . . specity the size we wanna change it to
# save it

from PIL import Image


def reize_image(x,y):
    img = Image.open('')

    print(f"current size: {img.size}")

    resized_img = img.resize((500,500))

    resized_img.save('{filename}.jpeg')

x = int(input("Enter the dimension you want(length): "))
y = int(input("Enter width  "))

reize_image(x,y)
