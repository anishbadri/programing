


def firstmain(string, length):
	actualLength = len(string)
	string = string[:length].replace(" ","%20")
	return string	


'''


position = actualLength-1
	print(position)
	while(position>0):
		length -= 1
		string[position] = string[length]
		print(string[position])
		position -= 1
	print(string)
		 
'''	








if __name__ == "__main__":
	print(firstmain("Mr John Smith    ",13))
