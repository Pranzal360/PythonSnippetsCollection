# have a python dicionary that has a key/value pair that represents a word and it's definition
# collect input from the use, input is a word 
# check if the word is in dictinoary 
# print the definition 

def main():
    word_dict = {
        'hi' : ' a way of greeting',
        'eyes' : 'an organ for seeing',
        'earth' : 'a planet in space where we live'
    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dict:
            print(word, ":", word_dict[word])

main()