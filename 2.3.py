
import re

def WordCounter(string):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    hits = [
        (alphabet[i], string.count(alphabet[i]))
        for i in range(len(alphabet))
        if string.count(alphabet[i])
    ]

    for letter, frequency in hits:
        print (letter, frequency)

    count = len(re.findall(r'\w+', line))
    print ("Word Count: " + str(count))
    letters = sum(a.isalpha() for a in line)
    print("Letter Count: " + str(letters))

if __name__ == '__main__':
    line = input()
    WordCounter(line)

