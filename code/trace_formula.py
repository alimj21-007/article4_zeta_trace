"""
trace_formula.py — Trace formula implementation for Article 4
Author: Seyed Ali Mozhgani
Date: November 2025

This module implements a simplified trace formula framework for spectral analysis
and comparison with Riemann zeta zeros.
"""

import numpy as np

# --- Core Trace Formula Components ---

def trace_formula(f, zeta_zeros, trivial_zeros=None, archimedean_term=None):
    """
    Compute trace formula approximation:
        Tr(f(T)) = sum_{rho} f(rho) - f(1) + sum_{m>=1} f(-2m) + A(f)

    Parameters:
        f (callable): test function, e.g. lambda s: np.exp(-s**2)
        zeta_zeros (array-like): nontrivial zeros γ_n
        trivial_zeros (array-like): optional list of trivial zeros (-2m)
        archimedean_term (callable): optional archimedean contribution A(f)

    Returns:
        float: trace formula value
    """
    # Nontrivial zeros contribution
    rho_sum = np.sum([f(rho) for rho in zeta_zeros])

    # Pole at s=1
    pole_term = -f(1)

    # Trivial zeros contribution
    trivial_sum = 0.0
    if trivial_zeros is not None:
        trivial_sum = np.sum([f(tz) for tz in trivial_zeros])

    # Archimedean contribution
    arch_term = 0.0
    if archimedean_term is not None:
        arch_term = archimedean_term(f)

    return rho_sum + pole_term + trivial_sum + arch_term


# --- Helper Functions ---

def generate_trivial_zeros(M=10):
    """
    Generate first M trivial zeros of zeta: -2, -4, -6, ...
    """
    return [-2*m for m in range(1, M+1)]

def archimedean_contribution(f, samples=1000):
    """
    Approximate archimedean contribution A(f) via numerical integration.
    For demonstration, we use a Gaussian weight.
    """
    x = np.linspace(0.1, 10, samples)
    return np.trapz([f(val) * np.exp(-val) for val in x], x)


# --- Example Usage ---

if __name__ == "__main__":
    # Example: test function
    f = lambda s: np.exp(-s**2)

    # Synthetic zeta zeros (first few ordinates)
    zeta_zeros = [14.134725, 21.022040, 25.010857, 30.424876, 32.935062]

    # Trivial zeros
    trivial_zeros = generate_trivial_zeros(M=5)

    # Compute trace formula
    result = trace_formula(f, zeta_zeros, trivial_zeros, archimedean_contribution)
    print("Trace formula result:", result)
