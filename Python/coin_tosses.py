#### Coin Tosses

 

def coin_toss():
    head_count = 0
    tail_count = 0
    for i in range (1,5001):
        import random
        random_num = random.randint(1,2)
        coin = ''
        if random_num == 2:
            coin += 'heads'
            head_count += 1
        else:
            coin += 'tails'
            tail_count += 1
        print 'Attempt #{}:  Throwing coin... It\'s {}! ... Got {} head(s) so far and {} tail(s) so far'.format(i, coin, head_count, tail_count)
coin_toss()    
    
