ETA_BASIC = 1
ETA_PEGASOS = 2
ETA_CONSTANT = 3

LOOP_BALANCED_STOCHASTIC = 1
LOOP_STOCHASTIC = 2

PREDICTION_LINEAR = 1
PREDICTION_LOGISTIC = 2

LEARNER_PEGASOS_SVM = 1
LEARNER_PEGASOS_LOGREG = 2

# defaults for hyperparameters
DFLT_ITERATIONS = 100000
DFLT_LAMBDA_REG = 0.1
DFLT_DIMENSION = 2<<16

# make sure we protect against lambda * eta > 1.0 which
# causes numerical issues for regularization and projection
MIN_SCALING_FACTOR = 0.0000001
