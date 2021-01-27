from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np 
import matplotlib as plt

def feature_importance(df, target, reg=False):
    """Genreric Random Forest For Feature Ranking  
    Designed for the early stages of model building 
    so it takes the df with the target 
    rather than an array
    
    if reg = True use the Regression Version
    else use the classifier
    
    Parameters
    ----------
    df : pandas dataframe
    
    target : str, the tilte of the target data column in the dataframe
    
    reg = False, regressor or classifier
  
    Returns
    -------
    None
    Prints a dataframe of ranked features.
    and
    Prints a barchart of the feature importance
    """

    # create the target to predict
    y_train = df[target]
    X_train = df.drop([target], axis=1)
    # Create a random forest model
    if reg = True:
        clf = RandomForestRegressor(n_estimators=100, random_state=0, n_jobs=-1)
    else:
        clf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
        
    # Train the model
    clf.fit(X_train, y_train)
    
    # collect the feature labels
    feat_labels = list(X_train.columns)
    feat_importance = list(clf.feature_importances_)
    # get the standard deviation
    std = list(np.std([tree.feature_importances_ for tree in clf.estimators_],
                 axis=0))
    # create the output table
    features_df = pd.DataFrame({'features': feat_labels, 'importance': feat_importance, 'std': std} )
    features_df.sort_values('importance', inplace=True, ascending=False)
    print(features_df.head(10))
    # create the output graph
    plt.figure(figsize=(8,5))
    plt.bar(x='features', height='importance',
            data=features_df, yerr='std')
    # plt.ylim(-0.1, 0.5)
    plt.ylabel('Metric Importance')
    plt.grid(b=1, axis='y')
    plt.title(f'The Importance of Features that predict {target}')
    plt.xticks(rotation=90)
    plt.show()
    
    # unquote to return the df
    # return features_df
    
