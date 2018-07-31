import collections 

def firstmain(string1, string2):
	p = collections.defaultdict(int)
	for char in string1:
		p[char] += 1


	for char in string2:
		p[char] -= 1
	
	return (not any(p.values()))	





if __name__ == "__main__":
	print(firstmain("aanish","hsinaa"))







 
