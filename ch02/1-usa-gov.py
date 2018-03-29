import json
import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = "/home/mickey/Documents/python/data_analysis/" \
        "pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt"


with open(path) as f:
    records = [json.loads(data) for data in f]


def get_count(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(sequence, n):
    counter = Counter(sequence)
    return counter.most_common(n)
    
timezone = [record['tz'] for record in records if 'tz' in record]

# use pandas to create DateFrame
frame = DataFrame(records)
tz_count = frame['tz'].value_counts()


# use matplotlib to draw a picture
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknow'
tz_count = clean_tz.value_counts()
mlt = tz_count[:10].plot(kind='barh', rot=0)


if __name__ == '__main__':
    #  pass
    #  counts = get_count(timezone)
    #  print(top_counts(timezone,5))
    #  print(frame['tz'][:10])
    #  print(tz_count[:10])
    plt.show()
