#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Superoscillation energy-cost demo (1D, band-limited).

Purpose
-------
Show numerically that "going more superoscillatory" (faster local phase
gradient with a fixed max wavenumber) puts almost all L2-norm in the side
lobes, not in the tight core. This is the energy / Born-rule tax.

This does NOT implement a tesseract, phase-conjugate cavity, or free-space
Maxwell solver. It is a minimal band-limited Fourier example.

Run
---
    python scripts/superoscillation_energy_cost_demo.py

Optional
--------
    python scripts/superoscillation_energy_cost_demo.py --plot
        saves plots/superoscillation_energy_cost.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def bandlimited_superoscillation(
    n_modes: int = 9,
    k_max: float = 1.0,
    n_x: int = 20001,
    x_max: float = 40.0,
    target_k: float = 3.0,
    core_halfwidth: float = 0.5,
) -> dict:
    """
    Construct a real band-limited function as a sum of cosines with |k|<=k_max
    whose coefficients are chosen so that, near x=0, it mimics cos(target_k * x)
    with target_k > k_max (superoscillation), by least-squares matching on a
    small window.
    """
    x = np.linspace(-x_max, x_max, n_x)
    # modes 0..n_modes-1 : k = k_max * m/(n_modes-1)
    ks = np.linspace(0.0, k_max, n_modes)
    # design matrix on a small matching window
    w = 1.2  # match window half-width
    mask_m = np.abs(x) <= w
    xm = x[mask_m]
    A = np.column_stack([np.cos(k * xm) for k in ks])
    # target superoscillatory cosine
    y = np.cos(target_k * xm)
    # least squares coefficients
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    # full field
    psi = np.zeros_like(x)
    for c, k in zip(coef, ks):
        psi += c * np.cos(k * x)
    # normalize L2
    dx = x[1] - x[0]
    norm2 = np.sum(psi**2) * dx
    psi = psi / np.sqrt(norm2)
    # core energy fraction
    core = np.abs(x) <= core_halfwidth
    e_core = np.sum(psi[core] ** 2) * dx
    e_side = 1.0 - e_core
    # local wavenumber proxy near 0: |dpsi/dx| / sqrt(psi^2+eps) average
    dpsi = np.gradient(psi, dx)
    mid = np.abs(x) < 0.3
    local_k = np.mean(np.abs(dpsi[mid]) / (np.abs(psi[mid]) + 1e-12))

    return {
        "x": x,
        "psi": psi,
        "ks": ks,
        "coef": coef,
        "k_max": k_max,
        "target_k": target_k,
        "e_core": float(e_core),
        "e_side": float(e_side),
        "local_k": float(local_k),
        "core_halfwidth": core_halfwidth,
    }


def scan_targets(targets: list[float]) -> list[dict]:
    rows = []
    for tk in targets:
        r = bandlimited_superoscillation(target_k=tk)
        rows.append(r)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", action="store_true", help="Save PNG figure")
    args = parser.parse_args()

    print("=" * 70)
    print("SUPEROSCILLATION ENERGY COST (1D band-limited demo)")
    print("=" * 70)
    print("k_max = 1.0  |  core = |x| <= 0.5  |  L2 normalized")
    print()
    print(f"{'target_k':>10}  {'local_k~':>10}  {'E_core':>12}  {'E_side':>12}  {'core%':>8}")
    print("-" * 60)

    targets = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    rows = scan_targets(targets)
    for r in rows:
        print(
            f"{r['target_k']:10.2f}  {r['local_k']:10.3f}  "
            f"{r['e_core']:12.4e}  {r['e_side']:12.4e}  {100*r['e_core']:8.4f}"
        )

    print()
    print("Reading guide:")
    print("  - target_k > k_max means 'superoscillatory intent' on the match window.")
    print("  - As target_k grows, E_core typically collapses: energy flees to side lobes.")
    print("  - For a single photon, Born probability in the core ~ E_core, not ~1.")
    print("  - A 'perfect phase' for a given design yields this split; it does not erase it.")
    print("  - No tesseract appears in this calculation; none is required for the tax.")
    print("=" * 70)

    if args.plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib not available; skip plot")
            return
        r = rows[-2]  # target_k=3.5 example
        x, psi = r["x"], r["psi"]
        fig, ax = plt.subplots(1, 2, figsize=(12, 4))
        ax[0].plot(x, psi, lw=1.0)
        ax[0].axvspan(-r["core_halfwidth"], r["core_halfwidth"], color="C1", alpha=0.2, label="core")
        ax[0].set_xlim(-15, 15)
        ax[0].set_title(f"psi(x), target_k={r['target_k']}, k_max={r['k_max']}")
        ax[0].legend()
        ax[0].grid(alpha=0.3)

        cores = [rr["e_core"] for rr in rows]
        ax[1].semilogy(targets, cores, "o-", lw=2)
        ax[1].set_xlabel("target_k")
        ax[1].set_ylabel("E_core (L2 fraction)")
        ax[1].set_title("Energy tax vs superoscillation strength")
        ax[1].grid(alpha=0.3)

        out_dir = Path("plots")
        out_dir.mkdir(exist_ok=True)
        path = out_dir / "superoscillation_energy_cost.png"
        fig.tight_layout()
        fig.savefig(path, dpi=140)
        print(f"Saved {path}")


if __name__ == "__main__":
    main()
