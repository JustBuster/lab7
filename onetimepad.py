'''
Hidden Key: # # # _ # # # S # # # N # # # U # #

table = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','!']
'''

from rsa import encrypt



table = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','!']

text = 'NMWSHAQBV_DRTNJ'

key = 'THE_QUESTIONS_RUN'
key = [i for i in key]

def coder(table, key, text):
    key_indexs = [table.index(i) for i in key]
    text = [table.index(i) for i in text]

    for i in range(len(text)):
        text[i] = (text[i] - key_indexs[i]) % 29

    decoded = ''

    for i in text:
        decoded += table[i]

    return decoded

print(coder(table, key, "NMWSHAQBV_DRTNJ"))


            
#def brute(text: list[str] = text, limiter: int = 4, table: list[str] = table, hidden_key: list[str] = hidden_key):

    # for i in text:
    #     i = i[:limiter]
    #     for j in i:
    #         print(j)
    # decoded = ''

    # for i in text:
    #     for j in i:
    #         if j == ' ':
    #             continue
    #         index1 = 0
    #         encrpyted = table.index(j)
    #         if hidden_key[index1] != '#':
    #             encrpyted -= table.index(hidden_key[i.index(j)])

    #             if encrpyted < 0:
    #                 encrpyted += len(table)

    #             decoded += table[encrpyted]

    #         else:
    #             for k in range(len(table)):
                    
    #                 decoded += keyChecker(table, j, k)
    #                 print(decoded)
    #                 decoded = decoded[:len(decoded) - 1]

    #         index1 += 1


    #     print(decoded, "\n")
                    

