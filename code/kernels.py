"""
kernels.py — Spectral kernels and error analysis for Article 4
Author: Seysd Ali Mozhgani
Date: November 2025

This module defines numerical kernels and error functions used in trace computations,
spectral comparisons, and zeta zero analysis.
"""

import numpy as np

# --- Spectral Kernels ---

def exponential_kernel(lambda_array, t):
    """
    Kernel: exp(t * lambda)
    Used in trace computations: Tr(f(T)) = sum exp(t * lambda_n)
    
    Parameters:
        lambda_array (array-like): Eigenvalues λₙ
        t (float): Evaluation parameter

    Returns:
        np.ndarray: Kernel values
    """
    return np.exp(t * np.array(lambda_array))

def gaussian_kernel(lambda_array, t, sigma=1.0):
    """
    Kernel: exp(- (t - lambda)^2 / (2 * sigma^2))
    Useful for smoothing spectral contributions

    Parameters:
        lambda_array (array-like): Eigenvalues λₙ
        t (float): Evaluation point
        sigma (float): Width of Gaussian

    Returns:
        np.ndarray: Smoothed kernel values
    """
    lambda_array = np.array(lambda_array)
    return np.exp(- (t - lambda_array)**2 / (2 * sigma**2))

def sinc_kernel(lambda_array, t, scale=1.0):
    """
    Kernel: sinc(scale * (t - lambda))
    Used for band-limited approximations

    Parameters:
        lambda_array (array-like): Eigenvalues λₙ
        t (float): Evaluation point
        scale (float): Frequency scaling

    Returns:
        np.ndarray: Sinc kernel values
    """
    lambda_array = np.array(lambda_array)
    return np.sinc(scale * (t - lambda_array))

# --- Trace and Spacing Utilities ---

def trace_sum(kernel_values):
    """
    Sum over kernel values to compute trace approximation

    Parameters:
        kernel_values (array-like): Values from kernel evaluation

    Returns:
        float: Trace estimate
    """
    return np.sum(kernel_values)

def spacing(array):
    """
    Compute spacing between consecutive values

    Parameters:
        array (array-like): Sequence of values

    Returns:
        np.ndarray: Differences between consecutive entries
    """
    array = np.array(array)
    return np.diff(array)

# --- Error Analysis ---

def absolute_error(approx, exact):
    """
    Compute absolute error between two arrays

    Parameters:
        approx (array-like): Approximated values
        exact (array-like): Reference values

    Returns:
        np.ndarray: Absolute errors
    """
    return np.abs(np.array(approx) - np.array(exact))

def relative_error(approx, exact):
    """
    Compute relative error between two arrays

    Parameters:
        approx (array-like): Approximated values
        exact (array-like): Reference values

    Returns:
        np.ndarray: Relative errors
    """
    approx = np.array(approx)
    exact = np.array(exact)
    return np.abs(approx - exact) / np.abs(exact)
