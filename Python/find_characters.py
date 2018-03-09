#### Find Characters

def find_characters(l,char):
    new_list = []
    for i in range(0,len(l)):
        for j in l[i]:
            if j == char:
                new_list.append(l[i])
    print new_list
find_characters(['hello','world','my','name','is','Anna'],'o')

