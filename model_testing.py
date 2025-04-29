import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

test_data = pd.read_csv("data/test/temperature_test_scaled.csv")
model = joblib.load("model.pkl")

X_test = test_data[["day"]]
y_test = test_data["temperature_scaled"]
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")
