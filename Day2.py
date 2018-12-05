import re




file = open(r'data/day2.txt')
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
# print(a)

for word in a: ###ugly...
    for word_compare in a:
        errors = 0
        for i, letter in enumerate(word_compare):
            if word[i] != word_compare[i]:
                errors = errors + 1
                error_index = i
            if errors > 1:
                break
        if errors == 1:
            in_common = set(word)
            print(in_common)
            in_common.remove(word[error_index])

            print(word[error_index])
            print([word, word_compare])
            print(in_common)