#  1. You will be sorting the following list by each element’s second letter a to z.
# Create a function to use when sorting that takes a string as input and return the second letter
# of that string and name it second_let. Create a variable called func_sort and assign
# the sorted list to it. Do not use lambda.

# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
#
# def second_let(s):
#     return s[1]
# func_sort = sorted(ex_lst,key = second_let)

# ________________________________________

# 2. Below, we have provided a list of strings called nums. Write a function called last_char
# that takes a string as input, and returns only its last character.
# Use this function to sort the list nums by the last digit of each number,
# from highest to lowest, and save this as a new list called nums_sorted.

# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
#
# def last_char(s):
#     return s[-1]
#
# nums_sorted = sorted(nums,key = last_char, reverse = True)

# ________________________________________


# 3. Once again, sort the list nums based on the last digit of each number from
# highest to lowest. However, now you should do so by writing a lambda function.
# Save the new list as nums_sorted_lambda.

# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
# a = lambda x: x[-1]
# nums_sorted_lambda = sorted(nums,key = a,reverse = True)

# ________________________________________

# GOoD Example

# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
#
# y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
# for k in y:
#     print("{} appears {} times".format(k, d[k]))
#_____________________________________

# Another Way
#
#
# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# d = {}
# for x in L:
#     if x in d:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
#
# def g(k):
#     return d[k]
#
# y =(sorted(d.keys(), key=g, reverse = True))
#
# # now loop through the keys
# for k in y:
#     print("{} appears {} times".format(k, d[k]))


# ___________________________

# 2. Sort the following dictionary based on the keys so that they are sorted a to z.
# Assign the resulting value to the variable sorted_keys.

# dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
#
# sorted_keys = sorted(dictionary.keys())

# ___________________________
# 4. Sort the following dictionary’s keys based on the value from highest to lowest.
# Assign the resulting value to the variable sorted_values.

# dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
#def a(s):
    #return dictionary[s]
# sorted_values = sorted(dictionary.keys(),key=lambda k: dictionary[k], reverse=True)
# sorted_values = sorted(dictionary.keys(),key=a, reverse=True)
# ___________________________
# fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
# new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
# for fruit in new_order:
#     print(fruit)

# ___________________________

# weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
#            'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
#            'Cairo': {'temp': 96, 'condition': 'sunny'},
#            'Berlin': {'temp': 89 'condition': 'sunny'},
#            'Caloocan': {'temp': 78 'condition': 'sunny'}}
#
# sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
# answer :A. first country name (alphabetically), then temperature (lowest to highest)
# __________________________
# Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# def a(s):
#     return medals[s]
# top_three = sorted(medals.keys(), key =lambda i: medals[i], reverse = True)[:3]
# top_three = sorted(medals.keys(), key =a, reverse = True)[:3]
# print(top_three)

# ______________________
# We have provided the dictionary groceries. You should return a list of its keys,
# but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.

# groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
#
# most_needed = sorted(groceries.keys(), key =lambda i: groceries[i], reverse = True)
# print(most_needed)
# ______________________
# **********GooD**********
# Create a function called last_four that takes in an ID number and returns the last four digits.
# For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint:
# Remember that only strings can be indexed, so conversions may be needed.
#
# def last_four(x):
#     a = str(x)
#     return a[4:]
#
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_ids = sorted(ids,key = last_four)
# ______________________
# Sort the list ids by the last four digits of each id.
# Do this using lambda and not using a defined function.
# Save this sorted list in the variable sorted_id.
#
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
#
# sorted_id = sorted(ids,key = lambda x: str(x)[4:])
# ______________________
# Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
#
# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
# lambda_sort = sorted(ex_lst, key = lambda x: x[1])
_______________________
