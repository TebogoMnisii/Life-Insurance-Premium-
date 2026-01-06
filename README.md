
# 🧮 Life Insurance Premium Calculator (Actuarial)

This repository implements a **life insurance actuarial pricing model** that calculates the **net single premium** for a term life insurance policy using **mortality tables and present value principles**.

The project demonstrates core **actuarial mathematics concepts**, including mortality risk modeling, survival probabilities, and discounted cash flow valuation.

This work forms part of **Aureus Capital Intelligence (demo-stage)** and is intended for **analytical demonstration and portfolio use**.

---

## 🎯 Objective

To calculate the **net single premium** of a life insurance policy based on:
- Policyholder age
- Mortality probabilities
- Interest rate assumptions
- Sum assured

---

## 📊 Actuarial Methodology

- Discrete-time mortality modeling using `q_x`
- Survival probability accumulation (`p_x`)
- Present value discounting
- Expected value of death benefits
- Net single premium calculation

---

## 🔬 Model Description

The premium is calculated as:

- Iterating over future ages until terminal age
- Computing the probability of death in each policy year
- Discounting the expected benefit payment
- Summing expected present values across policy years

This approach follows **classical actuarial pricing theory**.

---

## 🧪 Example Output

```text
Net single premium for age 30: R12,345.67
