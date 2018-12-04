import re




file = open(r'C:\Users\gleonard\PycharmProjects\AoC2018\data\day2.txt')
a = []
for line in file:
    a.append(str(line.strip()))

def countx(strings,num):
    counter = 0
    for word in strings:
        for char in word:
            if word.count(char) == num:
                counter += 1
                break
    return counter






twos = countx(a,2)
threes = countx(a,3)

# print(twos*threes) # part 1 answer


# print(a)
# part 2
b = []
for word in a:
    b.append(dict.fromkeys(word))

print(b)