import string

string.printable = string.printable[10:62]

lower = list(string.printable[:26])
upper = list(string.printable[26:52])


def pangram(word):
	for i in range(len(word)):
		for letter in zip(lower[:],upper[:]):
			if letter[0] == word[i] or letter[1] == word[i]:
				lower.remove(letter[0])       		
				upper.remove(letter[1])
				
				

	if lower == [] or upper == []:
		print " Sentence is a pangram"
	else:
		print "Sentence is not a  pangram"




word = raw_input("Enter a sentence")

pangram(word)











	



	  	















