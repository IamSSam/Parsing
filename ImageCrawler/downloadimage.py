import urllib.request, json
import os


def download_web_images(url, num):
    full_name = "THE NAME_" + str(num) + ".jpg" # Input name of file what you want

    directory = "path" # Input name of directory what you want
    if not os.path.exists(directory):
        os.makedirs(directory)

    fullfilename = os.path.join(directory, full_name)
    urllib.request.urlretrieve(url, fullfilename)

with urllib.request.urlopen("URL") as url: # Input URL
    data = json.loads(url.read().decode())
    print(str(data) + "\n")
    img_url = []
    for item in data:
        images = item.get('images')
        for image in images:
            if "non-contrast" == image.get('aux_modality') and "Axial" == image.get('plane_projection'):
                img_url.append(image.get('public_filename'))

    img_url.sort()

    for index, item in enumerate(img_url):
           download_web_images(item, index)
