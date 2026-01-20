

## What is the central limit theorem?

The **Central Limit Theorem (CLT)** is a key concept in statistics stating that ==if you take large enough samples from any population with finite variance, the distribution of the sample means will resemble a normal distribution (bell curve), regardless of the original population's distribution==.

![[Pasted image 20251112152430.png]]

![[Pasted image 20251112102301.png]]


## Central limit theorem formula

Fortunately, you don’t need to actually repeatedly sample a population to know the shape of the sampling distribution. The [parameters](https://www.scribbr.com/statistics/parameter-vs-statistic/) of the sampling distribution of the mean are determined by the parameters of the population:

- The [mean](https://www.scribbr.com/statistics/mean/) of the sampling distribution is the mean of the population.

  ![[Pasted image 20251107025852.png]]
- The [standard deviation](https://www.scribbr.com/statistics/standard-deviation/) of the sampling distribution is the standard deviation of the population divided by the square root of the sample size.

  ![\begin{equation*}\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}\end{equation*}](https://www.scribbr.com/wp-content/ql-cache/quicklatex.com-6443a361247d9c6f5764e4503e390634_l3.png "Rendered by QuickLaTeX.com")![[Pasted image 20251107025903.png]]

We can describe the sampling distribution of the mean using this notation:

![[Pasted image 20251112102523.png]]

Where:

- X̄ is the sampling distribution of the sample means
- ~ means “follows the distribution”
- _N_ is the [normal distribution](https://www.scribbr.com/statistics/normal-distribution/)
- µ is the mean of the population
- σ is the standard deviation of the population
- _n_ is the sample size

## Sample size and the central limit theorem

The **sample size** (_n_) is the number of observations drawn from the population for each sample. The sample size is the same for all samples.

The sample size affects the sampling distribution of the mean in two ways.

### 1. Sample size and normality

The larger the sample size, the more closely the sampling distribution will follow a [normal distribution](https://www.scribbr.com/statistics/normal-distribution/).

When the sample size is small, the sampling distribution of the mean is sometimes non-normal. That’s because the central limit theorem only holds true when the sample size is “sufficiently large.”

By convention, we consider a sample size of 30 to be “sufficiently large.”

- **When** **_n_** **< 30**, the central limit theorem doesn’t apply. The sampling distribution will follow a similar distribution to the population. Therefore, the sampling distribution will only be normal if the population is normal.

- **When** **_n_** **≥ 30**, the central limit theorem applies. The sampling distribution will approximately follow a normal distribution.

### 2. Sample size and standard deviations

The sample size affects the standard deviation of the sampling distribution. Standard deviation is a measure of the [variability](https://www.scribbr.com/statistics/variability/) or spread of the distribution (i.e., how wide or narrow it is).

- **When** **_n_** **is low**, the standard deviation is high. There’s a lot of spread in the samples’ means because they aren’t precise estimates of the population’s mean.

- **When** **_n_** **is high**, the [standard deviation](https://www.scribbr.com/statistics/standard-deviation/) is low. There’s not much spread in the samples’ means because they’re precise estimates of the population’s mean.

## Conditions of the central limit theorem

The central limit theorem states that the sampling distribution of the mean will always follow a [normal distribution](https://www.scribbr.com/statistics/normal-distribution/) under the following conditions:

1. The sample size is **sufficiently large**. This condition is usually met if the sample size is _n_ ≥ 30.

2. The samples are **independent and identically distributed (i.i.d.) random variables**. This condition is usually met if the [sampling is random](https://www.scribbr.com/methodology/simple-random-sampling/).

3. The population’s distribution has **finite** [**variance**](https://www.scribbr.com/statistics/variance/). Central limit theorem doesn’t apply to distributions with infinite variance, such as the Cauchy distribution. Most distributions have finite variance.

![[Pasted image 20251112195327.png]]