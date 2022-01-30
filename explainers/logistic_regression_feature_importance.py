import pandas as pd
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# create a dataframe to hold the scores
feature_importance = pd.DataFrame(model.coef_[0], X_train.columns, columns=['coef'])
# add the scores to the dataframe
feature_importance['score'] = feature_importance.iloc[:,0].abs()
# sort the dataframe by the score
feature_importance = feature_importance.sort_values(by='score', ascending=False)
# the top 10 features
print(feature_importance.head(10))

# plot the scores - flip the dataframe as barh always plots the wrong way round
feature_importance.sort_values(by='score',
                               ascending=True).score.plot(kind='barh',
                                                          legend=False,
                                                          figsize=(6, 10)
                                                          title='Feature Importance Absoulte Score\n')
# or
# plot the scores - flip the dataframe as barh always plots the wrong way round
feature_importance.sort_values(by='score',
                               ascending=True).coef.plot(kind='barh',
                                                          legend=False,
                                                          figsize=(6, 10),
                                                          title='Feature Importance and Direction of Effect\n')
