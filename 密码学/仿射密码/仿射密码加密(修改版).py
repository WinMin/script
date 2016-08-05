plain_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(plaintext):
	'ENCRYPT FUNCTION,PARAMETER:PLAINTEXT,RETURN:CIPHERTEXT'
	cipher_array=[0 for i in range (len(plaintext))] #init the array
	plainlist=list(plaintext)
	#print plainlist #debug
	j=0
	for item in plainlist:
		for i in range(len(plain_char)):
			if item==plain_char[i]:
				index=(11*i+8)%26
				cipher_array[j]=cipher_char[index]
				j=j+1
	ciphertext=''.join(cipher_array)
	return ciphertext

def decrypt(ciphertext):
	'DECRYPT FUNCTION,PARAMETER:CIPHERTEXT,RETURN:PLAINTEXT'
	plain_array=[0 for i in range (len(ciphertext))] #init the array
	cipherlist=list(ciphertext)
	#print cipherlist #debug
	j=0
	for item in cipherlist:
		for i in range(len(cipher_char)):
			if item==cipher_char[i]:
				index=(15*i-19)%26
				plain_array[j]=plain_char[index]
				j=j+1
	plaintext=''.join(plain_array)
	return plaintext

def main():
	'MAIN FUNCTION'
	string=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	z=0
	for z in range(0,26):
		plaintext=string[z]
		ciphertext=encrypt(plaintext)
		print z,ciphertext
		z=z+1
	
if __name__=="__main__":
	main()


