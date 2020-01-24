'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    """
    Recursive function to count the number of times 'th' appears in a string
    """

    # if word is less than 2 letters long, return 0
    if len(word) < 2:
        return 0

    # Initialize th
    # th = 1 if the first two letters are 'th' otherwise 0
    th = int(word[0:2] == 'th')

    # if word is exactly 2 letters long, return th
    if len(word)==2:
            return th
    # otherwise keep track of the current value of th and
    # move to the right 1 letter in the word
    else:
        return th + count_th(word[1:])

