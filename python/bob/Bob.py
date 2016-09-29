

def answer(question):
	flag = 0
	if len(question)>0:
		for i in range(len(question)):
			if question[i] == "!":
				flag = 1
				print "Woah, Chill out!"
				break
				
			elif question[i] == "?":
				flag = 1

				if i == len(question)-1:
					print "Sure"
					break
				elif question[i+1] == "!":

					print "Woah,Chill out!"
					break

				

				
					


				



		if flag == 0:
			print "Whatever"

	else:
		print "Fine, Be that way!"


			
	

prompt = ">"
print "Bob: Ask me a question \n"
question = raw_input(prompt)



answer(question)

   	