import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_Xy_in_2d_space(X, y, title='Classes'):   
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)
    colors = ['#1F77B4', '#FF7F0E']
    markers = ['o', 's']
    for l, c, m in zip(np.unique(y), colors, markers):
        plt.scatter(
            X[y==l, 0],
            X[y==l, 1],
            c=c, label=l, marker=m
        )
    plt.title(title)
    plt.legend(loc='upper right')
    plt.show()
