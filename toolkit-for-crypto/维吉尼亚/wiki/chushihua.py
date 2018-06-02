from string import letters
def chushihua():
	pass
	msg=open("./sec.txt")
	final=""
	for each in msg:
		for each_char in each:
			if each_char in letters:
				final+=each_char.lower()
		final+="\n"
	msg.close()
	poi=open("./chushihua.txt","w")
	poi.writelines(final)
	poi.close()