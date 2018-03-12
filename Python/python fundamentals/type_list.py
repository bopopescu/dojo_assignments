#### Type List
li = ['magical unicorns',19,'hello',98.98,'world']
li2 = [2,3,1,7,4,12]
li3 = ['magical','unicorns']

def type_list(l):
    newStr = ''
    sum = 0
    for i in range (0,len(l)):
        if type(l[i]) == str:
            newStr += ' '+l[i]
        elif type(l[i]) == int or float:
            sum += l[i]   
    print "sum:" + str(sum)
    print "string:" + str(newStr)
    if len(newStr) == 0:
        print 'The list you entered is of number type'
    if sum == 0:
        print 'The list you entered is of string type'
    if len(newStr) > 0 and sum > 0:
        print 'The list you entered is of mixed type'
type_list(li)  
type_list(li2)
type_list(li3)  



