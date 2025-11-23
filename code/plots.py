"""
plots.py — Visualization utilities for Article 4
Author:Seyed Ali Mozhgani
Date: November 2025

This module provides plotting functions for spectral analysis and comparison
with Riemann zeta zeros. It generates comparison plots, spacing plots,
density overlays, and trace plots.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Comparison Plot ---

def plot_comparison(mu_values, gamma_values, savepath="comparison_plot.png"):
    """
    Plot normalized spectral values μ_n vs zeta zeros γ_n.
    """
    plt.figure(figsize=(8,5))
    plt.plot(mu_values, label="Spectral μ_n", marker="o")
    plt.plot(gamma_values, label="Zeta zeros γ_n", marker="x")
    plt.xlabel("n")
    plt.ylabel("Value")
    plt.title("Comparison: Spectral vs Zeta Zeros")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(savepath, dpi=300)
    plt.close()

# --- Spacing Plot ---

def plot_spacing(mu_values, gamma_values, savepath="spacing_plot.png"):
    """
    Plot spacing between consecutive μ_n and γ_n.
    """
    mu_spacing = np.diff(mu_values)
    gamma_spacing = np.diff(gamma_values)
    plt.figure(figsize=(8,5))
    plt.plot(mu_spacing, label="Spectral spacing", marker="o")
    plt.plot(gamma_spacing, label="Zeta spacing", marker="x")
    plt.xlabel("n")
    plt.ylabel("Spacing")
    plt.title("Spacing Comparison: Spectral vs Zeta Zeros")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(savepath, dpi=300)
    plt.close()

# --- Density Plot ---

def plot_density(mu_values, gamma_values, bins=20, savepath="density_plot.png"):
    """
    Overlay histograms of μ_n and γ_n.
    """
    plt.figure(figsize=(8,5))
    plt.hist(mu_values, bins=bins, alpha=0.5, label="Spectral μ_n")
    plt.hist(gamma_values, bins=bins, alpha=0.5, label="Zeta zeros γ_n")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Density Overlay: Spectral vs Zeta Zeros")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(savepath, dpi=300)
    plt.close()

# --- Trace Plot ---

def plot_trace(lambdas, t_values, savepath="trace_plot.png"):
    """
    Plot trace function Tr(f(T)) = sum exp(t * λ_n).
    """
    traces = []
    for t in t_values:
        traces.append(np.sum(np.exp(t * np.array(lambdas))))
    plt.figure(figsize=(8,5))
    plt.plot(t_values, traces, marker="o")
    plt.xlabel("t")
    plt.ylabel("Trace value")
    plt.title("Trace Function Plot")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(savepath, dpi=300)
    plt.close()

# --- Example Usage ---

if __name__ == "__main__":
    # Synthetic data
    lambdas = 2.5 * np.arange(1, 21)
    mu_values = 0.5 * lambdas + 10
    gamma_values = np.array([14.134725, 21.022040, 25.010857, 30.424876,
                             32.935062, 37.586178, 40.918719, 43.327073,
                             48.005150, 49.773832, 52.970, 56.446, 59.347,
                             60.831, 65.112, 67.079, 69.546, 72.067, 75.704, 77.144])

    # Generate plots
    plot_comparison(mu_values, gamma_values)
    plot_spacing(mu_values, gamma_values)
    plot_density(mu_values, gamma_values)
    plot_trace(lambdas, np.linspace(0.01, 0.1, 20))
    print("Plots generated and saved.")
