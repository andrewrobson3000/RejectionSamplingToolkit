# Rejection Sampling: A Monte Carlo Sampling Technique

**Overview**

This repository contains code examples and explanations of the rejection sampling algorithm, a versatile Monte Carlo method for generating random samples from complex distributions.

**What is Rejection Sampling?**

Rejection sampling is a technique used when direct sampling from a target distribution is difficult or computationally expensive. It works by proposing samples from a simpler, known distribution (the proposal distribution) and selectively accepting them based on their fit to the target distribution.

**Key Concepts**

* **Target Distribution:** The distribution we want to sample from.
* **Proposal Distribution:** A simpler distribution that we can easily sample from. This distribution should "envelope" the target distribution, meaning that the proposal distribution takes greater-than-or-equal values for all possible inputs.
* **Bounding Constant (M):** A scaling factor that ensures the proposal distribution fully covers the target distribution.
* **Acceptance Criteria:**  Determines whether we accept or reject a proposed sample. 

**When to Use Rejection Sampling**

* The target distribution is complex or has an unusual shape.
* The cumulative distribution function (CDF) of the target distribution is difficult or impossible to calculate.
* Efficiency is a concern, and a suitable proposal distribution can be found.

**In This Repository**

* **Code Examples:**  Python implementations for simulating random variables using rejection sampling (e.g., Gamma and Beta distributions).
* **Explanation:** A detailed breakdown and analysis of the rejection sampling process in Report.md

**Let's Get Started!**  

Explore the code, experiment with different distributions, and discover the power of rejection sampling. 
