# %%
import pandas as pd
import sklearn as sk
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
import math
import matplotlib.pyplot as plt
import myConfig
os.chdir(myConfig.absPath)
import numpy as np
def regression_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """
    Вычисляет три основные метрики для регрессии:
    - MAE (Mean Absolute Error): средняя абсолютная ошибка в исходном масштабе
    - RMSE (Root Mean Squared Error): корень из среднеквадратичной ошибки
    - MAPE (Mean Absolute Percentage Error): средняя абсолютная процентная ошибка (%)
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / np.clip(np.abs(y_true), 1e-8, None))) * 100
    return {"MAE": mae, "RMSE": rmse, "MAPE": mape}


# %%
dataset = pd.read_csv("data\\StudentPerformanceFactors_prepared.csv")
dataset

# %%
features = dataset.columns.to_list()
features.remove("Exam_Score")
X_train, X_test, y_train, y_test = train_test_split(dataset[features], dataset["Exam_Score"], test_size=0.3, random_state=myConfig.random_state)



# %%
baseline = LinearRegression()
baseline.fit(X_train,y_train)
baseline.score(X_test,y_test)


# %%
y_pred = baseline.predict(X_test)
regression_metrics(y_test,y_pred)

# %%
y_test

# %%
y_pred

# %%
baseline.coef_

# %%
plt.plot(y_pred,y_test,"o")
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.xlim((0,100))
plt.ylim((0,100))
plt.plot((0,100),(0,100))
plt.show()

# %%
import pickle
pickle.dump(baseline, open("artifacts\\regression.sav", 'wb'))


