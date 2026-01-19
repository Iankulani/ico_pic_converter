from PIL import Image

img = Image.open("spider.png")
img.save("app_icon.ico", format='ICO', sizes=[(256, 256)])