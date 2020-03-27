from numpy import array # We're going to use it for changing from list's type to array's type
letters = ['A','B','C','D','E','F','G',
           'H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']


def encryption(key):
    assert(type(key) == int), ('The key should be an integer number!')
    try:
        print('Encryption...')
        print("Please enter the string for encrypt it: \n")
        word = str(input('>>> ')) #WAITING AN INPUT FROM THE USER
        word_list = [] # We'll need this empty list
        for letter in word:
          #print(letters.index(letter))
          word_list.append(letters.index(letter))
        word_list = array(word_list) # As i said we'll need to transfer it to array's type
        encyptedWordList = (word_list + key) % 26 # The equation
        for item in encyptedWordList:
            print(letters[item])
    except AssertionError as e:
        print(e)

def decryption(key):
    assert(type(key) == int), ('The key should be an integer number!')
    try:
        print('Decryption...')
        print("Please enter the string for decrypt it: \n")
        word = str(input('>>> '))
        word_list = []
        for letter in word:
          #print(letters.index(letter))
          word_list.append(letters.index(letter))
        word_list = array(word_list)
        decyptedWordList = (word_list - key) % 26
        for item in decyptedWordList:
            print(letters[item])

    except AssertionError as e:
        print(e)

def main():
    print("===============================================")
    print("Hi there please selecte the following choices: ")
    print("1 - for encryption")
    print("2 - for decryption")
    print("3 - for exit: ")
    slct = int(input('>>> '))
    if slct == 1:
        mykey = int(input('Please enter the key >>> '))
        encryption(mykey)
        main()
    elif slct == 2:
        mykey = int(input('Please enter the key >>> '))
        decryption(mykey)
        main()
    elif slct == 3:
        exit()
    else:
        print('try again please!')
        main()

if __name__ == '__main__':
    main()


