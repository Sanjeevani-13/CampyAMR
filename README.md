# AI-Based Genomic Prediction of Antimicrobial Resistance in *Campylobacter jejuni* Using ML and DL Models

## Overview

Antimicrobial resistance (AMR) makes bacterial infections more difficult to treat and is an important public health concern. This project explores the use of machine learning (ML) and deep learning (DL) to predict antimicrobial resistance in *Campylobacter jejuni* using whole-genome sequencing (WGS) data.

Genomic sequences were converted into numerical features using 3-mer frequency extraction. A Random Forest classifier and a hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) model were explored for binary classification of isolates as resistant or susceptible. Feature-importance analysis was also used to identify influential genomic features.

The project combines genomic data preprocessing, feature engineering, model development, performance evaluation, and exploratory interpretation of resistance-associated genomic patterns.

## Objectives

- Develop a computational framework for predicting antimicrobial resistance from bacterial genome sequences.
- Preprocess genomic sequences and associated resistance metadata.
- Extract numerical features using 3-mer frequency representation.
- Apply machine learning and deep learning approaches to resistance classification.
- Evaluate model performance using standard classification metrics.
- Identify influential k-mer features and explore their potential biological relevance.

## Dataset

- **Source:** Bacterial and Viral Bioinformatics Resource Center (BV-BRC)
- **Organism:** *Campylobacter jejuni*
- **Number of isolates:** 300
- **Data format:** Genome sequences in FASTA format with associated metadata and resistance labels
- **Classification task:** Binary classification — resistant vs. susceptible

The project dataset comprised 150 resistant and 150 susceptible isolates. Genome identifiers were matched with metadata to associate each genome with its corresponding resistance label.

## Methodology

### 1. Data Collection and Preprocessing

Genome sequences and corresponding metadata were obtained from BV-BRC. The preprocessing workflow included:

- Parsing genome sequences from FASTA files.
- Matching genome identifiers with metadata.
- Preparing binary resistance labels.
- Organizing the data for downstream feature extraction and model training.

### 2. Dataset Splitting

The dataset was divided using a stratified split to preserve the class distribution across the training, validation, and testing subsets.

| Subset     | Samples | Proportion |
| Training   |   210   |    70%     |
| Validation |   45    |    15%     |
| Testing    |   45    |    15%     |
| **Total**  | **300** |  **100%**  |

### 3. 3-mer Feature Extraction

The genomic sequences were represented using overlapping nucleotide subsequences of length three, known as 3-mers.

K-mer-based feature extraction converts sequence information into numerical representations suitable for machine learning. The project materials describe a feature matrix containing 1,254 features.

### 4. Model Development

**Random Forest**

A supervised ensemble learning algorithm was used to classify genomic samples based on the extracted k-mer features. Random Forest combines predictions from multiple decision trees and supports feature-importance analysis.

**Hybrid CNN–LSTM**

A hybrid deep learning approach combining Convolutional Neural Network (CNN) and Long Short-Term Memory (LSTM) components was used in the reported experiments. CNN layers can learn local patterns, while LSTM layers are designed to learn sequential dependencies.

The architecture, input representation, training configuration, and evaluation outputs should be included in the repository to enable independent reproduction of the CNN–LSTM results.

### 5. Model Evaluation and Interpretation

The project evaluated classification performance using standard metrics, including:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Feature-importance analysis was used to identify influential k-mer features and explore their potential association with antimicrobial resistance.

Feature importance indicates predictive association; it does not independently establish a causal biological mechanism.

## Results

The project presentation reports the following test accuracies:

| Model | Reported test accuracy |
|---|---:|
| Random Forest | 93.33% |
| Hybrid CNN–LSTM | 86.67% |

Random Forest achieved the higher reported accuracy in these experiments.

**Reproducibility note:** The Random Forest implementation is available in the repository. The CNN–LSTM result should be treated as a reported experimental result until the corresponding implementation and evaluation outputs are available for verification. Confirm the final confusion matrices and prediction counts before using these metrics in formal reports or presentations.

These results describe performance on the project dataset and do not establish generalization to independent populations or clinical settings.

## Technologies and Libraries

The project uses or explores the following technologies. The final dependency list should match the libraries used in the corresponding scripts.

- **Python** — primary programming language
- **Biopython** — genomic sequence parsing
- **Pandas** — metadata and tabular data processing
- **NumPy** — numerical computation
- **Scikit-learn** — machine learning, data splitting, and evaluation
- **Deep learning framework** — confirm the framework used by the final CNN–LSTM implementation
- **Matplotlib and Seaborn** — data visualization, where used

## Repository Structure

The repository contains the project's Python scripts and associated data or feature files. Refer to the actual directory listing in GitHub for the current file organization.

Key components include:

- `ML.py` — Random Forest training and evaluation
- `Train_F.py` — training-related workflow
- `kmer.py` — k-mer processing
- Feature tables and other supporting project files

Additional model scripts, notebooks, evaluation outputs, and dependency files should be included as applicable to the final implementation.

## Getting Started

### Prerequisites

- Python 3
- Genome FASTA files and matching metadata
- Python libraries required by the selected scripts

### Installation

Clone the repository:

```bash
git clone https://github.com/Sanjeevani-13/CampyAMR.git
cd CampyAMR
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies required by the scripts you intend to run. For the Random Forest workflow, the core dependencies include:

```bash
pip install biopython pandas numpy scikit-learn matplotlib seaborn
```

Install the appropriate deep learning framework separately once the CNN–LSTM implementation and its dependencies have been confirmed.

### Running the Project

The exact commands depend on the input files, script arguments, and current workflow. Consult the individual Python scripts for their expected input paths and execution instructions before running them.

A reproducible release should include the exact commands, dependency versions, input-data requirements, and output locations.

## Limitations

- The dataset contains 300 isolates, so performance and generalizability should be evaluated on additional independent datasets.
- Predictions depend on the dataset, resistance labels, preprocessing steps, feature representation, and evaluation strategy.
- Genomic similarity between samples can affect evaluation if related isolates occur across different data splits.
- Feature importance identifies predictive associations and does not prove that a feature causes antimicrobial resistance.
- The reported metrics should not be interpreted as evidence of clinical readiness.
- Independent validation and further biological investigation are needed before practical or clinical application.

## Future Work

- Validate the models using an independent dataset.
- Compare additional genomic feature representations and model configurations.
- Investigate influential k-mers in their genomic context.
- Improve model reproducibility through documented dependencies, training configurations, and saved evaluation outputs.
- Strengthen biological interpretation of candidate resistance-associated genomic patterns.

## Acknowledgements

The genomic data used in this project were obtained from the Bacterial and Viral Bioinformatics Resource Center (BV-BRC).

## References

1. Dahl, L. G., Joensen, K. G., Østerlund, M. T., Kiil, K., & Nielsen, E. M. (2021). Prediction of antimicrobial resistance in clinical *Campylobacter jejuni* isolates from whole-genome sequencing data. *European Journal of Clinical Microbiology & Infectious Diseases, 40*(4), 673–682. https://doi.org/10.1007/s10096-020-04043-y

2. Her, H. L., Wu, Y. W., Chen, Y. M. A., Lin, I. H., & Hsiung, C. A. (2022). Prediction of antimicrobial resistance based on whole-genome sequencing and machine learning. *Bioinformatics, 38*(2), 325–334. https://doi.org/10.1093/bioinformatics/btab629

3. Shi, J., Yan, Y., Links, M. G., et al. (2019). Antimicrobial resistance genetic factor identification using deep feature selection. *BMC Bioinformatics, 20*, 535. https://doi.org/10.1186/s12859-019-3054-4

4. Hodges, L. M., Taboada, E. N., Koziol, A., et al. (2021). Systematic evaluation of whole-genome sequencing-based prediction of antimicrobial resistance in *Campylobacter jejuni* and *C. coli*. *Frontiers in Microbiology, 12*, 776967. https://doi.org/10.3389/fmicb.2021.776967
