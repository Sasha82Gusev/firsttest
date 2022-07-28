import requests
from pprint import pprint
#from yadisk import YaDisk
from yadisk import yadisk


token = 'AQAAAAAS8FNvAADLW6rn6rr7aUahsINUYMVbAp8'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


    def get_headers(self):
        return {
            'Content-Type': 'aplication/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files(self):
        files_url='https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    #path_to_file = 'c:\11.txt'
    #uploader = YaUploader(token)
    #result = uploader.upload(path_to_file)
    ya = yadisk.YaDisk(token=token)
    pprint(list(ya.get_files(limit = 1, fields = 'name')))