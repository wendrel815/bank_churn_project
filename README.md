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
