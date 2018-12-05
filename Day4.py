import pandas as pd
import numpy as np
import datetime
import re
from statistics import mode

df = pd.read_csv(r'data/day4.txt',delimiter=',', names=['date','message'])
# sorted_indices = df.index['index']
df['date'] = pd.to_datetime(df['date'], format='[%Y-%m-%d %H:%M]')   #[1518-03-31 00:26] #adjusted years to 20th century due to pandas quirk...
df = df.sort_values('date')
print(df)

sorted_i = df.index.values

# print(df.ix[410]['message'])

def get_number(string_):
    try:
        return re.search(r'([0-9]{2,5})', string_).group(1)
    except Exception:
        return False

def sleep_start(datetime_):
    """returns T/F if string is a going to sleep timestamp"""
    string_ = str(datetime_)
    return re.match(r'falls asleep', string_)


def wake_up(datetime_):
    """returns T/F if string is a waking up timestamp"""
    string_ = str(datetime_)
    return re.match(r'wakes', string_)


# test

# test = get_number('#199')
# # print(test)

guards = dict()
n=-1
t0s = []
tfs = []

while n < len(sorted_i)-1:
    n += 1
    line = df.ix[sorted_i[n]]
    guard = line['message']
    guard = get_number(guard)
    # print([guard,n])

    if guard:
        last_guard = guard
        continue

    if sleep_start(line['message']):
        t0 = line['date']
        continue

    if wake_up(line['message']):
        tf = line['date']
        delta_t = tf - t0
        delta_t = delta_t.seconds//60 #but no minutes direct.... fu!
        if last_guard in guards:
            guards[last_guard] += delta_t
        else:
            guards[last_guard] = delta_t

    if last_guard == '2953':
        t0s.append(t0.minute)
        tfs.append(tf.minute)
#         print(t0)
#         print(tf)
#
#
#
#
# print(df.ix[sorted_i[60]])
# print(df.ix[sorted_i[61]])
# print(df.ix[sorted_i[62]])


print(guards)
print(max(guards.values()))

# guard is 2953, probably




print(t0s)
print(tfs)
#
minutes_asleep = list()  #
for i, start in enumerate(t0s):
    # print(start)
    # print(tfs[i])
    slept = range(start, tfs[i])
    print(slept)
    minutes_asleep = minutes_asleep + list(slept)


print(minutes_asleep)
print(mode(minutes_asleep))

# print(minutes_asleep)


# print(our_guy)

#
# print(sorted)
#
# guards = dict()
# for n, index in enumerate(sorted):
#     message = df.ix[index]['message']
#     date = df.ix[index[n+1]]['date']
#     date = date
#     guard_num = None
#     time asleep = datetime.strptime(date)