# Network Intrusion Detection Using Ensemble Machine Learning

An Applied Machine Learning project that evaluates ensemble learning techniques for multi-class network intrusion detection using the **NSL-KDD dataset**.

This project was developed as part of the **Applied Machine Learning (CT046-3-M)** module in the Master of Science in Artificial Intelligence programme at Asia Pacific University (APU).

## Overview

Network intrusion detection involves identifying malicious network activity from network traffic data. This project investigates how different ensemble machine learning algorithms perform on the NSL-KDD benchmark dataset.

The project covers the complete machine learning workflow:

- Exploratory Data Analysis (EDA)
- Data preprocessing and cleaning
- Categorical feature encoding
- Outlier-resistant feature scaling
- Class imbalance handling
- Ensemble model training
- Model comparison
- Cross-validation
- Feature importance analysis

## Dataset

The project uses the **NSL-KDD dataset**, a benchmark dataset commonly used for network intrusion detection research.

The dataset contains:

- 125,973 training instances
- 41 input features
- Numerical and categorical network traffic attributes
- Normal network traffic and multiple attack categories

Attack types include:

- Denial of Service (DoS)
- Probe
- Remote-to-Local (R2L)
- User-to-Root (U2R)

## Data Preprocessing

Several preprocessing techniques were applied before model training.

### Categorical Encoding

Categorical variables such as:

- `protocol_type`
- `service`
- `flag`

were converted into numerical representations.

### Robust Scaling

The dataset contains highly skewed numerical features and extreme outliers, particularly network traffic features such as `src_bytes`.

**RobustScaler** was used because it relies on the median and interquartile range, making it less sensitive to extreme values.

### Class Imbalance

The original dataset contains substantial class imbalance, particularly for rare attack categories.

**Synthetic Minority Over-sampling Technique (SMOTE)** was applied to improve the representation of minority classes during model training.

## Machine Learning Models

Three ensemble learning approaches were evaluated:

### Random Forest

A bagging-based ensemble of decision trees designed to reduce variance and improve classification stability.

### AdaBoost

A sequential boosting algorithm that increases the importance of previously misclassified samples during training.

### HistGradientBoosting

A histogram-based gradient boosting algorithm designed to provide efficient training on larger datasets.

## Experimental Results

The experiments produced the following results:

| Model | Accuracy | Training Time |
|---|---:|---:|
| Random Forest | 99.99% | 1.27 min |
| AdaBoost | 49.69% | 2.61 min |
| HistGradientBoosting | 99.98% | 2.11 min |

Random Forest achieved the highest reported accuracy, while HistGradientBoosting achieved comparable performance. AdaBoost performed substantially worse under the experimental configuration.

## Model Validation

Random Forest was further evaluated using **5-fold cross-validation**.

Reported validation results:

- Mean CV Accuracy: **99.97%**
- Standard Deviation: **0.000088**

Feature-importance analysis was also performed to examine which network attributes contributed most strongly to the Random Forest predictions.

Important features included:

- `src_bytes`
- `wrong_fragment`
- `dst_bytes`
- `service`
- `dst_host_srv_diff_host_rate`

## Project Structure

```text
.
├── IntursionDetection(Source Code).ipynb
├── Submission AML.pdf
└── README.md
```

`IntursionDetection(Source Code).ipynb` contains the machine learning implementation and experimental workflow.

`Submission AML.pdf` contains the complete assignment report, methodology, analysis, experimental results, and discussion.

## Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Matplotlib
- Seaborn

## Running the Project

Clone the repository:

```bash
git clone https://github.com/masrie03/Applied-Machine-Learning-Project-Assignment.git
```

Navigate into the repository and open the notebook:

```bash
jupyter notebook "IntursionDetection(Source Code).ipynb"
```

Install the required Python libraries if they are not already available in your environment.

## Limitations

The NSL-KDD dataset is useful for controlled benchmarking but does not fully represent modern network environments or contemporary cyberattacks.

The project therefore evaluates machine learning techniques under a benchmark experimental setting rather than claiming production-level intrusion detection performance.

Potential future improvements include:

- Evaluation using more recent intrusion detection datasets
- Testing against real network traffic
- Adversarial robustness testing
- Real-time intrusion detection
- Further investigation of minority attack classes

## Author

**Masrie bin Bukhori**

Master of Science in Artificial Intelligence  
Asia Pacific University of Technology & Innovation (APU)

## Academic Context

This repository contains coursework developed for the **Applied Machine Learning (CT046-3-M)** module.

The project focuses on applying and evaluating machine learning techniques for network intrusion detection rather than providing a production-ready cybersecurity system.