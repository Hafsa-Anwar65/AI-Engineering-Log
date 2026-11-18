# 📝 Week 3 · Classic Machine Learning with scikit-learn

> My notes, in my own words. One section per day.

**Days this week:**
[Day 15](#-day-15--week-2-review--first-look-at-scikit-learn) ·
[Day 16](#-day-16--supervised-vs-unsupervised-splits--data-leakage) ·
[Day 17](#-day-17--logistic-regression--decision-trees) ·
[Day 18](#-day-18--random-forests--gradient-boosting) ·
Day 19 · Day 20 · Day 21

---

## 📅 Day 15 · Week 2 Review + First Look at scikit-learn

**Date:** Nov 15, 2026
**Code:** [`Day 15 - Week 2 Review and First Look at scikit-learn.py`](./Day%2015%20-%20Week%202%20Review%20and%20First%20Look%20at%20scikit-learn.py)

### 1. Week 2 Self-Check

I turned Week 2's main ideas into `assert` statements. If the file runs without an error, I still remember them.

| Idea | Check |
|---|---|
| Shapes & axis | `a.mean(axis=0)` gives one value per **column** |
| Broadcasting | A row vector is added to every row |
| A layer | `W @ x + b` |
| pandas | `groupby("city")["sales"].sum()` |
| Gradient descent | 100 steps on `(w - 3)²` lands on `w = 3` |

### 2. Exploring a Real Dataset (EDA)

**EDA (Exploratory Data Analysis)** = getting to know the data **before** building any model.

#### My EDA checklist

| Question | Code | Breast cancer answer |
|---|---|---|
| How big is it? | `df.shape` | 569 rows, 30 features |
| Anything missing? | `df.isna().sum()` | 0 missing |
| Are classes balanced? | `value_counts(normalize=True)` | 63% benign, 37% malignant |
| What do the numbers look like? | `df.describe()` | Very different scales (radius ~14, area ~650) |
| Which features matter? | `groupby` means, `.corr()` | `worst concave points` (0.79) |

![Mean radius by diagnosis](./day15_radius_hist.png)

> 💡 Different scales (radius vs area) are why **feature scaling** matters, just like in my Day 14 project.

### 3. The scikit-learn Pattern

Every model in scikit-learn works the same way:

```python
model = LinearRegression()      # 1. create
model.fit(X, y)                 # 2. learn
model.predict(X_new)            # 3. predict
model.score(X, y)               # 4. evaluate
```

| Term | Meaning |
|---|---|
| `X` | Features: a 2D table, one row per example |
| `y` | Target: the answer I want to predict |
| Estimator | Any model with `.fit()` |

> ✅ scikit-learn's `LinearRegression` gave **exactly the same weights** as solving it myself with NumPy (`np.linalg.lstsq`), so the Week 2 maths is what runs underneath.

---

## 📅 Day 16 · Supervised vs Unsupervised, Splits & Data Leakage

**Date:** Nov 16, 2026
**Code:** [`Day 16 - Supervised vs Unsupervised and Data Leakage.py`](./Day%2016%20-%20Supervised%20vs%20Unsupervised%20and%20Data%20Leakage.py)

### 1. Types of Machine Learning

| Type | Has the answers? | Goal | Example today | Result |
|---|:-:|---|---|---|
| **Supervised: classification** | ✅ | Predict a **category** | Benign or malignant | 98.2% accuracy |
| **Supervised: regression** | ✅ | Predict a **number** | Diabetes progression | MAE 42.8 points |
| **Unsupervised: clustering** | ❌ | Find groups by itself | Iris flowers | Matched species 0.73 (ARI) |

> 💡 KMeans never saw the species labels, yet its 3 groups matched the real species quite well.

### 2. Train / Validation / Test

| Set | Share | Used for |
|---|:-:|---|
| **Train** | 60% | The model learns from it |
| **Validation** | 20% | I compare settings and choose the best |
| **Test** | 20% | Final score, looked at **only once** |

```python
# 1. Cut off the test set first
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
# 2. Split the rest into train and validation (0.25 of 80% = 20%)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, stratify=y_temp)
```

- **`stratify=y`** keeps the same benign/malignant share in every set (0.63 / 0.62 / 0.63).
- **`random_state`** makes the split the same every run.

#### Choosing a setting with validation

| C | Validation accuracy |
|:-:|:-:|
| 0.001 | 0.851 |
| 0.01 | 0.939 |
| 0.1 | 0.974 |
| **1** | **0.991** ✅ |
| 10 | 0.965 |

Picked `C=1`, retrained on train + validation, then tested once: **0.982**.

> ⚠️ If I choose settings by looking at the **test** score, the test set stops being a fair final exam.

### 3. Data Leakage

**Leakage** = information from outside the training data sneaks into training, so the score looks better than the model really is.

#### Example 1: preparing data before splitting

On **pure random noise** (the honest answer is a coin flip, about 50%):

| Method | Accuracy |
|---|:-:|
| ❌ Pick best features using **all** data, then cross-validate | **0.87** (a lie) |
| ✅ Feature selection **inside a Pipeline** | **0.48** (the truth) |

```python
model = make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression())
cross_val_score(model, X, y, cv=5)    # each step only sees the training folds
```

#### Example 2: a feature that contains the answer

I added a fake "second opinion result" column, which is only known **after** the diagnosis:

| Features | Accuracy |
|---|:-:|
| With the leaky column | 1.000 |
| Without it | 0.982 |

#### How to avoid leakage

- Split **first**, then scale, select features or fill missing values.
- Put every preprocessing step in a **`Pipeline`**.
- Ask for every feature: *"Would I know this at prediction time?"*
- Treat a near-perfect score as a **warning sign**, not a win.

---

## 📅 Day 17 · Logistic Regression & Decision Trees

**Date:** Nov 17, 2026
**Code:** [`Day 17 - Logistic Regression and Decision Trees.py`](./Day%2017%20-%20Logistic%20Regression%20and%20Decision%20Trees.py)

### 1. Logistic Regression

Despite the name, it's a **classification** model. It works like linear regression, then squeezes the result into a probability with the **sigmoid**:

```text
probability = sigmoid(w · x + b)        sigmoid(z) = 1 / (1 + e^-z)
```

| z | sigmoid(z) |
|:-:|:-:|
| -5 | 0.007 |
| 0 | 0.500 |
| 5 | 0.993 |

- `predict_proba()` gives the probability; `predict()` uses a 0.5 cut-off.
- **Coefficients** show which features push towards each class (after scaling).
- Result: **98.2%** test accuracy on breast cancer data.

### 2. Decision Trees

A flowchart of yes/no questions the model learns from the data:

```text
worst radius <= 16.8?
├── yes → worst concave points <= 0.14? → benign / malignant
└── no  → texture error <= 0.47?        → benign / malignant
```

#### Depth controls overfitting

| max_depth | Train | Test |
|:-:|:-:|:-:|
| 1 | 0.923 | 0.921 |
| **3** | 0.976 | **0.939** |
| 5 | 0.993 | 0.921 |
| None | **1.000** | 0.912 |

> ⚠️ 100% on train but worse on test = **overfitting**: the tree memorised the training data.

### 3. Logistic Regression vs Decision Tree

| | Logistic regression | Decision tree |
|---|---|---|
| Shape of the boundary | Straight line / plane | Boxes (step-like) |
| Needs scaling | ✅ Yes | ❌ No |
| Easy to explain | Coefficients | Readable yes/no rules |
| Risk | Underfits curved patterns | Overfits when deep |

### 4. Classification Report

| Metric | Question it answers |
|---|---|
| **Precision** | Of the ones I said were malignant, how many really were? |
| **Recall** | Of all the real malignant ones, how many did I catch? |
| **F1** | One number balancing precision and recall |
| **Support** | How many real examples of that class |

### 5. Text with TF-IDF

**TF-IDF** turns text into numbers: a word scores high if it's common in **this** message but rare across **all** messages.

```python
spam_model = make_pipeline(TfidfVectorizer(), LogisticRegression())
```

My mini spam detector learned that **free, now, won, selected** point to spam.

### 🛠️ What I Built

| Part | What it does |
|---|---|
| Sigmoid demo | Shows how scores become probabilities |
| Cancer classifier | Logistic regression with probabilities and feature importance |
| Tree depth experiment | Shows overfitting as depth grows |
| Spam detector | TF-IDF + logistic regression on 12 messages |

---

## 📅 Day 18 · Random Forests & Gradient Boosting

**Date:** Nov 18, 2026
**Code:** [`Day 18 - Random Forests and Gradient Boosting.py`](./Day%2018%20-%20Random%20Forests%20and%20Gradient%20Boosting.py)

### 1. Why One Tree Isn't Enough

Training trees on slightly different samples of the same data gave different first questions and different scores (0.912 to 0.930). A single tree is **unstable** (high variance).

### 2. Ensembles: Many Models Together

| | **Bagging** (Random Forest) | **Boosting** (Gradient Boosting) |
|---|---|---|
| How trees are built | **In parallel**, independently | **One after another** |
| Each tree learns from | A random sample of rows (bootstrap) + random features | The **mistakes** of the trees before it |
| Final answer | Majority vote | Sum of all trees' small corrections |
| Mainly fixes | Variance (overfitting) | Bias (underfitting) |
| Famous versions | `RandomForestClassifier` | `GradientBoosting`, **XGBoost**, LightGBM |

#### Bagging by hand

| | Accuracy |
|---|:-:|
| Average single tree | 0.908 |
| 25 trees voting | **0.939** |

### 3. Model Comparison (5-fold cross-validation)

| Model | Mean accuracy | Std |
|---|:-:|:-:|
| Decision tree | 0.917 | 0.024 |
| Random forest | 0.958 | 0.024 |
| Gradient boosting | 0.963 | 0.021 |
| **Hist gradient boosting** | **0.965** | **0.018** |

> 💡 **Cross-validation** trains and tests 5 times on different splits, so the score doesn't depend on one lucky split.

### 4. Random Forest Details

- **More trees** = more stable (results settled around 50 trees).
- **Out-of-bag (OOB) score:** each tree skips about a third of the rows, which works as free validation. OOB = **0.960**.
- **Feature importance:** `worst perimeter`, `worst area`, `worst concave points` mattered most.

### 5. Gradient Boosting: Learning Rate

| learning_rate | After 10 trees | After 100 trees |
|:-:|:-:|:-:|
| 0.01 | 0.632 | 0.921 |
| 0.1 | 0.930 | 0.956 |
| 1.0 | 0.947 | 0.956 |

Small learning rate = slow but careful (needs more trees). Too big = can overshoot and overfit.

### 6. Multi-class: Wine (3 classes)

| Model | Accuracy |
|---|:-:|
| Decision tree | 0.865 |
| **Random forest** | **0.967** |
| Hist gradient boosting | 0.955 |

### 🛠️ What I Built

| Part | What it shows |
|---|---|
| Unstable trees | Same data, different trees |
| Bagging by hand | 25 trees voting beat one tree |
| Model comparison | Ensembles beat a single tree in cross-validation |
| Learning-rate experiment | How boosting improves tree by tree |

---
