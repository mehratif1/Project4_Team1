# Credit Risk Prediction



## Overview
This project aims to predict the likelihood of clients facing difficulty in repaying loans. The dataset includes features such as external sources, loan amounts, and client demographics.


## Data Source

https://www.kaggle.com/competitions/home-credit-default-risk/data

- The dataset is loaded from the "application_train.csv" file.
- Selected columns: ['EXT_SOURCE_3', 'EXT_SOURCE_2', 'EXT_SOURCE_1', 'AMT_ANNUITY', 'DAYS_ID_PUBLISH', 'DAYS_BIRTH', 'DAYS_LAST_PHONE_CHANGE', 'DAYS_REGISTRATION', 'DAYS_EMPLOYED', 'AMT_CREDIT', 'AMT_GOODS_PRICE', 'TARGET'].


## Dependencies
- pandas
- lightgbm
- scikit-learn
- LabelEncoder
- Flask
- Pipeline
- Tableau
- Matplotlib
- Seabone
- Html
- joblib
- RandomForestClassifier
- KFold
- SMOTE


## Data Preprocessing
- Handling missing values: Imputed missing values in 'EXT_SOURCE_3', 'EXT_SOURCE_2', 'EXT_SOURCE_1', 'AMT_ANNUITY', 'AMT_GOODS_PRICE' using median values.
- Balancing the target classes by undersampling the majority class.

## Exploratory Data Analysis
- Visualized the distribution of target classes before and after undersampling.

![alt text](Images/Undersampling.png)

## Model Training
- Used LightGBM classifier with specified hyperparameters for training.

![alt text](Images/Lightgbm.png)

## Evaluation
- Utilized metrics such as precision, recall, and classification report to evaluate the model on the test set.

![alt text](Images/classification_report.png)

- Visualized the confusion matrix using a heatmap.

![alt text](Images/confusion_matrix.png)

## Tableau Visualizations


- Tableau was used to create visualizations for a more comprehensive understanding of the dataset.

### Visualizations
1. **Age Group Analysis:**
   - Bar chart displaying the distribution of clients facing difficulty in loan repayment across different age groups.

2. **Time Series Analysis:**
   - Line chart depicting trends in loan repayment difficulties over the years.

![alt text](Images/Tableau_trends_analysis.png)


3. **External Sources Analysis:**
   - Bar charts illustrating the impact of external sources (1, 2, 3) on the likelihood of loan repayment difficulties.
   
![alt text](Images/Tableau_External_sources.png)



### How to Access
- To explore detailed visualizations, you can view the Tableau workbook here [Explore Tableau Visualizations](https://public.tableau.com/app/profile/mehr.atif/viz/Credit_Risk_Project_17074485866060/Story1?publish=yes)

### Insights
- These visualizations provide additional insights into the factors influencing loan repayment, enhancing the understanding gained from the model evaluation.

## Model Deployment with Flask and HTML
This repository contains the deployment code for our machine learning model using Flask and HTML. The deployed model predicts if the clients will have difficulties in loan repayment or not after taking in input into the form.

![alt text](<Images/Web_form1 (1).png>)

![alt text](Images/WEb_form2.png)

## Collaborators: 
## Mehr Atif 
## Daria Riechkina
## Megha Rani
