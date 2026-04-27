import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    k: number of trials (>=1), can be scalar or array
    p: probability of success (0 < p <= 1)
    """
    k = np.array(k)
    
    # PMF calculation
    pmf = ((1 - p) ** (k - 1)) * p
    
    # Mean
    mean = 1 / p
    
    return pmf, mean