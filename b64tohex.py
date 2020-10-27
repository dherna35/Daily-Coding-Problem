# Convert input string from base64 to hexadecimal
# Use 3q2+7w== shoud output deadbeef

import base64
import binascii
val = input("input a Base64 string:")
valHex = binascii.hexlify(base64.b64decode(val))
print(valHex.decode('utf-8'))