

def main(word):
	asciiArray = [0] * 256
	print(asciiArray)
	length = len(word)
	for char in word:
		print(char)
		asciiArray[ord(char)] += 1
	for ints in asciiArray:
		if ints > 1:
			return False
	return True 
		
		
def secondmain(word):
	for ipos,ichar  in enumerate(word):
		for jpos, jchar in enumerate(word):
			if ipos != jpos and ichar == jchar :
				return False
	return True
				 



if __name__ == "__main__":
	print(secondmain("Anissh"))
