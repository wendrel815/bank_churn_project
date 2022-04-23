# bank_churn_project
portfolio project

## files in the directory
- dataset
- requirement file
- bank_churn_final_cycle
- pre-processing experiment file
- pikle file
- api file
- data preparation file

### strategy addressed - cyclic method
- business problem identification
- creation and validation of hypotheses
- data cleaning and attribute engineering if necessary
- feature selection
- testing machine learning models with cross validation
- hyperparameters
- metrics

### main points of the project report
- model in production, which will receive a customer base via API and will return this same “scored” base, that is, an extra column with the probability of each customer churn.

1. What is TopBank's current Churn rate?
2. What is the model's performance in classifying customers as **churns**?
3. What is the expected return, in terms of revenue, if the company uses its model to avoid **churn** from customers?

***features that were removed to improve the performance of the model***

feature selection techniques were used to verify if there is a combination of features that would make the model perform better. the file with the procedure is in the link
- RowNumber,
- CustomerId 
- Surname

***pre-processing techniques used in this process***

*BINARINZING SOME CATEGORICAL COLUMNS*
- Gender
- Geography

### Models used for testing
- KNeighborsClassifier
- DecisionTreeClassifier
- GaussianNB
- LogisticRegression
- GaussianNB
- SGDClassifier
- RandomForestClassifier

### models performance

**TRAINING AND TESTING THE MODEL WITH CROSS VALIDATION TO SEE WHICH IS THE BEST ONE**

KNeighborsClassifier() score: 0.6881203380961249

DecisionTreeClassifier() score: 0.7870822603994517

GaussianNB() score: 0.720647455853267

LogisticRegression() score: 0.6742443638327416

GaussianNB() score: 0.720647455853267

SGDClassifier() score: 0.48517883873816076

RandomForestClassifier() score: 0.858099377082428

![performance graph](https://github.com/wendrel815/bank_churn_project/blob/main/graph%20to%20the%20report/model_performance.png)

### HYPERPARAMETERS

**Hyperparameters were used to try to improve the performance of the model**

BEST PARAMETERS {'criterion': 'entropy', 'max_features': 'auto', 'n_estimators': 300}

### metrics



              precision    recall  f1-score   support

    NO CHURN       0.88      0.85      0.86      1633
       CHURN       0.85      0.87      0.86      1553

    accuracy                           0.86      3186
   macro avg       0.86      0.86      0.86      3186
weighted avg       0.86      0.86      0.86      3186

### API ACCESS
- the API file for classification is in the directory
- it is necessary to run it before sending the data for classification


### MONEY
amount that the bank loses annually with the annual churn of customers with higher-than-average salaries - 31.373,947

amount that the bank loses annually with the annual churn of customers with salaries lower than the average - 7.472,377

amount the bank lost annually from all churn customers - 38.846,324

HOW MUCH WILL THIS DECREASE WITH THE USE OF THE MODEL (5% decrease which is the difference between the model's accuracy and the current % of churn- 1.942,316

HOW MUCH THE BANK WILL CONTINUE TO LOSE WITH THE MODEL - 36.904,008 (STILL STUDYING HOW TO IMPROVE THE MODEL AND REDUCE THIS LOSS)


![ANNUAL LOSS IN MILLIONS](https://github.com/wendrel815/bank_churn_project/blob/main/graph%20to%20the%20report/money.png)

