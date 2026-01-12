from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

MODEL_PATH = "models/thermal_comfort_model.pkl"


def train_models(X, y):
    """
    Train and compare ML models for thermal comfort prediction.
    """

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        )
    }

    best_model = None
    best_accuracy = 0.0

    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print(f"{name} Accuracy: {acc:.4f}")
        print(classification_report(y_test, y_pred))

        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model

    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)

    # Save best model
    joblib.dump(best_model, MODEL_PATH)
    print(f"\nBest model saved at: {MODEL_PATH}")

    return best_model
