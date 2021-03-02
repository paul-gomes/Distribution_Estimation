import pandas as pd
import numpy as np
from GMM import *
import matplotlib.pyplot as plt
import scipy.stats as sp
import matplotlib as mpl

def plot_1D(gmm,x,col):
  plt.hist(x,density=True)
  x = np.linspace(x.min(), x.max(), 100, endpoint=False)
  ys = np.zeros_like(x)

  i=0
  for w in gmm.phi:
      y=sp.multivariate_normal.pdf(x, mean=gmm.mean_arr[i], cov=gmm.sigma_arr[i])*w
      plt.plot(x, y)
      ys += y
      i+=1
  plt.xlabel(col)
  plt.plot(x,ys)
  plt.show()
  
def make_ellipses(gmm, ax):
    colors = ['blue', 'green']
    for n, color in enumerate(colors):
        covariances = gmm.sigma_arr[n]
        v, w = np.linalg.eigh(covariances)
        u = w[0] / np.linalg.norm(w[0])
        angle = np.arctan2(u[1], u[0])
        angle = 180 * angle / np.pi  # convert to degrees
        v = 3. * np.sqrt(2.) * np.sqrt(v)
        mean=gmm.mean_arr[n]
        mean=mean.reshape(2,1)
        print(mean)
        ell = mpl.patches.Ellipse(mean, v[0], v[1],
                                  180 + angle, color=color)
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(0.5)
        ax.add_artist(ell)
        ax.set_aspect('equal', 'datalim')
  
def plot_2D(gmm,x,col,label):
    h = plt.subplot(111, aspect='equal')
    make_ellipses(gmm, h)
    plt.scatter(x[:,0],x[:,1],c=label['class'],marker='x')
    plt.xlim(-3, 9)
    plt.ylim(-3, 9)
    plt.xlabel(col[0])
    plt.ylabel(col[1])
    plt.show()

def For_Iris(features,No_Component=2):
    data = pd.read_csv("Data/Iris.data", header = 0)
    data = data.reset_index()
    
    #For one feature
    if (features==1):
        col='petal_width'
        x=data[[col]]
        x=np.array(x)
        gmm = GMM(x,No_Component)
        gmm.fit()
        plot_1D(gmm,x,col)
    else:
        replace_map = {'class': {'Iris-virginica': 1, 'Iris-versicolor': 2,'Iris-setosa':3}}
        data.replace(replace_map, inplace=True)
        label=data[['class']]
        col=['petal_width','sepal_width']
        x=data[col]
        x=np.array(x)
        gmm = GMM(x,No_Component)
        gmm.fit()
        plot_2D(gmm,x,col,label) 

def For_BalanceScale(features):
    data = pd.read_csv("Data/balance-scale.data", header = 0)
    if(features==1):
        col='right_weight'
        x=data[[col]]
        x=np.array(x)
        gmm = GMM(x,2)
        gmm.fit()
        plot_1D(gmm,x,col)
    else:
        replace_map = {'class' : {'L':1, 'B':2, 'R':3}}
        data.replace(replace_map, inplace=True)
        label=data[['class']]
        col=['left_distance','right_distance']
        x=data[col]
        x=np.array(x)
        gmm = GMM(x,2)
        gmm.fit()
        plot_2D(gmm,x,col,label) 
        
def main():
  #For_Iris(2,2)
  For_BalanceScale(2)
  
if __name__== "__main__":
  main()


