import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    x: 0 or 1 (can also be array)
    p: probability of success
    """
    # Convert to numpy array (for vector support)
    x = np.array(x)
    
    # PMF calculation
    pmf = (p ** x) * ((1 - p) ** (1 - x))
    
    # Moments
    mean = p
    variance = p * (1 - p)
    
    return pmf, mean, variance