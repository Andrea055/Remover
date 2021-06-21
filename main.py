import requests                                                             #import libraries for api call and save       
import shutil

url = 'https://roughs.ru/api/remove-bg?url='                                #define api url for call
myobj = input("Write url of image you want to remove background:")          #specify url of image
source = '&source_from=test@gmail.com'                                      #you can change email, it's useless in this case. you mustn't delete "&source_from"
entire = url + myobj + source                                               #define complete url for api call
filename = 'no-bg.png'                                                      #you can change filename if you want


r = requests.get(entire, stream = True)                                     #Api recall, fondamentaly for the working of script


# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero,don't touch it!
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission and save image,don't touch it again :-)
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image without background sucessfully elaborated, saved as: ',filename)
else:
    print('Image Couldn\'t be retreived,retry and check url please or open issue on github')
