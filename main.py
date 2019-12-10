original_str = "The quick brown rhino jumped over the extremely lazy fox"
a = original_str.split()
num_words_list = []


for i in a:
    num_words_list.append(len(i))
print(num_words_list)
