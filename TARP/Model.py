import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Load the data
data = pd.read_csv('updated_merged_data.csv')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform Grid Search to find the best hyperparameters
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42),
                           param_grid=param_grid,
                           cv=5)
grid_search.fit(X_scaled, y)

# Get the best parameters and retrain the model
best_params = grid_search.best_params_
best_classifier = DecisionTreeClassifier(random_state=42, **best_params)
best_classifier.fit(X_scaled, y)

# Define a function to predict the target based on input values
def predict_target(input_values):
    # Check if the number of input features matches the number used during training
    if len(input_values) != X.shape[1]:
        raise ValueError(f'Input should have {X.shape[1]} features, but got {len(input_values)} features.')
    
    # Standardize the input values using the same scaler
    input_values_standardized = scaler.transform([input_values])
    
    # Predict the target based on the input values using the best model
    predicted_target = best_classifier.predict(input_values_standardized)[0]
    
    return predicted_target