'''Some img function'''


import os
import base64
import json
import requests


def img_func(img_path: str, new_img_name: str) -> int:
    '''Some img function'''

    url = 'https://postman-echo.com/post'

    files = {'image': open(img_path, 'rb')}
    response = requests.request('POST', url, files=files, stream=True)

    data = json.loads(response.text)

    filename = next(iter(data['files']))
    img = data['files'][filename]\
        .replace('data:application/octet-stream;base64,', '')
    img_content = base64.b64decode(img)

    with open(new_img_name, "wb") as new_img:
        new_img.write(img_content)

    return os.stat(new_img_name).st_size


def main():
    '''Call img_func function'''

    print(img_func(r'1.jpeg', "img.jpeg"))


if __name__ == '__main__':
    main()
