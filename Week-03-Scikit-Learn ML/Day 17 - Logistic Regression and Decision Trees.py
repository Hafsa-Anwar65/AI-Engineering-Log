"""
Day 17 · Logistic regression & decision trees (+ text features with TF-IDF)
"""
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, export_text

RANDOM = 42

# ------------------------------------------------------------
# 1. The sigmoid: turns any number into a probability (0 to 1)
# ------------------------------------------------------------
print("=== 1. Sigmoid ===")


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


for z in [-5, -1, 0, 1, 5]:
    print(f"z = {z:>2}  ->  probability {sigmoid(z):.3f}")

# ------------------------------------------------------------
# 2. Logistic regression on real data
# ------------------------------------------------------------
print("\n=== 2. Logistic regression ===")
data = load_breast_cancer()
X, y = data.data, data.target            # 0 = malignant, 1 = benign
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM
)

log_reg = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
log_reg.fit(X_train, y_train)
print(f"Test accuracy: {accuracy_score(y_test, log_reg.predict(X_test)):.3f}")

# predict_proba gives the probability for each class
probs = log_reg.predict_proba(X_test[:5])[:, 1]
for p, true in zip(probs, y_test[:5]):
    print(f"P(benign) = {p:.3f}   real: {'benign' if true else 'malignant'}")

# Which features push towards benign or malignant?
coefs = log_reg.named_steps["logisticregression"].coef_[0]
top = np.argsort(np.abs(coefs))[::-1][:5]
print("\nMost important features:")
for i in top:
    direction = "benign" if coefs[i] > 0 else "malignant"
    print(f"  {data.feature_names[i]:<25} {coefs[i]:+.2f}  (pushes to {direction})")

# ------------------------------------------------------------
# 3. Decision tree: a flowchart of yes/no questions
# ------------------------------------------------------------
print("\n=== 3. Decision tree ===")
for depth in [1, 3, 5, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=RANDOM).fit(X_train, y_train)
    print(f"max_depth={str(depth):<5} train {tree.score(X_train, y_train):.3f} | "
          f"test {tree.score(X_test, y_test):.3f}")
print("No depth limit -> 100% on train but lower on test = overfitting")

small_tree = DecisionTreeClassifier(max_depth=2, random_state=RANDOM).fit(X_train, y_train)
print("\nThe tree's questions (depth 2):")
print(export_text(small_tree, feature_names=list(data.feature_names)))

print("Classification report (depth 3 tree):")
tree3 = DecisionTreeClassifier(max_depth=3, random_state=RANDOM).fit(X_train, y_train)
print(classification_report(y_test, tree3.predict(X_test), target_names=data.target_names))

# ------------------------------------------------------------
# 4. Text classification with TF-IDF
# ------------------------------------------------------------
print("=== 4. Text: spam or not? (TF-IDF + logistic regression) ===")
messages = [
    "Win a free iPhone now, click here", "Congratulations you won 1 lakh cash prize",
    "Claim your free reward today only", "Urgent: your account wins a lucky draw",
    "Limited offer, buy now and get free gift", "You are selected for a free holiday",
    "Are we meeting for lunch tomorrow?", "Please send me the lecture notes",
    "Assignment deadline is on Friday", "Can you call me after the class?",
    "The project meeting moved to 3 pm", "Thanks for the help with the code",
]
labels = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]   # 1 = spam, 0 = normal

spam_model = make_pipeline(TfidfVectorizer(), LogisticRegression())
spam_model.fit(messages, labels)

tests = ["Free prize waiting, click now", "Can you send the notes before class?",
         "You won a free gift card"]
for msg, p in zip(tests, spam_model.predict_proba(tests)[:, 1]):
    print(f"{'SPAM ' if p > 0.5 else 'OK   '} {p:.2f}  {msg}")

# Words the model links most with spam
vec = spam_model.named_steps["tfidfvectorizer"]
weights = spam_model.named_steps["logisticregression"].coef_[0]
words = np.array(vec.get_feature_names_out())
print("Top spam words:", ", ".join(words[np.argsort(weights)[::-1][:6]]))