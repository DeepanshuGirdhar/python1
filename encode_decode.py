
from steganography.steganography import Steganography
def send_message():
    # prepare the message
    orig_image = raw_input("Provide the name of the image to hide the message : ")
    op_image = raw_input("Provide the name of the output image  : ")
    text = raw_input("Enter your message here : ")
    # Encrypt the message
    Steganography.encode(orig_image,op_image,text)
    # Successful message
    print "Your message encrypted successfully."


def read_message():
    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message

input=int(raw_input("1.Encode a message\n2. Decode a message\nPress any key....."))
if (input==1):
    send_message()
elif(input==2):
    read_message()
else:
    print "Please enter a valid choice"


