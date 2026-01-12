from sklearn.ensemble import RandomForestClassifier

def train_models(X, y):
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        class_weight="balanced",
        random_state=42
    )
    model.fit(X, y)
    return model
