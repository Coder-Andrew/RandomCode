'''
A simple Caesar Cypher that I made using modulus, ascii values and
elementary python knowledge
'''

import sys

def cypher(string, key):
    temp = ''

    for i in range(len(string)):
        j = i % len(key)

        temp += chr((ord(string[i]) + ord(key[j])) % 93 + 33)

    return temp

def decypher(string, key):
    temp = ''

    for i in range(len(string)):
        j = i % len(key)

        char_dif = ord(string[i]) - ord(key[j])

        while not (32 <= (char_dif - 33) <= 60) and (char_dif <= 93):

            char_dif += 93
        
        char =  chr(char_dif - 33)

        temp += char

    return temp


if __name__ == '__main__':
    if (('-d' not in sys.argv) and ('-e' not in sys.argv)) or ('-k' not in sys.argv):
        print('Usage:\t-d|-e "msg" -k key\n\n\t-d: decrypt message\n\tmsg: message to decrypt/encrypt\n\t-k: key to use to encrypt/decrypt\n\tkey: key to encrypt/decrypt by')

    elif sys.argv[1] == '-d':
        msg = ' '.join(sys.argv[(sys.argv.index('-d'))+1:sys.argv.index('-k')])
        key = ' '.join(sys.argv[(sys.argv.index('-k'))+1:])

        print(decypher(msg, key))        

    elif sys.argv[1] == '-e':
        msg = ' '.join(sys.argv[(sys.argv.index('-e'))+1:sys.argv.index('-k')])
        key = ' '.join(sys.argv[(sys.argv.index('-k'))+1:])

        print(cypher(msg, key)) 
