# def triple(value):
#     return 3*value
#
# def triplestuff(a_list):
#     new_list = list(map(lambda value: 4*value, a_list))
#     return new_list
#
#
# things = [3,6,8]
#
# things3 = triplestuff(things)
#
# print(things3)
# abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
# def dupple(a_list):
#     new_list = map(lambda a: a.upper(),a_list)
#     return new_list

# def upper2(word):
#     return word.upper()
#
# a = list(map(upper2,abbrevs))
# print(a)

# def keep_even(nums):
#     new_seq = filter(lambda i: i % 2==0,nums)
#     return list(new_seq)
#
# print(keep_even([1,2,3,4,5,6,7]))

# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
#
# filter_testing  = filter(lambda st: "w" in st,lst_check)
# alist = [4,2,8,6,5]
# because 5 is odd before doubled it
# blist = [num*2 for num in alist if num%2==1]
# import json
# tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
#
# a = tester['info']
# #print(json.dumps((a), indent = 2))
# compri = [d['name'] for d in a]
# l1 = [1,2,3]
# l2 = [4,5,6]
# a = list(zip(l1,l2))
# l3 = []
# for (i,j) in a:
#     l3.append(i+j)
#
# newlisq = [i + j for (i,j) in list(zip(l1,l2)) ]
# print(newlisq)

# _____________________________

# New Problem **********
# Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension,
# create a new list, L3, that sums the two numbers
# if the number from L1 is greater than 10 and the number from L2 is less than 5.
# This can be accomplished in one line of code.
#
# L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
# L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
# L3 = [i + j for (i,j) in list(zip(L1,L2))if i > 10 and j < 5]

# *************************
# Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.

# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
# map_testing  = list(map(lambda st: "Fruit: "+ st, lst_check))
# print(map_testing)
# *************************
# Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.

# countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
# b_countries  = list(filter(lambda st: st[0] =="B",countries))
# print(b_countries)
# *************************
# Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.

# people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
#
# first_names = [i[1] for i in people]
# *************************
# Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
#
# lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
# lst2 = [i * 2 for i in lst]
# *************************

# Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
#
# students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
#
# passed  = [i[0] for i in students if i[1] >= 70]
# *************************
# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.

# l1 = ['left', 'up', 'front']
# l2 = ['right', 'down', 'back']
#
# first  = list(zip(l1,l2))
# opposites  = list(filter(lambda i: len(i[0])>3 and len(i[1]),first))

# *************************
# Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.

# species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
#
# population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
#
# pop_info = list(zip(species,population))
#
# endangered = [i[0] for i in pop_info if i[1] < 2500]
