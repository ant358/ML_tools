import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer

# binary classification example edit to suit other stuff
scaler_results_df = pd.DataFrame()
i = 0
for scaler in [MinMaxScaler(), MaxAbsScaler(), StandardScaler(), RobustScaler(), Normalizer(), QuantileTransformer(), PowerTransformer()]:
    # scale the data
    sc = scaler
    print(sc.__class__.__name__)
    scaler_results_df.loc[i, 'scaler'] = sc.__class__.__name__
    X = sc.fit_transform(X)
    # split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=True, stratify=y)

    # Start with a basic model - adjust layers depending on data
    model_1 = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    # compile the model
    model_1.compile(optimizer="rmsprop", 
                    loss="binary_crossentropy", 
                    metrics=["accuracy"])
    # train the model
    history = model_1.fit(
        X_train, y_train, 
        epochs=30, 
        batch_size=512, 
        validation_data=(X_test, y_test),
        verbose=0
    )
    # evaluate the model
    ev = model_1.evaluate(X_test, y_test)
    scaler_results_df.loc[i, 'loss'] = ev[0]
    scaler_results_df.loc[i, 'accuracy'] = ev[1]
    # generate roc data
    y_pred = model_1.predict(X_test).ravel()
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    # generate the auc data
    auc_output = auc(fpr, tpr)
    scaler_results_df.loc[i, 'auc'] = auc_output
    cm = confusion_matrix(y_test, y_pred.round())
    scaler_results_df.loc[i, 'True Positive'] = cm[1][1]
    scaler_results_df.loc[i, 'False Positive'] = cm[0][1]
    scaler_results_df.loc[i, 'True Negative'] = cm[0][0]
    scaler_results_df.loc[i, 'False Negative'] = cm[1][0]
    i += 1
    
print(scaler_results_df)
