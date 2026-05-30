# %% [markdown]
# Информация о датасете и его подготовка

# %%
import pandas as pd
import sklearn as sk
import os
from random import randint
os.chdir("..")

# %%
Norm = False
dataset = pd.read_csv("data\\StudentPerformanceFactors.csv")
dataset

# %%
dataset.info()

# %%
dataset.describe()

# %%
dataset.isna().sum()

# %%
dataset=dataset.dropna() #в датасете есть немного пропусков, их удаление не критично
dataset.info()


# %%
dataset.describe()

# %%
for i in range(5):
    r  = randint(0,dataset.shape[0])
    res = dataset.iloc[r]
    res["Learning_Disabilities"]= True if res["Learning_Disabilities"]=="Yes" else False
    res["Internet_Access"]= True if res["Internet_Access"]=="Yes" else False
    res.to_json(f"data\\service_validate_{i}.json")
    dataset.drop(index=i,inplace=True)


# %%
cat_features=["Parental_Involvement","Access_to_Resources","Extracurricular_Activities","Motivation_Level","Internet_Access","Family_Income","Teacher_Quality","School_Type","Peer_Influence","Parental_Education_Level","Distance_from_Home","Learning_Disabilities","Gender"]
encoder=sk.preprocessing.OneHotEncoder(handle_unknown="ignore",sparse_output=False)

cats=encoder.fit_transform(dataset[cat_features])
cats_names = encoder.get_feature_names_out()

        
#metrics_to_see=list(metrics_to_see)+list(cats_names)
#i=i.drop(["cat_a","cat_b"],axis=1)
#metrics_to_see.remove('cat_a')
#metrics_to_see.remove('cat_b')
cats_names

# %%
dataset=dataset.drop(cat_features,axis=1)
for j in range(len(cats_names)):
            
    dataset.insert(0, cats_names[j],cats[:,j])



# %%
if Norm:
    for i in dataset.columns:
        dataset[i]=dataset[i]/max(dataset[i])
dataset

# %%
dataset.to_csv("data/StudentPerformanceFactors_prepared.csv",index=False)


