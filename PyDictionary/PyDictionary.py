'''Import libraries Json and difflib'''
import json
from difflib import get_close_matches as gtcm

'''Building dictionary importing Json data'''
data = json.load(open("data.json"))

'''translate(word) is a method who find the word in the dictionary'''
def translate(word):
    word.lower() #Avoid case-sensitive
    if word in data: #Check if word is in data
        print(word.upper() + ':')
        return data[word] #Return the definition
    elif len(gtcm(word, data.keys())) > 0: #Check if there are similar word in data
        yn = input('Did you mean %s instead? Enter Y or N if no: ' % gtcm(word, data.keys())[0])
        if yn == 'Y':
            s = gtcm(word, data.keys())[0]
            print(s.upper() + ':')
            return data[gtcm(word, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "we didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."

while True:
    word = input('(Q for quit)\n' + 'Enter Word:\n')
    i = 0 #Set a counter as Index
    if word != 'Q': #Set a Break of Loop
        output = translate(word)
        if type(output) == list: #Check if the output is a list
            for item in output:
                i += 1
                print('[%s]'%i + item)#Stamp the output
        else:
            print(output)
    else:
        break
