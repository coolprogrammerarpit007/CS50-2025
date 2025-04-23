from PIL import Image

filename = "buildings.jpg"

with Image.open(filename) as img:
    img.load()
#  Loading and showing the image
# print(type(img))
# print(isinstance(img,Image.Image))
# print(img.format)
# print(img.size)
# print(img.mode)
# img.show()


#  Method to crop the image.
cropped_img = img.crop((300,150,700,1000))
# cropped_img.show()

resized_img = cropped_img.resize((cropped_img.width // 4 , cropped_img.height //4))
# resized_img.show()