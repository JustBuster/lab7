# def count(s: str) -> dict :
#     count = {}

#     for i in s:
#         if i not in count:
#             count[i] = 1
        
#         else:
#             count[i] += 1

#     return count

# c = count('YV__COQHYZGQZGQTCADIHVFP')
# print(c)

'''
Table for reference:
_	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	.	!
00	01	02	03	04	05	06	07	08	09	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28
'''

t = 'TCADIHVFQGTZVBTVP'

def decoder(key, text):
    table = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','!']
    decoded = ''

    for i in text:
        encrypted = table.index(i)
        encrypted -= key

        if encrypted < 0:
            encrypted += 29

        decoded += table[encrypted]

    return decoded

for i in range(29):
    print(f"Key: {i} Decoded Text: {decoder(i, t)}")
    print("----------------------------------------------------")

#Key: 17 Decoded Text: HELLO._THIS_IS_COMPUTER!