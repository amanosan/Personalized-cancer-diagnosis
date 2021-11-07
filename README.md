# Personalized Cancer Diagnosis

## 1. Business Problem

### 1.1 Description
Source: https://www.kaggle.com/c/msk-redefining-cancer-treatment/
***Note: Please download the data from the above link and store it in `data/` directory.***

### 1.2 Problem Statement
Classifiy the given genetic variations/mutations based on evidence from text-based clinical literature.

### 1.3 Business Objectives and Constraints
- No low-latency requirements.
- Interpretability is important.
- Errors can be very costly.
- Probability of a data point belonging to each class is needed.

***

## 2. EDA
Exploratory Data Analysis of the data and univariate analysis of all the features has been performed and the results as well as the procedure can be found in the  `EDA.ipynb` notebook.

***

## 3. Machine Learning

### 3.1 Data Overview
- The data is divided into two sets:
    1. Text - Located in the directory `data\training_text.zip`
    2. Variants - Located in the directory `data\training_variants.zip`
- The two sets were joined into one and is present as `data\train_data.csv`

### 3.2 Data Preprocessing
Data Preprocessing has been done in the `DataPreprocessing.ipynb` notebook.

Following steps were done to clean the data:
- Special Characters were removed from the text
- Multiple spaces were replaced with single space
- Text was converted to lower case
- Stopwords were removed

Null values were not removed but were replaced by their respective 'Gene' and 'Variation' features values.

### 3.3 Type of Machine Learning Problem
This is a multi-class classification problem where we need to predict using the text the class.

### 3.4 Performance Metrics
- Log-Loss was used to evaluate the performance of the model.
- Confusion Matrix was also used to identify how the model performed.
  
### 3.5 Modelling
Featurization of the text is done with the help of `CountVectorizer`
- Multinomial Naive Bayes - baseline model
- Logistic Regression - SGD with "log" loss.
- Support Vector Machines - SGD with "hinge" loss.

Ensebmle Techniques used:
- Random Forest.
- Stacking Classifier with *Logistic Regression*, *Support Vector Machines* and *Naive Bayes* as the models
- Majority Voting Classifier with the same models as Stacking Classifier.

***The Best performance was achieved by Logistic Regression - SGD with logloss and balanced class weights with a log loss value on Test Set = `1.170`***

***Followed by Majority Voting Classifier with Logistic Regression, SVM and Multinomial Naive Bayes as the estimators with a log loss on Test Set = `1.2214`***

**The Results of the other models including Logistic Regression can be found in the ***ML_Modelling_1.ipynb*** Notebook.**

***
## Future Improvements
- Can include both unigrams and bigrams in CountVectorizer.
- Can use TF-IDF instead of CountVectorizer.
- Can use Deep Learning models (LSTMs and GRUs) with word embeddings. 
