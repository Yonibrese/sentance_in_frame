#frame
string = input("enter a sentance ")
sentance = string.split(" ")
longest = len(max(sentance))
top = ("*"*(longest+4))
print(top+"**")
for word in sentance:
	newWord = word.center(len(top), " ")
	line = ("*"+newWord+"*").center(len(top))
	print(line)
print(top+"**")
