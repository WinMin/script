#str = "pgs{jro-fuv-lna-one}"
str =raw_input('put flag:')
new_str = ""
yi = 13
for i in str:
	if i>='a' and i<='z':
		i = ord(i)
		i = ((i-yi)-97)%26+97
		i = chr(i)
		new_str = new_str+i
		print(new_str)
