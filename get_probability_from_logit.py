# coding: utf-8

# Function to get us probability based upon a logit, which is the log of the odds, (p / (1-p)).
import numpy as np
def get_probability_from_logit(x):
    return np.exp(x) / (1 + np.exp(x))

