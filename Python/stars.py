##### Stars

### Part 1

li=[4,6,1,3,5,7,25]

def draw_stars(lis):
    for i in range(len(lis)):
        x = lis[i]
        stars = ''
        for j in range(0,x):
            stars += '*'
        print stars
draw_stars(li)

print "end of part 1"

### Part 2

print "Part 2"

li2=[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(lis):
    for i in range(len(lis)):
        if type(lis[i]) == int:
            x = lis[i]
            stars = ''
            for j in range(0,x):
                stars += '*'
            print stars
        else:
            x = len(lis[i])
            letters = ''
            for j in range(0,x):
                letters += lis[i][0].lower()
            print letters
draw_stars(li2)


