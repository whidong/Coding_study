import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
def show_binomial_distribution(n, p):
  y = np.arange(n+1)
  prob = binom.pmf(y, n, p)
# plotting y vs pmf(y)
  plt.bar(y, prob)
  plt.xlabel("y", fontsize=13)
  plt.ylabel("probability", fontsize=13)
  plt.title("n="+str(n)+", p="+str(p), fontsize=15)
  plt.show()
  return None
show_binomial_distribution(10, 0.1)
show_binomial_distribution(10, 0.5)
show_ebinomial_distribution(10, 0.9)