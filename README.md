# 🏠 Airbnb Superhost Prediction

> **Business Analytics II – Project II**  
> Classifying Airbnb hosts as "Superhost" or "Non-Superhost" using machine learning

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org)

---

## 🎬 Live Presentation

**👉 [View Interactive Presentation](https://yj99son.github.io/ba2_project2/presentation/presentation_en.html)**

Navigate with arrow keys, scroll, or click the dots on the right.

---

## 📋 Overview

This project builds and compares **6 classification models** to predict whether an Airbnb host qualifies as a **Superhost** based on listing characteristics, reviews, and host behavior metrics.

### Key Highlights
- 🎯 **93% Accuracy** with Random Forest (best model)
- 📊 **444 Features** engineered from 54 original features
- 🤖 **Sentence Transformer** embeddings for amenity text
- 🔍 **SHAP Analysis** for feature importance interpretation

---

## 🎯 Model Performance

| Model | Accuracy | Recall | F1-Score |
|:------|:--------:|:------:|:--------:|
| 🥇 **Random Forest** | **93.0%** | 67.5% | 73.6% |
| 🥈 Decision Tree | 89.4% | 66.2% | 67.8% |
| 🥉 PyTorch MLP | 83.5% | 82.7% | **76.4%** |
| KNN | 82.9% | 67.9% | 60.8% |
| Logistic Regression | 80.2% | 82.5% | 72.5% |
| Naive Bayes | 72.1% | **87.1%** | 58.2% |

---

## 📁 Project Structure

```
ba2_project2/
├── 📓 processing.ipynb              # Main analysis notebook
├── 📄 requirements.txt              # Dependencies
├── 📂 presentation/
│   ├── 🎬 presentation_en.html      # Interactive slides
│   ├── 📊 amenity_map.html          # t-SNE visualization
│   ├── 📓 processing_en.ipynb       # English notebook
│   ├── 📈 *_plot.png                # Model tuning charts
│   └── 📊 *_cv_results.csv          # CV results
└── 📄 README.md
```

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/YJ99Son/ba2_project2.git
cd ba2_project2

# Install dependencies
pip install -r requirements.txt

# Run
jupyter notebook processing.ipynb
```

---

## 🔬 Methodology

1. **Preprocessing**: Missing value handling, feature encoding, class balancing (upsampling)
2. **Feature Engineering**: Text embeddings (SentenceTransformer), property type clustering
3. **Model Training**: 5-fold CV with GridSearchCV
4. **Evaluation**: Accuracy, Recall, F1-Score, SHAP importance

---

## 👤 Author

**손영진 (Youngjin Son)** · 2020120083 · Business Analytics II, Fall 2025

---

<p align="center">⭐ Star this repo if you found it helpful!</p>
