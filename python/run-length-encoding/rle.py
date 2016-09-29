def rle(code):
	


	code = list(code)
	answer = []
	
	
	flag = 0
    

	out = ""
	
	

	
	for i in range(1,len(code)):
		
		
		if flag == 0:
			search = code[0]
			
			code = code[1:len(code)]
			
		count = 1
		flag = 0


		for j in range(len(code)):
			
			if search == code[j]:
				count += 1
				j += 1
			else:
				break


		



		






		answer.append(count)

		answer.append(search)

		

		if len(code) == 0:
			answer.pop()
			answer.pop()


		if count > 1 and len(code) > count:
			flag = 1
			search = code[count - 1]
			
			code = code[count:len(code)]
			
		elif count > 1 and len(code) < count:
			break
		elif count == len(code):
			break





		

		
		
			



    
	for i in range(len(answer)):
		if i%2 == 0:
			out += str(answer[i]) 
		else:
			out += str(answer[i]) + " "

		

	print out 


			
		

prompt = ">"

print "Enter code for run length encoding \n"

m = raw_input(prompt)
m = m + " "


rle(m)
































			
		



		
		

		
	


		
		
	   