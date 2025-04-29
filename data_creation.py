import numpy as np
import pandas as pd

def generate_temperature_data(days, noise_level=1.0, anomalies=False):
    x = np.arange(days)
    trend = 0.1 * x
    noise = np.random.normal(0, noise_level, days)
    temperature = 20 + trend + noise

    if anomalies and days > 10:
        anomaly_indices = np.random.choice(days, size=3, replace=False)
        temperature[anomaly_indices] += np.random.uniform(5, 10, 3)

    return pd.DataFrame({"day": x, "temperature": temperature})


train_data = generate_temperature_data(100, noise_level=2.0, anomalies=True)
test_data = generate_temperature_data(30, noise_level=1.5)

train_data.to_csv("data/train/temperature_train.csv", index=False)
test_data.to_csv("data/test/temperature_test.csv", index=False)

print("Данные успешно сгенерированы!")
