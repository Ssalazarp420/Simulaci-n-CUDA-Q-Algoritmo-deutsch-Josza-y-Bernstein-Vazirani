# Deutsch-Jozsa & Bernstein-Vazirani with NVIDIA CUDA-Q ⚛️

![Python](https://img.shields.io/badge/Python-3.10-blue)
![CUDA-Q](https://img.shields.io/badge/NVIDIA-CUDA--Q-76B900)
![Status](https://img.shields.io/badge/Status-Completed-success)

Implementation and simulation of the Deutsch-Jozsa and Bernstein-Vazirani quantum algorithms using **NVIDIA CUDA-Q**. This project compares the standard gate-based implementation (using an auxiliary qubit) against an optimized approach (using phase logic without auxiliary qubits), validated on a local GPU.

## 📋 Abstract

This project explores the physical and logical implementation of quantum oracle algorithms based on the theoretical framework of **Discrete-Time Quantum Walks (DTQW)**. 

We simulated two approaches:
1.  **Standard Approach:** Uses $n+1$ qubits and CNOT gates for *Phase Kickback*.
2.  **Optimized Approach:** Uses $n$ qubits and local Z-gates, eliminating the need for an auxiliary qubit and reducing circuit depth.

The simulations were executed on a **NVIDIA GTX 1650** GPU using the `nvidia-fp32` backend.

## 🚀 Features

* **No Auxiliary Qubit:** Implementation of oracles using direct phase injection ($(-1)^{f(x)}$).
* **GPU Acceleration:** Logic executed on NVIDIA hardware via CUDA-Q.
* **Benchmarking:** Comparison of circuit depth and qubit count between methods.
* **Scalability Analysis:** Theoretical analysis of complexity for $n > 3$.

## 🛠️ Installation & Setup

This project requires **Linux** (or WSL2 on Windows) due to CUDA-Q dependencies.

### 1. Prerequisites
* WSL2 (Ubuntu 22.04 recommended)
* Conda (Miniconda)
* NVIDIA Drivers

### 2. Environment Setup
Since standard pip installation might conflict with newer CUDA drivers (v13+), use the following steps:

```bash
# Create a dedicated environment
conda create -n cudaq_env python=3.10 -y
conda activate cudaq_env

# Install CUDA-Q ignoring build isolation (Fix for Driver Compatibility)
pip install --no-build-isolation cudaq

# Install other dependencies
pip install matplotlib numpy
