# Encoding Function
def encrypt(msg,shift):
  encoded_msg = ""
  for i in msg:
    encoded_msg += chr(ord(i)+shift)
  return encoded_msg

# Decoding Fuction
def decrypt(msg,shift):
  decoded_msg = ""
  for i in msg:
    decoded_msg +=  chr(ord(i)-shift)
  return decoded_msg


fuction_type = input("Type 'e' for encoding and 'd' for decoding\n ")
msg = input("Enter your message:\n").replace(" ","")
shift = int(input("Enter the shift:\n"))

# Condition for encoding and decoding
if fuction_type == "e":
  print(encrypt(msg,shift))
else:
  print(decrypt(msg,shift))