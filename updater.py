import os
import urllib.request

from zipfile import ZipFile

arhiveName = 'master.zip'
url = 'https://github.com/sevboa/updateOriginatorRegistration/archive/' + arhiveName  

print('Downloading...')

#try:
##urllib.request.urlretrieve(url, arhiveName)
#except(urllib.error.URLError):
#    print('Error host!')
#    quit()

with ZipFile(arhiveName, 'r') as zipFile:
    #os.remove('test')
    for name in zipFile.namelist():
        #zipFile.extractall()
        print(name)
        file = '/'.join(name.split('/')[1:])
        print(file)
        if file != '':
            try:
                os.makedirs(os.getcwd()+'/test/'+'/'.join(name.split('/')[1:-1]))
            except(FileExistsError):
                print('file exists')
            #quit()
            with open('test/'+'/'.join(name.split('/')[1:]), 'wb') as f:
                f.write(zipFile.read(name))
                print('Extracted '+ '/'.join(name.split('/')[1:]))
        
        #zipFile.extract(name, 'test/'+'/'.join(name.split('/')[1:]))
        #os.rename(name,name.decode('cp866'))
    #os.removedirs(list_files[0])
    ##os.remove(arhiveName)