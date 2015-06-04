import pickle
import operator
import numpy as np

def get_vocab(v_size):
	with open("unigram.pkl", 'rb') as input:
		unigram = pickle.load(input)
	print "Actual vocabulary size : {}".format(len(unigram))
	print "Selected vocabulary size : {}".format(v_size)
	sorted_uni = list(reversed(sorted(unigram.items(), key=operator.itemgetter(1))))
	nvocab = [sorted_uni[i][0] for i in range(v_size)]
	return nvocab


def get_lookup(words,dimension=2):
	lookup = {}
	count = 2
	for item in words:
		if item not in lookup:
			lookup[item] = []
			lookup[item].append(count)
			val = []
			for i in range(dimension):
				val.append(np.random.uniform(-1,1))
			lookup[item].append(val)
			count += 1

	lookup['__UNK__'] = []
	lookup['__UNK__'].append(0)
	val = []
	for i in range(dimension):
		val.append(np.random.uniform(-1,1))
	lookup['__UNK__'].append(val)

	lookup['__PAD__'] = []
	lookup['__PAD__'].append(1)
	val = []
	for i in range(dimension):
		val.append(np.random.uniform(-1,1))
	lookup['__PAD__'].append(val)
	return lookup


nvocab = get_vocab(10)
nlookup = get_lookup(nvocab)
