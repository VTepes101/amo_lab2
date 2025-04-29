#!/bin/bash

echo "Запуск конвейера машинного обучения..."

# 1. Генерация данных
echo "Шаг 1: Генерация данных..."
python3 data_creation.py

# 2. Предобработка данных
echo "Шаг 2: Предобработка данных..."
python3 model_preprocessing.py

# 3. Обучение модели
echo "Шаг 3: Обучение модели..."
python3 model_preparation.py

# 4. Тестирование модели
echo "Шаг 4: Тестирование модели..."
python3 model_testing.py

echo "Конвейер успешно завершен!"