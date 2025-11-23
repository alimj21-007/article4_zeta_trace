# Frequently Asked Questions (FAQ)

## 1. What is the main goal of Article 4?
The paper develops a framework for **trace formulas** and **spectral counting** associated with the Riemann zeta function. It compares synthetic spectral data with the distribution of zeta zeros.

## 2. Why use synthetic eigenvalues?
Synthetic eigenvalues (e.g., λₙ = 2.5n) provide a controlled model to test operator-theoretic identities and numerical experiments without requiring a fully defined Hilbert–space operator.

## 3. How are normalized spectral values defined?
We define normalized spectral values as:
\[
\mu_n = 0.5 \cdot \lambda_n + 10
\]
This scaling aligns the synthetic spectrum with the range of zeta zeros for comparison.

## 4. What datasets are included?
- `spectval_vs_zeta.csv`: comparison of spectral values μₙ and zeta zeros γₙ  
- `error_bounds.csv`: absolute and relative error analysis  
- Figures: comparison plots, spacing plots, density overlays, and trace plots  

## 5. How are spacing statistics computed?
Spacing statistics are computed as differences between consecutive values:
\[
\mu_{n+1} - \mu_n \quad \text{and} \quad \gamma_{n+1} - \gamma_n
\]

## 6. What is the trace formula used?
The simplified trace formula is:
\[
\mathrm{Tr}(f(T)) = \sum_{\rho} f(\rho) - f(1) + \sum_{m \geq 1} f(-2m) + \mathcal{A}(f)
\]
where ρ are nontrivial zeros, -2m are trivial zeros, and $\mathcal{A}(f)$ is the archimedean contribution.

## 7. How can I reproduce the figures?
Use the Python scripts in the `code/` directory:
- `operators.py` for eigenvalues and normalized values  
- `kernels.py` for kernel evaluations  
- `counting.py` for counting functions  
- `plots.py` for generating figures  

## 8. Where are outputs stored?
All figures are saved in `output/figures/` and CSV data files in `output/data/`. Logs are stored in `output/logs/`.

## 9. What is the broader significance?
The experiments support the **spectral interpretation of Riemann zeros**, showing structural parallels between operator spectra and zeta zero distributions. This contributes to bridging analytic number theory and spectral/operator theory.
