from probedict import kommun_dict
from pprint import pprint
import pandas as pd

df = pd.read_excel('location/sveriges-kommuner.xls')
kommun_all = df['Kommuner'].tolist()

kommun_probe=kommun_dict.keys()
probes=[]
for x in kommun_probe:
    probes.append(x)

s = set(probes)
diff = [x for x in kommun_all if x not in s]

def print_nice(diff):
    for x in diff:
        print('{}\n'.format(x))
    print('Antal kommuner utan någon probe: %d/290'% len(diff))

print_nice(diff)
