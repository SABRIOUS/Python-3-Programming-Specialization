lisq = [1,2,3,4,5,6]
# MAP ***
# map takes two parameter function and list
# new_list_map = list(map(lambda value: value**2, lisq))
#
# print(new_list_map)
# >>>>[1, 4, 9, 16, 25, 36]

# FILTER ****

# filter takes two parameter function and list but return based on condition
# new_seq = list(filter(lambda i: i % 2==0,lisq))
# >>>>[2, 4, 6]

# zip ***
# compine two list
# l1 = [1,2,3]
# l2 = [4,5,6]
# a = list(zip(l1,l2))
# l3 = []
# for (i,j) in a:
#     l3.append(i+j)
#
# newlisq = [i + j for (i,j) in list(zip(l1,l2)) ]
# L3 = [i + j for (i,j) in list(zip(L1,L2))if i > 10 and j < 5]

# list comprehension is the best one ************
# a =  [i[0] for i in students if i[1] >= 70] map and filter together


# *********** another example ********
# l1 = ['left', 'up', 'front']
# l2 = ['right', 'down', 'back']
#
# first  = list(zip(l1,l2))
# opposites  = list(filter(lambda i: len(i[0])>3 and len(i[1]),first))

# *********good example **********
# # species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
# #
# # population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
# #
# # pop_info = list(zip(species,population))
# #
# # endangered = [i[0] for i in pop_info if i[1] < 2500]
