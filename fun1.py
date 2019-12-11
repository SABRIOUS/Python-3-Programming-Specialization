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

new_file = open("squares.txt","r")
print(new_file.read())

new_file.close()
