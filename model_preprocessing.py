import pandas as pd
from sklearn.preprocessing import StandardScaler

train_data = pd.read_csv("data/train/temperature_train.csv")
test_data = pd.read_csv("data/test/temperature_test.csv")

scaler = StandardScaler()
train_data[["temperature_scaled"]] = scaler.fit_transform(train_data[["temperature"]])
test_data[["temperature_scaled"]] = scaler.transform(test_data[["temperature"]])

train_data.to_csv("data/train/temperature_train_scaled.csv", index=False)
test_data.to_csv("data/test/temperature_test_scaled.csv", index=False)

print("Предобработка данных завершена!")
