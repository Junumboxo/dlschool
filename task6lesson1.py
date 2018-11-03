from collections import Counter

urls = ['./20_newsgroups/sci.space/62477',
        './20_newsgroups/sci.space/62478',
        './20_newsgroups/sci.space/62479',
        './20_newsgroups/sci.space/62480',
        './20_newsgroups/sci.space/62481',
        './20_newsgroups/sci.space/62614',
        './20_newsgroups/sci.space/62615',
        './20_newsgroups/sci.space/62616',
        './20_newsgroups/sci.space/62708',
        './20_newsgroups/sci.space/62709']
for url in urls:
  bag_of_words = Counter()
  file = open(url, mode = "r")
  for line in file:
    words = line.split(' ')
    for word in words:
      bag_of_words[word]+=1
  print(url.index(), bag_of_words)
  flie.close()
