import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk.corpus
from nltk.text import Text 
import re
import PyPDF2
import random

def stephen(question):

	#text = input("Please enter your question: ")
	text = question

	pages = ['']
	file = open('hawking.pdf', 'rb')
	read_pdf = PyPDF2.PdfFileReader(file)
	n_of_pages = read_pdf.getNumPages()

	for page_n in range(n_of_pages):
		page = read_pdf.getPage(page_n)
		content= page.extractText()
		final_content, del1, del2 = content.partition('file:///C|/')
		pages.append(final_content)

	book = '/n'.join(pages)

	texta = nltk.Text(nltk.word_tokenize(book))

	tokenized = word_tokenize(text)
	tagged = nltk.pos_tag(tokenized)

	grammar = "NP: {<W.*><VB.*><.*>*}"

	cp = nltk.RegexpParser(grammar)
	result = cp.parse(tagged)

	alo = result.pos()

	if alo[len(alo)-1][0][0] == '?':
		alo = alo[:-1]

	i=0
	keyword=[]

	for word in alo:
		if word[1] == 'NP':
			j=i+2;
			while alo[j][1] == 'NP':
				keyword.append(alo[j][0][0])
				if j+1 < len(alo):
					j=j+1
				else:
					break

			keyword.append(alo[i+1][0][0])
			break
		i = i+1

	print(keyword)

	y=0
	index=0
	posa=[]

	for word in texta:
		if word == keyword[0]:
			z=1
			if texta[index+1] == keyword[z]:
				while texta[index+z] == keyword[z]:
					#print(keyword[z])

					if z+1 < len(keyword):
						z=z+1
					else:
						posa.append(index)
						y=y+1
						z=1
						break
		index=index+1

	if y == 0:
		return ""

	oNumber = posa[random.randrange(len(posa))-1]

	y=0
	index=0
	oAnswer=''

	oAnswer=texta[oNumber-20:oNumber+100]

	fanswer = ' '.join(oAnswer)


	#print(fanswer)
	return fanswer