from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.lancaster import LancasterStemmer
import operator
import pickle
import numpy as np
import re

def derive_vocabulary(filename,stem = True):
	stemmed = []
	with open(filename,"r") as f:
		text = f.read()
		re_tokenizer = RegexpTokenizer('\w+')
		words = re_tokenizer.tokenize(text)
		st = LancasterStemmer()
		if(stem):
			for i in words:
				stemmed.append(st.stem(i.lower()))
		else:
			for i in words:
				stemmed.append(i.lower())

	print "Total number of words : {}".format(len(stemmed))
	with open('vocabulary.pkl', 'wb') as output:
		pickle.dump(stemmed, output, pickle.HIGHEST_PROTOCOL)



def get_unigram(filename):
	words = []
	with open(filename, 'rb') as input:
		words = pickle.load(input)
   	unigram = {}
   	for item in words:
   		if item not in unigram:
   			unigram[item] = 1
   		else:
   			unigram[item] += 1
   	for key in unigram:
   		unigram[key] = float(unigram[key])/len(words)
   	with open('unigram.pkl', 'wb') as output:
		pickle.dump(unigram, output, pickle.HIGHEST_PROTOCOL)
   	




def get_sentences(filename,size=4,stem=True):
	sentences = []
	with open('data/union.txt', 'r') as f:
		text = f.read()
		text = re.sub(r'(M\w{1,2})\.', r'\1', text)
		# sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
		sentences = sent_tokenize(text)
	# print sentences
	data = []
	for sentence in sentences:
		sent = []
		re_tokenizer = RegexpTokenizer('\w+')
		words = re_tokenizer.tokenize(sentence)
		st = LancasterStemmer()
		for i in words:
			if stem:
				sent.append(st.stem(i.lower()))
			else:
				sent.append(i.lower())

		if len(sent)<size:
			w = sent
			while len(w)<size:
				w.append('__PAD__')
			data.append(w)
		else:
			j=0
			while (j+size)<len(sent):
				w=[]
				k=0
				while k<size:
					w.append(sent[j+k])
					k+=1
				data.append(w)
				j+=k
			if j%size != 0:
				w=sent[j:]
				while len(w)<size:
					w.append('__PAD__')
				data.append(w)

	print "Number of sentence contexts : {}".format(len(data))
	with open('sentences.pkl', 'wb') as output:
		pickle.dump(sentences, output, pickle.HIGHEST_PROTOCOL)


derive_vocabulary("data/union.txt",True)
get_unigram("vocabulary.pkl")
get_sentences("union.txt",stem=True)
