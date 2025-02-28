import requests

from zipfile import ZipFile

file = ZipFile('asdf.zip')

with open('pass.txt', 'r') as f:
    for line in f.readlines():
        try:
            file.extractall(pwd=line.strip().encode())
            print('подходит', line)
        except:
            print('не подходит', line)



class ZipHacker():

    def __init__(self, path) -> None:
        self.path = path

    def hack(self):
        
        file = ZipFile(self.path)
        password = ''
        with open('pass.txt', 'r') as f:
            for line in f.readlines():
                try:
                    file.extractall(pwd=line.strip().encode())
                    password = line
                except:
                    pass
        return password


print(ZipHacker('asdf.zip').hack())

        