'''
Write a function which takes a sentence and returns the number of four letter words it contains. Don't worry about handling punctuation.
'''


def four_letter_words(sentence):

    count = 0
    list = sentence.split(' ')
    for str in list:
        if(len(str) == 4):
            count += 1

    return count