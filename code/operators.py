"""
operators.py — Operator definitions and spectral utilities for Article 4
Author: Seyed Ali Mozhgani
Date: November 2025

This module defines model operators, spectral utilities, and helper functions
for trace formulas and zeta zero comparisons.
"""

import numpy as np

# --- Model Operator Definitions ---

class ScalingOperator:
    """
    Model operator T acting on f(x) = -x * d/dx f(x).
    Here we simulate eigenvalues as λ_n = alpha * n.
    """

    def __init__(self, alpha=2.5):
        self.alpha = alpha

    def eigenvalues(self, N=100):
        """
        Generate synthetic eigenvalues λ_n = alpha * n
        Parameters:
            N (int): number of eigenvalues
        Returns:
            np.ndarray: array of eigenvalues
        """
        return self.alpha * np.arange(1, N+1)

    def normalized_values(self, N=100):
        """
        Compute normalized spectral values μ_n = 0.5 * λ_n + 10
        Parameters:
            N (int): number of values
        Returns:
            np.ndarray: array of normalized values
        """
        lambdas = self.eigenvalues(N)
        return 0.5 * lambdas + 10

# --- Utility Functions ---

def spectral_spacing(values):
    """
    Compute spacing between consecutive spectral values.
    Parameters:
        values (array-like): sequence of spectral values
    Returns:
        np.ndarray: differences between consecutive entries
    """
    values = np.array(values)
    return np.diff(values)

def compare_with_zeta(mu_values, gamma_values):
    """
    Compare spectral values μ_n with zeta zeros γ_n.
    Parameters:
        mu_values (array-like): normalized spectral values
        gamma_values (array-like): zeta zeros
    Returns:
        dict: containing abs_error and rel_error arrays
    """
    mu_values = np.array(mu_values)
    gamma_values = np.array(gamma_values)
    abs_error = np.abs(mu_values - gamma_values)
    rel_error = abs_error / np.abs(gamma_values)
    return {
        "abs_error": abs_error,
        "rel_error": rel_error
    }

def trace_function(lambdas, t):
    """
    Compute trace function Tr(f(T)) = sum exp(t * λ_n).
    Parameters:
        lambdas (array-like): eigenvalues λ_n
        t (float): evaluation parameter
    Returns:
        float: trace value
    """
    lambdas = np.array(lambdas)
    return np.sum(np.exp(t * lambdas))
