# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file
# named project_twitter_data.csv which has the text of a tweet, the number
# of retweets of that tweet, and the number of replies to that tweet.
# We have also provided lists of words that are considered positive (positive_words)
# and words that are considered negative (negative_words). You may want to read in the
# file and print out the first few lines to see what the data looks like.
# Your task is to build a sentiment classifier, which will detect how positive or
# negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. Upload the csv file to Excel or Google Sheets,
# and produce a graph of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter,
# a string which represents a word, and removes characters considered punctuation
# from any position in a word.

from allllwords import positive_words, negative_words

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in punctuation_chars:
        if i in s:
            s = s.replace(i,'')
    return s
# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurances there are of positive words in the text.

def get_pos(s):
    a = strip_punctuation(s)
    split_string = a.split(" ")
    count = 0
    for i in positive_words:
        if i in split_string:
            count += 1
    return count
# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurances there are of negative words in the text.

def get_neg(s):
    a = strip_punctuation(s)
    split_string = a.split(" ")
    count = 0
    for i in negative_words:
        if i in split_string:
            count += 1
    return count
# Finally, copy in your previous functions and write code that opens
# the file project_twitter_data.csv which has
# the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies,
#Positive Score (which is how many happy words are in the tweet),
# Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check coursera for this portion of the assignment once you’re done!


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
