# Project 1 - Distribution estimation

### Gaussian Mixture Model (GMM)

GMMs assume that there are a certain number of Gaussian distributions, and each of these distributions represent a cluster. Therefore, a Gaussian Mixture Model tends to group the data points belonging to a single distribution together. GMMs are probabilistic models and use the soft clustering approach for distributing the points in different clusters.
Gaussian distribution or normal distribution has a bell-shaped curve, with the data points symmetrically distributed around the mean value. It runs expectation-maximization algorithm that has E-step and M-step. It runs the E-Step and the M-Step iteratively and maximize the log likelihood function until it converges.

### Process & Result
I have used Gaussian Mixture Model and Expectation-Maximization on two different datasets. Datasets have been obtained from UCI Machine Learnin libray.
1. IRIS dataset
2. Balance Scale dateset

I have created a class, GMM, that has e_step, m_step, loglikelihood, fit functions. In the main class, I have read the data and using GMM class I created kernel density plots for each features as well as GMM estimation for multiple features.

#### Density plots for IRIS dataset
![petal_length](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/petal_length.png)
![petal_weight](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/petal_width.png)
![sepal_length](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_length.png)
![sepal_width](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_width.png)
#### GMM Estimation for Two Features
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/petal_widthVSpetal_length.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_lengthVSpetal_length.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_widthVSpetal_width.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/sepal_widthVSsepal_length.png)

#### Density plots for Balance Scale dataset
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/left_distance.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/left_weight.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/right_distance.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/right_weight.png)
#### GMM Estimation for Two Features
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/left_distanceVSleft_weight.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/right_distanceVSleft_distance.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/right_distanceVSright_weight.png)
![](https://github.com/paul-gomes/Distribution_Estimation/blob/main/Image/right_weightVSleft_weight.png)


### References
1. [expectation_maximization_and_gaussian_mixture_models](https://www.python-course.eu/expectation_maximization_and_gaussian_mixture_models.php)
1. [gaussian-mixture-models-clustering](https://www.analyticsvidhya.com/blog/2019/10/gaussian-mixture-models-clustering/)
1. [Exploration of IRIS Dataset](http://rstudio-pubs-static.s3.amazonaws.com/324830_8985f6dac8d34633b6cf23a92ff3e64c.html)
1. [Gaussian-Mixture-Model](https://github.com/sohaib730/Gaussian-Mixture-Model)
2. [distributions](https://www.kaggle.com/alexisbcook/distributions)
