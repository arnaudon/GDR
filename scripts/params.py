import numpy as np
import sys

dataset = sys.argv[-1] if len(sys.argv)>0 else 'cora-d'
#which prior distribution, cosine similarity or MLP
tpe_prior    = 'cos' #or 'mlp' 

#which markov times
t_max = 1.0 #maximum time
N_t = 1000   #number of timesteps

#number of time steps to use for t_min scan
n_min = 500 

#which type of random walk dynamics: Combinatorial or Normalised
tpe_rw = 'Combinatorial'
#tpe_rw = 'Normalized'
#tpe_rw = 'max_entropy'

