import sys

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # There's no list in Python containing only the spanish alphabet, so we have to create a string with all the spanish characters
message = str(input("Type a message to encode: "))
message = message.replace(' ', '').upper()	 # This stores the input message altogether (upper case)
original_key = str(input("Type a keyword: "))
original_key = original_key.replace(' ', '').upper()  # This stores the key altogether and also in upper case
key = ''
cipher = ''
decrypt = ''

if len(message) > len(original_key):	# If the lenght of the message is longer than the original key...
	for i in range(int(len(message) / len(original_key))):	# The key gets longer until the message is the same lenght
		key += original_key
	key += original_key[:len(message) % len(original_key)]

elif len(message) < len(original_key):	# If the lenght of the message is shorter than the lenght of the original key...
	key = original_key[:len(message)]	# Same process but this time the key gets shorter

elif len(message) == len(original_key):	 # If both are the same lenght...
	key = original_key	# The key is stored here

else:
	print('Unexpected error. Ending program')
	sys.exit(1)


print('Original message: ' + message)
print('Keyword: ' + original_key)
print()


print('Encrypting...')
for i in range(len(message)):
	x = abc.find(message[i])	# The position of the character is stored after being found in the dictionary
	y = abc.find(key[i])	# Same process with the key
	sum = x + y	 # We calculate the sum of both positions
	module = sum % len(abc)	 # We calculate the modulus of the sum divided by the lenght of the abecedary
	cipher += abc[module]	# We sum that to the cipher variable

print('Encrypted message: ' + cipher)
print()


print('Decrypting...')
for i in range(len(cipher)):
	x = abc.find(cipher[i])
	y = abc.find(key[i])
	minus = x - y
	module = minus % len(abc)
	decrypt += abc[module]

print('Decrypted message: ' + decrypt)

sys.exit(0)
