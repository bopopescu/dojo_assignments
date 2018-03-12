#### Compare List

def compare_list(l1,l2):
    if len(l1) == len(l2):
        counter = 0
        for i in range (0,len(l1)):
            if l1[i] == l2[i]:
                counter += 1
            else:
                print 'The list are not the same'
                break 
        if counter == len(l1):
            print 'The lists are the same'
    else: 
        print 'The list are not the same'
compare_list([1,2,5,6,2],[1,2,5,6,2])
compare_list([1,2,5,6,5],[1,2,5,6,5,3])
compare_list([1,2,5,6,5,16],[1,2,5,6,5])
compare_list(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])