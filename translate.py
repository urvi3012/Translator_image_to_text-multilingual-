import cv2
from PIL import Image
import PIL.Image
import googletrans
from pytesseract import image_to_string
import pytesseract
from google_trans_new import google_translator  


videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()

output = pytesseract.image_to_string(PIL.Image.open('NewPicture.jpg').convert("RGB"), lang='eng')
print (output)

translator = google_translator()  

print(googletrans.LANGUAGES)

l_dict = googletrans.LANGUAGES

output_language=input("Choose and Enter the language ")

key_list = list(l_dict.keys())
val_list = list(l_dict.values())
 
position = val_list.index(output_language)
language=key_list[position] 

translate_text = translator.translate(output,lang_tgt=language)  
print(translate_text)


