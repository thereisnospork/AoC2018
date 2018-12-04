# part 1 done in google sheets(sum of all inputs)
import numpy as np

file = open(r'C:\Users\gleonard\PycharmProjects\AoC2018\data\day1.txt')
a = []
for line in file:
    # print(line)
    a.append(int(line.rstrip('\n')))


#
#
# print(a)
# print(sum(a)) # also answer for part 1


def freq_adj(freq, freqs, adj_list):
    for each in a:
        freq = freq + each
        # print(freq)
        if freq in freqs:
            print(freq)
            print(type(freq))
            return freq
        freqs.add(freq)
    return freq_adj(freq, freqs, adj_list)


freqs = set()

ans = freq_adj(0, freqs, a)
print(ans)
print(type(ans))
