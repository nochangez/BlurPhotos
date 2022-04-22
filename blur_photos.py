# coding=utf-8


from os import listdir
from random import randint
from PIL import Image, ImageFilter

# from data.config import path_to_pictures


def blur_photos(from_path: str = f"/Users/nochanga/PycharmProjects/EyeOfGodBot/pictures/real_nude/",
                to_path: str = f"/Users/nochanga/PycharmProjects/EyeOfGodBot/pictures/fake_nude/"):
    print(f"[all] found {len(listdir(path=from_path))} objects")  # photos count

    for image_name in listdir(path=from_path):
        try:
            print(f"[blurring] {from_path}{image_name}")  # log start blurring

            original_image = Image.open(f"{from_path}{image_name}")  # open original image
            blurred_image = original_image.filter(ImageFilter.GaussianBlur(5))  # blurred image
            print(f"[blurred] {from_path}{image_name}")  # log blurred

            blurred_image_name = str(randint(4, 100000))  # generate name for blurred image
            blurred_image.save(f"{to_path}{blurred_image_name}.jpeg")  # save blurred image
            print(f"[saved] {to_path}{blurred_image_name}.jpeg\n\n")  # saved blurred
        except Exception as blurring_error:
            print(f"[error] an error has occurred while blurring: {blurring_error}")  # log blurring error
            continue


blur_photos()  # start blurring
