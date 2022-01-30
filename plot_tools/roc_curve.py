import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc, roc_curve, RocCurveDisplay

model = LogisticRegression()
mode.fit(X_train, y_train)

y_preds = model.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_preds)
auc_output = auc(fpr, tpr)
print('AUC: ', auc_output)
RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=auc_output).plot()
plt.plot([0, 1], [0, 1], 'k--')
plt.show()
