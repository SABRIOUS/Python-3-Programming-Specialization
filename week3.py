# rainfall_mi is a string that contains the average number of inches of rainfall in Michigan
# for every month (in inches) with every month separated by a comma
# Write code to compute the number of months that have more than 3 inches of rainfall.
# Store the result in the variable num_rainy_months. In other words,
# count the number of items with values > 3.0.
# ________________________
# problem "1"
# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# a = rainfall_mi.split(",")
# new_list = []
# num_rainy_months  = 0
#
# for num in a:
#     if float(num) > 3:
#         num_rainy_months += 1
#
# print(num_rainy_months)

# _______________________________

# problem "2"
# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
#
# # Write your code here.
# same_letter_count = 0
# new_list = sentence.split(" ")
#
# for word in new_list:
#     if word[0] == word[-1]:
#         same_letter_count += 1


# _______________________________
# problem "3"

# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
# acc_num = 0
#
# for word in items:
#     if "w" in word:
#         acc_num += 1

# _______________________________

# problem "4"

# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
# new_list = sentence.split(" ")
#
# num_a_or_e = 0
#
# for word in new_list:
#     if "a" in word or "e" in word:
#         num_a_or_e += 1
# _______________________________

# problem "5"

# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# vowels = ['a','e','i','o','u']
#
# # Write your code here.
# num_vowels = 0
# for i in s:
#     if i in vowels:
#         num_vowels += 1
# ______________________
