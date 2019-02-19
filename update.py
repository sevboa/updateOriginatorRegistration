import os
import urllib.request

from zipfile import ZipFile

print('Downloading...')

url = 'https://github.com/sevboa/updateOriginatorRegistration/archive/master.zip'  
urllib.request.urlretrieve(url, 'master.zip')

#quit()

with ZipFile('master.zip', 'r') as zipFile:
    for name in zipFile.namelist():
        print('Extracted '+ '/'.join(name.split('/')[1:]))
        
        zipFile.extractall()
        #zipFile.extract('/'.join(name.split('/')[1:]))
        #os.rename(name,name.decode('cp866'))
    #os.removedirs(list_files[0])