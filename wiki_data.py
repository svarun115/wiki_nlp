import wikipedia

def getpage(name):
	pg = wikipedia.page(name)
	print "getting page"
	with open("data/"+name+".txt","w") as f:
		f.write(pg.content.encode("ascii","ignore"))
	with open("data/union.txt","a") as f:
		f.write(pg.content.encode("ascii","ignore"))
	return pg.url,pg.title,pg.content

def get_data():
	with open("topics.txt","r") as f:
		topics = f.readlines();
		return topics

print "Collecting data from wikipedia for the given topics...\n"
topics = get_data()

for item in topics:
	url,title, content = getpage(item.strip())
	print "Url :"+ url +"\nTitle : "+title+"\n"