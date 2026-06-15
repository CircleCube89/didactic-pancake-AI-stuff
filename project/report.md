# Отчёт по итоговому проекту по курсу «Инженерия Искусственного Интеллекта»

---

## 1. Постановка задачи и контекст

1. **Предметная область и задача:**
   - Задача регрессия. Необходимо по данным о студенте и его подготовке предугадать оценку на экзамене.

2. **Формулировку задачи в терминах ML/ИИ:**
   - какие есть входные данные;
   - что является целевой переменной / выходом модели;
   - какие ограничения/требования есть (скорость, интерпретируемость, точность и т.п.).

3. **Целевые метрики качества:**
   - MAE (Mean Absolute Error): средняя абсолютная ошибка в исходном масштабе
   - RMSE (Root Mean Squared Error): корень из среднеквадратичной ошибки
   - MAPE (Mean Absolute Percentage Error): средняя абсолютная процентная ошибка (%)

---

## 2. Данные

1. **Источник данных:**
   - открытый датасет [(ссылка на источник);](https://www.kaggle.com/datasets/itszubi/students-academic-performance-dataset)
  
2. **Структура данных:**
   - таблица
   - файл:`data/StudentPerformanceFactors.csv`

   ``` Plain text
      RangeIndex: 6607 entries, 0 to 6606
   Data columns (total 20 columns):
    #   Column                      Non-Null Count  Dtype
   ---  ------                      --------------  -----
    0   Hours_Studied               6607 non-null   int64
    1   Attendance                  6607 non-null   int64
    2   Parental_Involvement        6607 non-null   str  
    3   Access_to_Resources         6607 non-null   str  
    4   Extracurricular_Activities  6607 non-null   str  
    5   Sleep_Hours                 6607 non-null   int64
    6   Previous_Scores             6607 non-null   int64
    7   Motivation_Level            6607 non-null   str  
    8   Internet_Access             6607 non-null   str  
    9   Tutoring_Sessions           6607 non-null   int64
    10  Family_Income               6607 non-null   str  
    11  Teacher_Quality             6529 non-null   str  
    12  School_Type                 6607 non-null   str  
    13  Peer_Influence              6607 non-null   str  
    14  Physical_Activity           6607 non-null   int64
    15  Learning_Disabilities       6607 non-null   str  
    16  Parental_Education_Level    6517 non-null   str  
    17  Distance_from_Home          6540 non-null   str  
    18  Gender                      6607 non-null   str  
    19  Exam_Score                  6607 non-null   int64
   dtypes: int64(7), str(13)
   memory usage: 1.0 MB
   ```

3. **Предобработка и EDA:**
   - В данных присуиствует некоторое количество пропусков. Их относительное количество небольшое (~4.5 %), поэтому допустимо удалить строки с пропусками.
   - Категориальные признаки разнесены в отдельные столбцы.
   - 5 строк удалены из общего датасета и сохранены в json для ручной проверки сервиса.(См. `data/service_validate_*.json`)
См. `notebooks/eda.ipynb` и `data/StudentPerformanceFactors_prepared.csv`

---

## 3. Модели и подходы

1. **Базовые (baseline) модели:**
   В качестве baseline используется линейная регрессия.
   См. `notebooks/baseline.ipynb`
2. **Улучшенные модели и эксперименты:**
   - Была исследована возможность использования простых нейросетевых моделей в `noteboks/model_experiments.ipynb` и `notebooks/model_experiments2.ipynb`.
   - Нормирование числовых признаков не улучшило качество результатов, поэтому не использутся.

---

## 4. Экспериментальный протокол и результаты

1. **Экспериментальный протокол:**
   - Для проверки работы сервиса из общего датасета исключены 5 строк и записаны в `data/service_validate_*.json` в формате запроса.
   - train/val:70/30
   - В дальнейшем test и validation совпадают.

2. **Сравнение моделей по метрикам:**

   Пример таблицы (адаптируйте под свои метрики):

   | Модель / конфигурация         | Описание                             | MAE       | RMSE      | MAPE      |
   |-------------------------------|--------------------------------------|-----------|-----------|-----------|
   | Baseline                      | LinearRegression                     | 0.48      | 2.01      | 0.66      |
   | Model A                       | Простая нейронная сеть               | 0.75      | 2.15      | 5.96      |
   | Model B                       | Больше слоев и нейронов              | 0.82      | 2.18      | 5.92      |

3. **Выбор финальной модели:**
  Из экспериментов (`noteboks/model_experiments.ipynb` , `noteboks/model_experiments2.ipynb` и `noteboks/baseline_training.ipynb`) следует, что усложненние модели не увеличивает её точность, соответственно нерационально использовать полноценную нейронную сеть в сервисе по соотношению результат/количество вычислений.

---

## 5. Архитектура решения и сервис

1. **Архитектура пайплайна:**
   - `notebooks/eda.ipynb`  - EDA и разбиение по столбцам.
   - `notebooks/baseline_training.ipynb` - обучение регрессии и сохранение результатов в `artifacts/regression.sav`.
   - `src/api.py` - сервис.

   Сервис:
      Запрос -> Преобразование в формат модели -> Обработка -> Результат

2. **API и endpoints:**
   - endpoints:
      - `/health`
      - `/predict`
   - Примеры
      - Запрос `/predict`:

          ``` json
   
         {
            "Hours_Studied": 23,
            "Attendance": 84,
            "Parental_Involvement": "Low",
            "Access_to_Resources": "High",
            "Extracurricular_Activities": false,
            "Sleep_Hours": 7,
            "Previous_Scores": 73,
            "Motivation_Level": "Low",
            "Internet_Access": true,
            "Tutoring_Sessions": 0,
            "Family_Income": "Low",
            "Teacher_Quality": "Medium",
            "School_Type": "Public",
            "Peer_Influence": "Positive",
            "Physical_Activity": 3,
            "Learning_Disabilities": false,
            "Parental_Education_Level": "High School",
            "Distance_from_Home": "Near",
            "Gender": "Male"
         }
   
          ```

      - Ответ `/predict`:

         ```json

         {
            "exam_score": 67.02956074545699
         }

         ```

      - Ответ `/health`:

      ```json
         {
           "status": "ok",
           "weigts_file": "artifacts/regression.sav",
           "version": "0.2.0"
         }
      ```

3. **Технологический стек:**
   - Сервис работает на FastAPI
   - Для линейной регрессии используется sklearn.

---

## 6. Наблюдаемость, конфигурация и безопасность

- Используются логи в консоль FastAPI.

- При обращении к `/health` ответ должен совпадать с примером.

- Для того, чтобы код в различных частях проекта имел стабильный доступ ко всем файлам проекта, задаются абсолютные (относительные использовать неудобно/возникают ошибки) пути скриптом `configure.py` в файлах `myConfig.py`. Перед первым запуском и при прермещении папки проекта нужно выполнять `configure.py`. Очистка выполняется `unconfigure.py` Других секретов/ключей в проекте нет.

---

## 7. Ограничения и дальнейшая работа

- Линейная регрессия слишком хорошо предсказывает ответ, возможно данные синтетические (явно в источнике это не указанно).

- Оптимизация проекта: уменьшение числа зависимостей  и общего размера сервиса.

---

## 8. Сценарий демонстрации на защите

1. Кратко покажу структуру проекта (`notebooks/`, `src/`, `data/`).
2. Запущу сервис по инструкции из `project/README.md`, покажу пару запросов через Swagger UI.
3. Покажу ноутбук с основными экспериментами и сравнение моделей по метрике качества.

---
