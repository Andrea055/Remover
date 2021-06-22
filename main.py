import requests
import shutil
import os

urluploader = 'your-server-ip/upload.php'                                               #check my php&python file uploader https://github.com/Andrea055/Python-File-uploader-PHP
url = 'https://roughs.ru/api/remove-bg?url='
urls = "http://3b8j.l.time4vps.cloud/" 
urlupload = "0"
possibility = input("Do you want remove background of an image on internet,press 1 or in your pc, press 2?")
#
if possibility == "1":
    myobj = input("Write url of image you want to remove background:")
else:
    file = input("Name of the file you want upload:")
#
while possibility == "2" and os.path.isfile(file) == False:
    file = input("File does not exist, please rewrite the name of the file you want upload:")
#
if possibility == "2":
    files = {'file': open(file, 'rb')}
    urlupload = urls + file
#
source = '&source_from=test@gmail.com'


print(urlupload)
#
if possibility == "1":
    entire = url + myobj + source
else:
    entire = url + urlupload + source
#   
filename = 'no-bg.png'
#
if possibility == "2":
    print("if response is 200 the transfer is complete without error otherwise there is an error")
    r = requests.post(urluploader, files=files)
    print("response:", r.status_code)
print(entire)
r = requests.get(entire, stream = True)
# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image without background sucessfully elaborated, saved as: ',filename)
else:
    print('Image Couldn\'t be retreived,retry and check url please or open issue on github')

