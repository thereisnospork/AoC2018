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
        slept = list(range(t0.minute, tf.minute))

        if last_guard in guards:
            guards[last_guard] = guards[last_guard] + slept
        else:
            guards[last_guard] = slept



print(guards)
for key, value in guards.items():
    try:
        mode_ = mode(value)
        num = value.count(mode_)

        print('guard #{} slept most, {}x at minute {}'.format(key, num, mode_))
    except Exception:
        None

# print(max(guards.values()))

# guard is 2953, probably



