#### Scores and Goals


print "Scores and Grades"
def scores_and_grades():
    import random
    random_num = random.randint(60,100)
    for i in range(0,10):
        import random
        random_num = random.randint(60,100)
        random_num 
        grade = ''
        if random_num > 89:
            grade += 'A'
        if random_num <90 and random_num >79:
            grade += 'B'
        if random_num <80 and random_num >69:
            grade += 'C'
        if random_num <70 and random_num >59:
            grade += 'D'
        print 'Score: {}; Your grade is {}'.format(random_num,grade)
scores_and_grades()
print 'End of the program. BYE!'