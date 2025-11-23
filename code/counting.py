"""
counting.py — Spectral and zeta zero counting functions for Article 4
Author: Seyed Ali Mozhgani
Date: November 2025

This module implements spectral counting functions, Riemann–von Mangoldt formula,
and comparison utilities for Article 4.
"""

import numpy as np

# --- Spectral Counting ---

def spectral_counting(lambdas, T):
    """
    Count number of eigenvalues λ_n <= T.
    
    Parameters:
        lambdas (array-like): eigenvalues λ_n
        T (float): threshold
    
    Returns:
        int: count of eigenvalues below threshold
    """
    lambdas = np.array(lambdas)
    return np.sum(lambdas <= T)

def spectral_asymptotics(T):
    """
    Asymptotic law for spectral counting:
        N_spec(T) ~ (T / 2π) log(T / 2π) - (T / 2π)
    
    Parameters:
        T (float): threshold
    
    Returns:
        float: asymptotic estimate
    """
    return (T / (2*np.pi)) * np.log(T / (2*np.pi)) - (T / (2*np.pi))

# --- Zeta Zero Counting ---

def zeta_counting(gammas, T):
    """
    Count number of zeta zeros γ_n <= T.
    
    Parameters:
        gammas (array-like): ordinates of zeta zeros
        T (float): threshold
    
    Returns:
        int: count of zeros below threshold
    """
    gammas = np.array(gammas)
    return np.sum(gammas <= T)

def riemann_von_mangoldt(T):
    """
    Riemann–von Mangoldt formula:
        N(T) = (T / 2π) log(T / 2π) - (T / 2π) + O(log T)
    
    Parameters:
        T (float): threshold
    
    Returns:
        float: asymptotic estimate
    """
    return (T / (2*np.pi)) * np.log(T / (2*np.pi)) - (T / (2*np.pi))

# --- Comparison Utilities ---

def compare_counts(lambdas, gammas, T):
    """
    Compare spectral and zeta zero counts up to threshold T.
    
    Parameters:
        lambdas (array-like): eigenvalues λ_n
        gammas (array-like): zeta zeros γ_n
        T (float): threshold
    
    Returns:
        dict: containing counts and difference
    """
    spec_count = spectral_counting(lambdas, T)
    zeta_count = zeta_counting(gammas, T)
    return {
        "spectral_count": spec_count,
        "zeta_count": zeta_count,
        "difference": spec_count - zeta_count
    }

# --- Example Usage ---

if __name__ == "__main__":
    # Synthetic eigenvalues λ_n = 2.5n
    lambdas = 2.5 * np.arange(1, 101)
    # First few zeta zeros (approximate)
    gammas = np.array([14.134725, 21.022040, 25.010857, 30.424876, 32.935062,
                       37.586178, 40.918719, 43.327073, 48.005150, 49.773832])
    
    T = 50
    print("Spectral count up to T:", spectral_counting(lambdas, T))
    print("Zeta count up to T:", zeta_counting(gammas, T))
    print("Comparison:", compare_counts(lambdas, gammas, T))
    print("Spectral asymptotics:", spectral_asymptotics(T))
    print("Riemann–von Mangoldt:", riemann_von_mangoldt(T))
