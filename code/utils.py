"""
utils.py — General utility functions for Article 4
Author:Seyed Ali Mozhgani
Date: November 2025

This module provides helper functions for data handling, normalization,
CSV export, and reproducibility in spectral/zeta analysis.
"""

import numpy as np
import csv
import os

# --- Normalization Utilities ---

def normalize(array):
    """
    Normalize an array to mean 0 and variance 1.
    
    Parameters:
        array (array-like): input values
    
    Returns:
        np.ndarray: normalized values
    """
    arr = np.array(array, dtype=float)
    return (arr - np.mean(arr)) / np.std(arr)

def scale(array, factor=1.0, shift=0.0):
    """
    Scale and shift an array.
    
    Parameters:
        array (array-like): input values
        factor (float): scaling factor
        shift (float): additive shift
    
    Returns:
        np.ndarray: transformed values
    """
    arr = np.array(array, dtype=float)
    return factor * arr + shift

# --- CSV Export Utilities ---

def export_csv(filename, headers, rows, folder="output/data"):
    """
    Export data to CSV file.
    
    Parameters:
        filename (str): name of CSV file
        headers (list): list of column names
        rows (list of lists): data rows
        folder (str): target folder
    
    Returns:
        str: full path of saved file
    """
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    return filepath

# --- Error Metrics ---

def mean_absolute_error(approx, exact):
    """
    Compute mean absolute error (MAE).
    """
    approx = np.array(approx, dtype=float)
    exact = np.array(exact, dtype=float)
    return np.mean(np.abs(approx - exact))

def mean_relative_error(approx, exact):
    """
    Compute mean relative error (MRE).
    """
    approx = np.array(approx, dtype=float)
    exact = np.array(exact, dtype=float)
    return np.mean(np.abs(approx - exact) / np.abs(exact))

# --- Logging Utilities ---

def log_message(message, logfile="output/logs/run.log"):
    """
    Append a message to a log file.
    
    Parameters:
        message (str): log message
        logfile (str): path to log file
    """
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(message + "\n")

# --- Example Usage ---

if __name__ == "__main__":
    # Example normalization
    data = [10, 20, 30, 40, 50]
    print("Normalized:", normalize(data))
    
    # Example scaling
    print("Scaled:", scale(data, factor=0.5, shift=10))
    
    # Example CSV export
    headers = ["n", "mu_n", "gamma_n", "abs_error"]
    rows = [[1, 11.25, 14.134725, 2.884725],
            [2, 12.5, 21.022040, 8.522040]]
    path = export_csv("test.csv", headers, rows)
    print("CSV saved to:", path)
    
    # Example logging
    log_message("Test run completed successfully.")
