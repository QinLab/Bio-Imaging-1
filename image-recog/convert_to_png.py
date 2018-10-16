from PIL import Image
import glob


for image_path in glob.glob("dataset/train/Non-Reproductive/*.jpg"):
    im = Image.open(image_path)
    im.save(image_path+".png")