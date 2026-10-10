# ==============================
# STEP 1: IMPORTS
# ==============================
from Bio import SeqIO
from collections import Counter
import pandas as pd

# ==============================
# STEP 2: LOAD CSV FILES
# ==============================
train_df = pd.read_csv("train.csv")
val_df = pd.read_csv("val.csv")
test_df = pd.read_csv("test.csv")

# Ensure same datatype
train_df['Genome ID'] = train_df['Genome ID'].astype(str)
val_df['Genome ID'] = val_df['Genome ID'].astype(str)
test_df['Genome ID'] = test_df['Genome ID'].astype(str)

# ==============================
# STEP 3: K-MER FUNCTIONS
# ==============================
k = 3  # you can try 4 later

def get_kmers(sequence, k):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def kmer_count(sequence, k):
    return Counter(get_kmers(sequence, k))

def process_fasta(fasta_file):
    data = []
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        counts = kmer_count(seq, k)
        
        # Extract Genome ID
        genome_id = record.description.split('|')[-1].replace(']', '').strip()
        
        counts['Genome ID'] = str(genome_id)
        data.append(counts)
    
    return pd.DataFrame(data).fillna(0)

# ==============================
# STEP 4: PROCESS FASTA FILES
# ==============================
train_features = process_fasta("train.fasta")
val_features = process_fasta("val.fasta")
test_features = process_fasta("test.fasta")

# ==============================
# STEP 5: FIX FEATURE MISMATCH (VERY IMPORTANT)
# ==============================
train_columns = train_features.columns

val_features = val_features.reindex(columns=train_columns, fill_value=0)
test_features = test_features.reindex(columns=train_columns, fill_value=0)

# ==============================
# STEP 6: MERGE WITH LABELS
# ==============================
train_data = train_features.merge(train_df, on="Genome ID")
val_data = val_features.merge(val_df, on="Genome ID")
test_data = test_features.merge(test_df, on="Genome ID")

# ==============================
# STEP 7: VERIFY OUTPUT
# ==============================
print("Train shape:", train_data.shape)
print("Val shape:", val_data.shape)
print("Test shape:", test_data.shape)

print("\nSample data:")
print(train_data.head())

# ==============================
# STEP 8: SAVE FINAL FILES
# ==============================
train_data.to_csv("train_features.csv", index=False)
val_data.to_csv("val_features.csv", index=False)
test_data.to_csv("test_features.csv", index=False)

print("\nFeature files saved successfully!")