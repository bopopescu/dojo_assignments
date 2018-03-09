##### Names

### Part 1

# students = [
#      {'first_name': 'Michael', 'last_name' : 'Jordan'},
#      {'first_name': 'John', 'last_name' : 'Rosales'},
#      {'first_name': 'Mark', 'last_name' : 'Guillen'},
#      {'first_name': 'KB', 'last_name' : 'Tonel'}
# ]

# def names(lit):
#     for i in range (0,len(lit)):
#         print lit[i]['first_name'] +' '+ lit[i]['last_name']
        
# names(students)

### Part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def name_num(dit):
    for user_group,user_data in dit.items():
        print dit.items()
        print user_group
        for item in user_data:
            name = item['first_name'] + ' ' + item['last_name']
            print '{} - {} - {}'.format(
                user_data.index(item)+1, name, len(name)-1) 
name_num(users)


