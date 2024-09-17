import qrcode
import random
import cv2
import pyzbar

def input_from_user():
    raw = input("Enter URL/Text to be encoded in qr code:") #Taking input from user.
    qrcode_generator(raw) 

def qrcode_generator(raw):
    #Initializing the qrcode with custom settings
    qr = qrcode.QRCode(
        version = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size =30,
        border = 2
    )
    
    #adding data to QR Code
    qr.add_data(raw)
    
    #Finalizing the QR Code
    qr.make(fit=True)
    
    #Randomly naming the QR Code
    img_number = str(random.randint(0,100000))
    img_name = f"{img_number}.png"
    
    #Saving the QR Code as image
    img = qr.make_image(fill='black', back_color = 'white') #RGB Value supported
    img.save(img_name)
    print(f"QR code in saved as {img_name}.")

    #Calling decoder function
    qr_code_decoder(img_name)

def qr_code_decoder(img_name):
    img_load = cv2.imread(img_name)     #Loading the image
    qcd = cv2.QRCodeDetector()          #Initalizing the QR Code detector
    retval, decoded_info,c,d= qcd.detectAndDecodeMulti(img_load)   #Getting the data
    
    if retval == True:
        print(decoded_info)

    else:
        print("QR CODE not Detected")



input_from_user()