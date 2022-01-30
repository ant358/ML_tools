import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, classes, normalize=None):
    """Plots a confusion matrix. using seaborn

    Args:
        y_true (numpy array): the true class labels
        y_pred (numpy array): the predicted class labels
        classes (list): the class labels
        normalize must be one of {'true', 'pred', 'all', None}
    """
    # check the format of the y_true and y_pred
    if len(y_true.shape) > 1:
        y_true = np.argmax(y_true, axis=1)
    if len(y_pred.shape) > 1:
        y_pred = np.argmax(y_pred, axis=1)
    # plot the confusion matrix
    plt.figure(figsize=(10, 7))
    data = confusion_matrix(y_true, y_pred, normalize=normalize)
    df_cm = pd.DataFrame(data, columns=classes, index=classes)
    df_cm.index.name = 'Actual'
    df_cm.columns.name = 'Predicted'
    sns.set(font_scale=1.4)
    sns.heatmap(df_cm, cmap="Blues", annot=True, annot_kws={"size": 16}, fmt='g')
    plt.title('Confusion Matrix')
    # set the number format
    plt.show()
    # return df_cm
