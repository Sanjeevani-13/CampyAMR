import pandas as pd
from sklearn.model_selection import train_test_split
from Bio import SeqIO


df = pd.read_csv("MD.csv")

print(" Metadata loaded")
print(df.head())


train_df, temp_df = train_test_split(
    df, test_size=0.3, stratify=df['Label'], random_state=42
)

val_df, test_df = train_test_split(
    temp_df, test_size=0.5, stratify=temp_df['Label'], random_state=42
)

print("\n Data split done")
print("Train size:", len(train_df))
print("Validation size:", len(val_df))
print("Test size:", len(test_df))

df['Label'] = df['Label'].map({'Resistant': 1, 'Susceptible': 0})

# Features (Genome IDs) and Labels
X = df['Genome ID']
y = df['Label']

# Step 1: Train (70%) and temp (30%)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

# Step 2: Validation (15%) and Test (15%)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    stratify=y_temp,
    random_state=42
)

# Combine back into DataFrames (optional but useful)
train_df = pd.DataFrame({'Genome ID': X_train, 'Label': y_train})
val_df = pd.DataFrame({'Genome ID': X_val, 'Label': y_val})
test_df = pd.DataFrame({'Genome ID': X_test, 'Label': y_test})

# Save files
train_df.to_csv("train.csv", index=False)
val_df.to_csv("val.csv", index=False)
test_df.to_csv("test.csv", index=False)


fasta_dict = {}

for record in SeqIO.parse("genome_sequence.fasta", "fasta"):
    desc = record.description
    
    # Extract genome_id from last part: [ ... | 197.20728]
    if "|" in desc:
        G_id = desc.split("|")[-1].replace("]", "").strip()
        fasta_dict[G_id] = record

print("\nFASTA loaded")
print("Total sequences in FASTA:", len(fasta_dict))


def extract_sequences(df, fasta_dict):
    sequences = []
    labels = []
    
    for _, row in df.iterrows():
        gid = str(row['Genome ID'])
        
        if gid in fasta_dict:
            sequences.append(str(fasta_dict[gid].seq))
            labels.append(row['Label'])
    
    return sequences, labels


train_sequences, train_labels = extract_sequences(train_df, fasta_dict)
val_sequences, val_labels = extract_sequences(val_df, fasta_dict)
test_sequences, test_labels = extract_sequences(test_df, fasta_dict)


print("\n Extraction done")

print("\nTrain sequences:", len(train_sequences))
print("Train labels:", len(train_labels))

print("\nValidation sequences:", len(val_sequences))
print("Test sequences:", len(test_sequences))

# Show sample safely
if len(train_sequences) > 0:
    print("\nSample sequence:", train_sequences[0][:50])
    print("Sample label:", train_labels[0])
else:
    print("\n No sequences matched — check ID mapping")


match_percent = (len(train_sequences) / len(train_df)) * 100
print(f"\n Match percentage: {match_percent:.2f}%")


from Bio import SeqIO

train_ids = set(train_df['Genome ID'].astype(str).str.strip())
val_ids = set(val_df['Genome ID'].astype(str).str.strip())
test_ids = set(test_df['Genome ID'].astype(str).str.strip())
fasta_file = "genome_sequence.fasta"

train_out = open("train.fasta", "w")
val_out = open("val.fasta", "w")
test_out = open("test.fasta", "w")

for record in SeqIO.parse(fasta_file, "fasta"):
    header = record.description
    
    # ✅ Extract genome_id INSIDE loop
    genome_id = header.split("|")[-1].strip(" ]")
    
    if genome_id in train_ids:
        SeqIO.write(record, train_out, "fasta")
    elif genome_id in val_ids:
        SeqIO.write(record, val_out, "fasta")
    elif genome_id in test_ids:
        SeqIO.write(record, test_out, "fasta")

train_out.close()
val_out.close()
test_out.close()

def count_headers(file):
    with open(file) as f:
        return sum(1 for line in f if line.startswith(">"))

print("Train:", count_headers("train.fasta"))
print("Validation:", count_headers("val.fasta"))
print("Test:", count_headers("test.fasta"))