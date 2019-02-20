import os
import urllib.request
import shutil

from zipfile import ZipFile

class updater:
    BranchName = str()
    ArhiveName = str()
    Url = str()

    def __init__(self, branchName):
        self.BranchName = branchName
        self.ArhiveName = branchName + '.zip'

    def downloadArhive(self):
        self.Url = 'https://github.com/sevboa/updateOriginatorRegistration/archive/' + self.ArhiveName
        print('Downloading...')
        urllib.request.urlretrieve(self.Url, self.ArhiveName)

    def unzipArhive(self):
        with ZipFile(self.ArhiveName, 'r') as zipFile:
            try:
                shutil.rmtree('class/', ignore_errors=False, onerror=None)
            except(FileNotFoundError):
                ''
            try:
                os.remove('test.py')
            except(FileNotFoundError):
                ''
            try:   
                os.remove('update.py')
            except(FileNotFoundError):
                ''
            for name in zipFile.namelist():
                print(name)
                fileName = '/'.join(name.split('/')[1:])
                print(fileName)
                if fileName != '':
                    if fileName[-1] == '/':
                        try:
                            os.makedirs(fileName)
                            print('Directory create '+ fileName)
                        except(FileExistsError):
                            print('Directory exist '+ fileName)
                    else:
                        with open(fileName, 'wb') as f:
                            f.write(zipFile.read(name))
                            print('Extracted '+ '/'.join(name.split('/')[1:]))
                
            #os.removedirs(list_files[0])
        os.remove(self.ArhiveName)

Updater = updater('master')

Updater.downloadArhive()
Updater.unzipArhive()
