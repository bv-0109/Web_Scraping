import requests
import os

def download_image(image_url, title, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    image = requests.get(image_url).content

    filename = title.replace(" ", "_") + ".jpg"

    filepath = os.path.join(folder, filename)

    with open(filepath, "wb") as file:
        file.write(image)

    return filepath