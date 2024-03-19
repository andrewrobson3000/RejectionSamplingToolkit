#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random

def my_gamma(a=1, b=1):
    if a < 1 or b <= 0:
        raise ValueError('a < 1 or b <= 0')
    
    aq = int(np.floor(a))  # Equivalent to floor(a) in R
    bq = b * (aq / a)  # Best choice but any 0 < bq < b OK
    del_a = a - aq
    del_b = b - bq
    
    finished = False
    count = 0  # To count the number of trials
    
    while not finished:
        Y = np.sum(np.random.exponential(1/bq, aq))  # Y ~ Gamma(aq, bq)
        U = random.uniform(0, 1)
        accept_prob = (Y*del_b/del_a)**del_a * np.exp(-del_b*Y + del_a)
        finished = U < accept_prob
        count += 1
    
    return Y, count

# Example usage
a = 7.5
b = 0.5
n = 100000
samples = [my_gamma(a, b) for _ in range(n)]
X = [sample[0] for sample in samples]  # Extract the generated samples
N = [sample[1] for sample in samples]  # Extract the number of trials for each sample

print(f"Mean of X: {np.mean(X)}, should be close to a/b = {a/b}")
print(f"Standard deviation of X: {np.std(X)/np.sqrt(n)}, should be close to sqrt(a/n)/b = {np.sqrt(a/n)/b}")
print(f"Average number of trials needed: {np.mean(N)}")



# In[ ]:


def my_gamma_modified(a=1, b=1):
    if a < 1 or b <= 0:
        raise ValueError('a < 1 or b <= 0')
    
    finished = False
    count = 0  # To count the number of trials
    
    while not finished:
        Y = np.random.gamma(shape=a, scale=1/b)  # Directly simulate Y ~ Gamma(a, b)
        count += 1
        finished = True  # In this direct simulation, Y is always accepted
    
    return Y, count

# Example usage to calculate the mean number of trials
a = 7.5
b = 0.5
n = 10000
trials = [my_gamma_modified(a, b)[1] for _ in range(n)]

print(f"Average number of trials needed: {np.mean(trials)}")
