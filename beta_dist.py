#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def my_beta_rejection(alpha, beta):
  """Rejection sampling for Beta distribution (alpha >= 1, beta >= 1)"""

  # Calculate M (maximum of the Beta density)
  M = (alpha - 1)**(alpha - 1) * (beta - 1)**(beta - 1) / (alpha + beta - 2)**(alpha + beta - 2)

  while True:
    Y = np.random.rand()  # Sample from the uniform proposal distribution
    U = np.random.rand()

    # Acceptance criteria
    if U <= (Y**(alpha - 1) * (1 - Y)**(beta - 1)) / M:
      return Y 

# Example Usage
alpha = 1.5
beta = 2.5
n = 100000
samples = np.array([my_beta_rejection(alpha, beta) for _ in range(n)])

print("Sample Mean:", samples.mean())
print("Theoretical Mean:", alpha / (alpha + beta))
print("Sample Standard Deviation:", samples.std())

