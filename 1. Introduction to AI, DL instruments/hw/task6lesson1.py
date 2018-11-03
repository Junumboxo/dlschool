import glob
from collections import Counter

urls = glob.glob('./20_newsgroups/sci.space/*')
for url in urls:
    bag_of_words = Counter()
    file = open(url, mode = "r")
    for line in file:
        words = line.split(' ')
        for word in words:
            bag_of_words[word]+=1
    print(urls.index(url), bag_of_words)
    flie.close()
