# Test_problem
# olypmicsfile = open("olypmics.txt","r")
# for aline in olypmicsfile.readlines():
#     values = aline.split(",")
#     Name,Sex,Age,Team,Event,Medal = values
#     print(Name, "is from", Team, "and is on the roster for", Event)
#
# olypmicsfile.close()

# __________________________

# create_file = open("squares.txt","w")
# for number in range(13):
#     square = number * number
#     create_file.write(str(square) + "\n")
#     # create_file.write("\n")
# create_file.close()

# __________________________

# new_file = open("squares.txt","r")
# print(new_file.read())
#
# new_file.close()

# _________________________

# olympians = [("John Aalberg", 31, "Cross Country Skiing"),
#             ("Minna Maarit Aalto", 30, "Sailing"),
#             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
#             ("Wakako Abe", 18, "Cycling")]
#
#
# header_row = "Name,Age,Sport"
# print(header_row)
#
# for olymp in olympians:
#     row_string = "{},{},{}".format(olymp[0],olymp[1],olymp[2])
#     print(row_string)
#
#
#
# olympians = [("John Aalberg", 31, "Cross Country Skiing"),
#             ("Minna Maarit Aalto", 30, "Sailing"),
#             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
#             ("Wakako Abe", 18, "Cycling")]


# ________________________

# outfile = open("reduced_olympics.csv","w")
# # output the header row
# outfile.write('Name,Age,Sport')
# outfile.write('\n')
# # output each of the rows:
# for olympian in olympians:
#     row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
#     outfile.write(row_string)
#     outfile.write('\n')
# outfile.close()
# _______________________________

# ______________________________
# _______________________________

# ______________________________
# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
#
# get_file = open("school_prompt.txt","r")
# a = get_file.read()
# beginning_chars = a[:30]

# _______________________________
# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
# get_file = open("school_prompt.txt","r")
# a = get_file.readlines()
# three =[]
# for i in a:
#     three.append((i.split()[2]))
# ______________________________# _______________________________
# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
# get_file = open("emotion_words.txt","r")
# a = get_file.readlines()
# emotions  =[]
# for i in a:
#     emotions .append((i.split()[0]))

# ______________________________

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
# get_file = open("travel_plans.txt","r")
# a = get_file.read()
# first_chars  = a[:33]
#

# _______________________

# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
# get_file = open("school_prompt.txt","r")
# a = get_file.read().split()
# p_words = []
# for i in a:
#     if "p" in i:
#         p_words.append(i)
