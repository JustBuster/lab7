n = 4559
for i in range(2, n):
    if n % i == 0:
        print(i, n/i)

        T = (i-1) * (n//i - 1)

e = 5
for i in range(2, T):
    if i*e % T == 1:
        print('d: %d e: %d' % (i, e))
        d = i

c = 2333

m = (c**d) % n
print(m)

'''
Table for reference:
_	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	.	!
00	01	02	03	04	05	06	07	08	09	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28
'''