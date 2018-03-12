# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')
print words.replace(" day",' month')

# Min and Max
x = [2,54,-2,7,12,98]
print min(x), max(x)

# First and Last
y = ['hello',2,54,-2,7,12,98,'world']
newY =[]
newY.append(y[0])
newY.append(y[len(y)-1])
print newY

# New List
i = [19,2,54,-2,7,12,98,32,10,-3,6]
i.sort()
firstHalf = i[:5]
newI = i[5:]
newI.insert(0,firstHalf)
print newI
