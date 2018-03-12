##### Making and Reading from Dictionaries

user = {
    'name': 'Victor',
    'age': '30',
    'country of birth': 'USA',
    'favorite language': 'Python' 
}

def user_info(dit):
    print 'My name is {}'.format(dit['name'])
    print 'My age is {}'.format(dit['age'])
    print 'My country of birth is {}'.format(dit['country of birth'])
    print 'My favorite language is {}'.format(dit['favorite language'])

user_info(user)