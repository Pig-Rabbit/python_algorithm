# print out the maximum of each array element (tuple, sentence, sentence list)

from max import max_of
t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'the maximum of {t} is {max_of(t)}')
print(f'the maximum of {s} is {max_of(s)}')
print(f'the maximum of {a} if {max_of(a)}')