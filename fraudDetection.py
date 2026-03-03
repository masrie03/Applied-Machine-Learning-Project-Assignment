import pandas as pd


# Step 1: Define column names
column_names = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
    'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
    'num_root', 'num_file_creations', 'num_shells', 'num_access_files',
    'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
    'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label'
]


# Step 2: Load datasets
train_path = "C:/Users/masri/OneDrive - Asia Pacific University of Technology And Innovation (APU)/SEM1/AML/Assignment/archive/KDDTrain+.txt"  
test_path  = "C:/Users/masri/OneDrive - Asia Pacific University of Technology And Innovation (APU)/SEM1/AML/Assignment/archive/KDDTest+.txt"   

train_df = pd.read_csv(train_path, names=column_names)
test_df  = pd.read_csv(test_path, names=column_names)

# Step 3: Basic info
print("=== TRAIN DATASET INFO ===")
print("Shape:", train_df.shape)
print("\nMissing values:\n", train_df.isnull().sum())
print("\nClass distribution:\n", train_df['label'].value_counts())

print("\n=== TEST DATASET INFO ===")
print("Shape:", test_df.shape)
print("\nMissing values:\n", test_df.isnull().sum())
print("\nClass distribution:\n", test_df['label'].value_counts())
