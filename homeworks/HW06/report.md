# HW06 – Report

> Файл: `homeworks/HW06/report.md`  
> Важно: не меняйте названия разделов (заголовков). Заполняйте текстом и/или вставляйте результаты.

## 1. Dataset

- Какой датасет выбран: `S06-hw-dataset-01.csv`
- Размер: (12000, 30)
- Целевая переменная: `target`
    - 0  -  0.676583
    - 1  - 0.323417
- Признаки: числовые float64

## 2. Protocol

- Разбиение: test_size=0.25, random_state=42
- Подбор: CV на train по ROC-AUC
- Метрики: accuracy, F1, ROC-AUC уместны потому что задача классификации
 
## 3. Models

"LogReg(scaled)": {
    "best_params": {
      "lr__C": 10.0,
      "lr__penalty": "l2",
      "lr__solver": "lbfgs"
    },
    "best_cv_roc_auc": 0.8822238806908922
  },
  "DecisionTree": {
    "best_params": {
      "ccp_alpha": 0.0,
      "max_depth": null,
      "min_samples_leaf": 20
    },
    "best_cv_roc_auc": 0.9112358432907914
  },
  "RandomForest": {
    "best_params": {
      "max_depth": null,
      "max_features": "sqrt",
      "min_samples_leaf": 1
    },
    "best_cv_roc_auc": 0.9684465802433795
  },
  "HistGradientBoosting": {
    "best_params": {
      "learning_rate": 0.1,
      "max_depth": null,
      "max_leaf_nodes": 63
    },
    "best_cv_roc_auc": 0.9719880531240899
  }


## 4. Results

|	| accuracy |f1 |	roc_auc	|model|
|--|--|--|--|--|
|0|0.562333|	0.325629|	0.500840|	Dummy(most_frequent)|
|1|0.829667|	0.714685|	0.878905|	LogReg(scaled)|
|2|0.863333|	0.784890|	0.910533|	DecisionTree|
|3|0.934667|	0.894283|	0.970610|	RandomForest|
|4|0.936333|	0.898242|	0.974682|	HistGradientBoosting|


## 5. Analysis

- Устойчивость: что будет, если поменять `random_state` (хотя бы 5 прогонов для 1-2 моделей) – кратко
- Ошибки: confusion matrix для лучшей модели + комментарий
- Интерпретация: permutation importance (top-10/15) + выводы
![img](artifacts/figures/permutation.png)
## 6. Conclusion
Bagging деревьевья дают лучший результат, но требуют больше ресурсов для обучения.
Оценивать важность признаков - хорошая практика.
