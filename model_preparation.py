import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

train_data = pd.read_csv("data/train/temperature_train_scaled.csv")

X_train = train_data[["day"]]
y_train = train_data["temperature_scaled"]

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("Модель обучена и сохранена!")
