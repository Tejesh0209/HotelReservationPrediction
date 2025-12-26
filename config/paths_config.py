import os

###################### DATA PATH CONFIGURATIONS ######################
RAW_DIR = "artifacts/raw"
RAW_File_Path = os.path.join(RAW_DIR, "raw.csv")
Train_File_Path = os.path.join(RAW_DIR, "train.csv")
Test_File_Path = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH = "config/config.yaml"


##################### DATA PROCESSING PATH CONFIGURATIONS ####################
PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_train.csv")
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_test.csv")


