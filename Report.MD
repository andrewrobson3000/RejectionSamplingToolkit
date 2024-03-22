# Report for Gamma and Beta Distribution Sampling

## Introduction

**Rejection Sampling**

Rejection sampling is a versatile Monte Carlo technique used to generate random samples from distributions that are difficult to sample from directly.  Here's how it works:

* **Target Distribution:** We want to sample from a distribution with probability density function (pdf) π(x).  

* **Proposal Distribution:** We choose a simpler distribution q(x) from which we can easily generate samples. This distribution should 'envelope' π(x), meaning q(x) ≥ π(x) for all possible x values.

* **Bounding Constant:** We find a constant M such that Mq(x) ≥ π(x) for all x values.  The smaller M is, the more efficient the process.

* **Sampling and Acceptance:**
    1. We draw a sample `X` from the proposal distribution q(x).
    2. We generate a uniform random number `U` between 0 and 1.
    3. We accept `X` as a sample from π(x) if  `U ≤ π(x) / (Mq(x))`. If not, we reject `X` and repeat.

* **Why does this work?** The acceptance criterion ensures that the final distribution of accepted samples matches the target distribution π(x).  
* **Efficiency Considerations:**
    *  The average number of trials needed for a successful sample is M. A tighter envelope (smaller M) improves efficiency.
    * We can use rejection sampling even when π(x) and q(x) are only known up to normalizing constants, as long as we can establish an appropriate bounding constant.

## Gamma Distribution Sampling

**The `my_gamma` Function**

This function simulates values from a Gamma distribution with non-integer shape parameters `a`.

**How It Works**

* **Parameter Validation:** Ensures that `a` (shape) and `b` (rate) are valid.
* **Intermediate Variables:** Calculates necessary quantities for determining acceptance probabilities in the rejection sampling process.
* **Rejection Sampling Loop:**
    * Generates a candidate sample `Y` from a Gamma distribution with parameters `aq` and `bq` (related to the target Gamma distribution).  
    * Calculates an acceptance probability based on the target Gamma distribution.
    * Accepts `Y` if a uniformly generated random value falls below the acceptance probability.

**Simulation and Analysis**

Using parameters `a = 7.5` and `b = 0.5`, we generated `n = 100000` samples. Key observations:

* **Accuracy:** The sample mean (15.0102) closely matches the theoretical mean (a/b = 15.0).
* **Consistency:** The sample standard deviation, when scaled appropriately (0.0174), aligns with the theoretical value (sqrt(a/n)/b = 0.0173).
* **Efficiency:** The average number of trials per successful sample (1.03691) is low, highlighting the efficiency of the rejection sampling method.

**The `my_gamma_modified` Function**

This function directly simulates Gamma-distributed values without rejection sampling.

**How It Works**

* Leverages specialized functions (e.g., `np.random.gamma`) to directly generate samples from the Gamma distribution.
* Always accepts generated samples.

**Simulation and Analysis**

Simulating `n = 10000` samples with `a = 7.5` and `b = 0.5` consistently requires an average of 1 trial per sample, demonstrating the inherent efficiency of direct sampling.

## Beta Distribution Sampling

**The `my_beta_rejection` Function**

Implements rejection sampling for Beta distributions where shape parameters α ≥ 1 and β ≥ 1.

**How It Works**

* **Calculate M:** Finds the maximum value of the Beta density, used for creating an 'envelope' distribution.
* **Envelope Distribution:** The uniform distribution serves as the envelope for the Beta distribution in this case.
* **Sampling Loop:**
    * Generates a candidate sample `Y` from a uniform distribution.
    * Compares the scaled Beta density at `Y` to a uniform random value.
    * Accepts `Y` if it falls within the scaled Beta distribution's curve.

**Simulation and Analysis**

With parameters α = 1.5 and β = 2.5, we generated n = 100000 samples. Results:

* **Accuracy:** The sample mean (0.374068) is very close to the theoretical mean (0.375).
* **Expected Variability:** The sample standard deviation (0.216524) is in line with the Beta distribution's behavior.

## Conclusion

Both rejection sampling (`my_gamma`) and direct sampling (`my_gamma_modified`) effectively generate Gamma-distributed random variables.  Rejection sampling offers flexibility for non-integer shape parameters, while direct sampling is generally more efficient. The Beta distribution example highlights the use of rejection sampling for distributions where direct sampling might be less straightforward.