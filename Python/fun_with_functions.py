#### Fun with Functions

### Odd/Even
def odd_even():
    for i in range (1,2001):
        if i%2 == 0:
            print 'number is {}.   This is a even number'.format(i)
        else:
            print 'number is {}.   This is a odd number'.format(i)
odd_even()

### Multiply
a = [2,4,10,16]
def multiply(lis,val):
    # print "you are now in function"
    for i in range(len(lis)):
        # print 'you are now in for loop'
        # print i
        lis[i] *= val
        # print lis
    return lis
b = multiply(a, 5)
print b

### Hacker Challenge
def layered_multiples(lis):         
    # print 'you are now in function'
    newLis=[]
    for i in range(len(lis)):                       #itirate thru list
        # print 'you are now in 1st for loop'
        new_inner_list = []
        for j in range(0,lis[i]):                   #going thru value of lis[i] 1 by 1
            # print 'you are now in 2nd for loop'
            new_inner_list.append(1)                    #appending 1 every integer of value 
        newLis.append(new_inner_list)
    return newLis
x = layered_multiples(multiply([2,4,5],3))
print x



