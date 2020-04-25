#!/usr/bin/env python
# coding: utf-8

# In[2]:


filename=input("Please enter a file name:  ")
gap=int(input("Please enter a gap penalty score:  "))
match=int(input("Please enter a match score:  "))
miss_m=int(input("Please enter a miss match score:  "))

file_read = open(filename, 'r') 
lines = file_read.readlines()

seq1=lines[0]
seq2=lines[1]

seq1=seq1.replace('\n','')
seq2=seq2.replace('\n','')
rows = len(seq1) + 1
cols = len(seq2) + 1


# In[3]:


#print(seq1)
#print(len(seq1))
#print(rows)
import itertools
import numpy as np


# In[4]:


#print(lines[1])
#print('--')
#print(seq2)
#print(cols)
#print(gap)
#print(match)
#print(miss_m)


# In[5]:


#seq1[0]


# In[6]:


H = np.zeros((rows,cols),np.int)


# In[7]:


H
#print(rows)
#print(cols)

best=0
optloc=(0,0)


# In[8]:


for i in range(1,rows):
    for j in range(1,cols):
        match_score = H[i-1][j-1]+(match if seq1[i-1]==seq2[j-1] else miss_m)
        horizontal = H[i,j-1]+gap
        vertical = H[i-1,j]+gap
        H[i,j]=max(match_score,horizontal,vertical,0)
        
        if H[i][j] >= best:
            best = H[i][j]
            optloc = (i,j)
        #print([seq1[i-1]])
        #print("----")
        #print([seq2[j-1]])
        #print('----')
        #print(H[i-1][j-1])
        #print('---------')
        #print(match_score)
        #print(horizontal)
        #print(vertical)


# In[9]:


#print(optloc)
#print(best)
#print(i,j)


# In[10]:


H


# In[11]:


i,j=optloc
seq1_all=''
seq2_all=''


# In[12]:


while(i>0 and j>0) and H[i][j]>0:
    
    score=H[i][j]
    
    if seq1[i-1]==seq2[j-1]:
        seq1_all=seq1_all + seq1[i-1]
        seq2_all=seq2_all + seq2[j-1]
        i=i-1
        j=j-1
        #print("1")
    elif score==H[i-1][j-1]+ miss_m and H[i-1][j-1]>0:
        seq1_all=seq1_all + seq1[i-1]
        seq2_all=seq2_all + seq2[j-1]
        i=i-1
        j=j-1
        #print("2")
    elif score==H[i][j-1]+gap and H[i][j-1]>0:
        seq1_all=seq1_all + '-'
        seq2_all=seq2_all + seq2[j-1]
        j=j-1
        #print('3')
    elif score==H[i-1][j]+gap and H[i-1][j]>0:
        seq1_all=seq1_all + seq1[i-1]
        seq2_all=seq2_all + '-'
        i=i-1
        #print('4')


# In[13]:


#print(seq1_all)
#print(seq2_all)
seq1_all=seq1_all[::-1]
seq2_all=seq2_all[::-1]
#print(seq1_all)
#print(seq2_all)


# In[14]:


align_list=[]
str_align_list=""
for i in range(len(seq1_all)):
    if seq1_all[i]==seq2_all[i]:
        align_list.append('|')
    elif seq1_all[i]=="-" or seq2_all[i]=='-':
        align_list.append(' ')
    else:
        align_list.append('.')
    str_align_list+=align_list[i]


# In[15]:


str_align_list


# In[17]:


out_file=open("output.txt","w")
out_file.write(seq1)
out_file.write('\n')
out_file.write(seq2)

if len(seq1_all)>0 and len(seq2_all)>0:
    out_file.write('\n')
    out_file.write('\n')
    out_file.write(seq1_all)
    out_file.write('\n')
    out_file.write(str_align_list)
    out_file.write('\n')
    out_file.write(seq2_all)
    out_file.write('\n')
    out_file.write('\n')
format_string = "Score=%d for Match=%d, mismatch = %d, gap = %d"
data = (best, match, miss_m, gap)
out_file.write(format_string % data)


# In[ ]:





# In[ ]:




