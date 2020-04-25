#!/usr/bin/env python
# coding: utf-8

# In[66]:


import Bio
from Bio import SeqIO
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

for seq_record in SeqIO.parse("P08100.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    seq = str(seq_record.seq)
    print(seq)
    

char_list = list(seq)

num_residues=len(seq)
    
df = pd.DataFrame({'chars': char_list})
df['num']=1

df = df.groupby('chars').sum().sort_values('num',ascending=False)
plt.bar(df.index, df.num/num_residues, color=(0.6, 0.3, 0.1, 0.9))


plt.xlabel("Aminoacids")
plt.ylabel("Frequencies of aminoacids in Rhodopsin")


plt.title("Frequency graph of Rhodopsin")

plt.show()


#Amino Acid frequency table


# In[67]:


score_dict= {'I' : 4.5, 'V' : 4.2, 'L' : 3.8, 'F' : 2.8, 'C' : 2.5, 'M' : 1.9, 'A' :1.8, 'G' : -0.4, 'T' : -0.7, 'W' : -0.9, 'S' : -0.8, 'Y' : -1.3, 'P' : -1.6, 'H' : -3.2, 'E' : -3.5, 'Q' : -3.5, 'D' : -3.5 , 'N' : -3.5, 'K' : -3.9, 'R' : -4.5 }


# In[68]:


values = []
for i in seq:
    values.append(score_dict[i])

print(values)


# In[69]:


window_size = int(input("Enter a window size: "))
#print(window_size)



if window_size%2==0:
    half_window_size = int(window_size/2)
elif window_size%2!=0:
    half_window_size = int((window_size+1)/2)

print("half window size is: " + str(half_window_size))


# In[70]:


y_data = []
for i in range(half_window_size, num_residues-half_window_size):
    average_value = 0.0
    for j in range(-half_window_size, half_window_size+1):
        average_value += values[i+j]
    y_data.append(average_value / window_size)

print(y_data)

x_data = range(half_window_size, half_window_size+len(y_data))

plt.plot(x_data, y_data, linewidth=1.0)



# Show exactly the length of the sequence
plt.axis(xmin = 1, xmax = num_residues)

plt.xlabel("residue number")
plt.ylabel("hydrophobicity (moving average over %d values)" % window_size)


plt.title("K&D hydrophobicity for ")

show()


# In[ ]:




