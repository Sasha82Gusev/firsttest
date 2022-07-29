import requests

TOKEN=""

max_intelligence = 0

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url)

for id in range(len(response.json())):
    if response.json()[id]['name'] == 'Thanos' or response.json()[id]['name'] == 'Hulk' or response.json()[id]['name'] == 'Captain America':
        if response.json()[id]['powerstats']['intelligence'] > max_intelligence:
            max_intelligence_name = response.json()[id]['name']


print("Задание 1:Самый умный супергерой это ",max_intelligence_name)


class YandexDisk:

    def __init__(self,token):
        self.token=token



    def _get_upload_link(self,disk_file_path):
        upload_url='https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'aplication/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers = headers, params = params)
        #pprint(response.json())
        return response.json()


    def upload_file_to_disk(self,disk_file_path,filename):
        href=self._get_upload_link(disk_file_path = disk_file_path).get("href","")
        response=requests.put(href,data=open(filename,'rb'))
        headers = {'Content-Type': 'aplication/json', 'Authorization': 'OAuth {}'.format(self.token)}
        response.raise_for_status()
        if response.status_code == 201:
            print("Задание 2: Файл скопирован успешно")


if __name__ == '__main__':
    ya = YandexDisk(token = TOKEN)
    #pprint(ya.get_files_list())
    ya.upload_file_to_disk('/22.txt','C:\\11.txt')





