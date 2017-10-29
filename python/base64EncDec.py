import base64
original_string = 'This is the data, in the clear.'
print('Original:', original_string)
enc_bytes  = base64.b64encode(original_string.encode("utf-8"))
print( 'Encoded :', enc_bytes.decode("utf-8") )
decoded_bytes = base64.b64decode(enc_bytes)
print( 'Decoded :', decoded_bytes.decode("utf-8"))