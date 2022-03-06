import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Ask again later'
    elif answerNumber == 5:
        return 'Concentrate and ask again'
    elif answerNumber == 6:
        return 'Reply hazy try again'
    elif answerNumber == 7:
        return 'Reply hazy try again'
    elif answerNumber == 8:
        return 'Not so good'
    elif answerNumber == 9:
        return 'YAY'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
