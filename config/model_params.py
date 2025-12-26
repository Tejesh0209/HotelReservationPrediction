from scipy.stats import uniform, randint

LIGHTGBM_PARAM_DISTRIBUTION = {
    'n_estimators': randint(100, 1000),
    'learning_rate': uniform(0.01, 0.3),
    'max_depth': randint(5,50),
    'boosting_type': ['gbdt', 'dart', 'goss'],
    'num_leaves': randint(20, 100),
}

RANDOM_FOREST_PARAM_DISTRIBUTION = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(5, 50),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 20),
    'bootstrap': [True, False]
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 5,
    'scoring': 'accuracy',
    'cv': 5,
    'verbose': 1,
    'random_state': 42,
    'n_jobs': -1
}

# Model parameters for training
MODEL_PARAMS = {
    'lightgbm': LIGHTGBM_PARAM_DISTRIBUTION
}

# Training parameters
TRAINING_PARAMS = RANDOM_SEARCH_PARAMS