
def rna(dna):
	cond = 0
	rna = []
	dna = list(dna)
	
	for i in range(len(dna)):
			
		if dna[i] == "G":
			
			rna.append("C")
		elif dna[i] == "C":
			
			rna.append("G")
		elif dna[i] == "T":
			
			rna.append("A")
		elif dna[i] == "A":
			
			rna.append("U")
		else:
			cond = 1
			print "Invalid DNA code"
			break

	if cond != 1:
		print "RNA Transcription of DNA strand is:",rna
		

prompt = ">"

print "Enter a DNA strand \n"

DNA = raw_input(prompt)

rna(DNA)