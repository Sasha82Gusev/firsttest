import requests

TOKEN="AQAAAAAS8FNvAADLW6rn6rr7aUahsINUYMVbAp8"

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
            print("Good")


if __name__ == '__main__':
    ya = YandexDisk(token = TOKEN)
    #pprint(ya.get_files_list())
    ya.upload_file_to_disk('/22.txt','C:\\11.txt')



