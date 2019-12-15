from allllwords import positive_words, negative_words

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in punctuation_chars:
        if i in s:
            s = s.replace(i,'')
    return s

def get_pos(s):
    a = strip_punctuation(s)
    split_string = a.split(" ")
    count = 0
    for i in positive_words:
        if i in split_string:
            count += 1
    return count

def get_neg(s):
    a = strip_punctuation(s)
    split_string = a.split(" ")
    count = 0
    for i in negative_words:
        if i in split_string:
            count += 1
    return count


with open('twitter.csv') as filename:
    twitdat = filename.readlines()
    resulte = open('c.csv','w')
    resulte.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    resulte.write('\n')
    for i in twitdat[1:]:
        all_words = list(i.strip().split(","))

        positive = get_pos(all_words[0])
        negative = get_neg(all_words[0])
        net_score = positive - negative
        resulte.write("{}, {}, {}, {}, {}".format(all_words[1],all_words[2],positive,negative,net_score))
        resulte.write('\n')
    resulte.close()
