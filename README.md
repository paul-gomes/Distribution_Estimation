# Project 1 - Distribution estimation

### Gaussian Mixture Model (GMM)

GMMs assume that there are a certain number of Gaussian distributions, and each of these distributions represent a cluster. Therefore, a Gaussian Mixture Model tends to group the data points belonging to a single distribution together. GMMs are probabilistic models and use the soft clustering approach for distributing the points in different clusters.
Gaussian distribution or normal distribution has a bell-shaped curve, with the data points symmetrically distributed around the mean value. It runs expectation-maximization algorithm that has E-step and M-step. It runs the E-Step and the M-Step iteratively and maximize the log likelihood function until it converges.

### Process & Result
I have used Gaussian Mixture Model and Expectation-Maximization on two different datasets. Datasets have been obtained from UCI Machine Learnin libray.
1. IRIS dataset
2. Balance Scale dateset

I have created a class, GMM, that has e_step, m_step, loglikelihood, fit functions. In the main class, I have read the data and using GMM class I creted kernel density plots for each features as well as GMM estimation.

#### Density plots for IRIS dataset
1. petal_length
![petal_length](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/petal_length.png)
1. petal_weight
![petal_weight](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/petal_weight.png)
1. sepal_length
![sepal_length](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_length.png)
1. sepal_width
![sepal_width](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_width.png)



