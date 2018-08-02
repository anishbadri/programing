import collections

def main(palin):
	s = collections.defaultdict(int)
	for char in palin:
		if char != " ":
			s[char] += 1 
	odd = 0
	for i in s:
		if s[i] %2 != 0:
			odd +=1
	return odd <= 1	






if __name__ == "__main__":
	print(main("malayala m"))
