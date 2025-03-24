# Credit Card Fraud Detection Project

##### By: Manvanth Sundareshan

## Project Description

This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The aim is to identify patterns within transactional data that distinguish between legitimate and fraudulent activities. A systematic approach is taken, starting with data exploration, visualization, and preprocessing, followed by model training and evaluation.

---

## Table of Contents

1. [Project Description](#project-description)
2. [Installation Instructions](#installation-instructions)
3. [Usage](#usage)
4. [Data Sources](#data-sources)
5. [Methodology](#methodology)
6. [Results and Insights](#results-and-insights)
7. [Buisness questions](#Buisness-questions-and-answers)
8. [Technologies Used](#technologies-used)
9. [Lisences](#Lisence-used)
10. [Future Work](#future-work)
11. [Reference](#References)
12. [Contact Information](#contact-information)

---

## Installation Instructions

### Prerequisites:
1. Python 3.x
2. Jupyter Notebook or any Python IDE

### Steps:
1. Clone the repository or download the project files.
2. Install the required Python libraries by running:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Place the dataset in the same directory as the notebook.
4. Open and run the notebook file step-by-step.

---

## Usage

1. **Dataset Exploration:** Gain insights into the data structure, check for null and duplicate values, and review correlations.
2. **Visualization:** Analyze transaction distributions and correlations to understand fraud patterns.
3. **Model Training:** Split the data into training and testing sets, then train a logistic regression model.
4. **Evaluation:** Use metrics like the confusion matrix, accuracy score, ROC curve, and AUC score to evaluate model performance.

---

## Data Sources

- The transactional data used in this project is sourced from a credit card fraud detection dataset provided as part of the coursework.
- The dataset contains features like transaction amount, class labels (fraud/non-fraud), and anonymized transactional details.

---

## Methodology

1. **Data Cleaning:** Handle null values, duplicates, and anomalies in the dataset.
2. **Exploratory Data Analysis (EDA):** Use visualizations like histograms, correlation heatmaps, and box plots.
3. **Data Preprocessing:** Normalize features using standard scaling.
4. **Model Training:** Train a logistic regression model to classify fraudulent transactions.
5. **Evaluation:** Validate model predictions using metrics like confusion matrices and ROC curves.

---

## Results and Insights

- A logistic regression model was implemented, providing a baseline for fraud detection.
- Key metrics include accuracy, precision, recall, and AUC-ROC scores.
- Fraudulent transactions show distinct patterns in certain features, aiding in detection.

---
## Buisness Questions

#### 1. Can Fraud Prediction Models Support Personalized Risk-Based Pricing Strategies for Customers Based on Transaction Behavior?

- Fraud prediction models, particularly those built using machine learning techniques, can effectively classify and score transactions based on features extracted from historical data, including spending patterns and anomalies (Lakshmi and Kavila, 2018).

- Customers identified as high-risk by the model could face adjusted rates reflecting the increased potential for fraud. 
- Logistic Regression, with its ability to interpret risk probabilities, serves as a practical tool for integrating fraud detection into personalized financial offerings.

---

#### 2. Are There Ways to Integrate Fraud Prevention with Marketing Analytics to Identify Loyal Customers and Cross-Sell Premium Services While Maintaining Security?

- By analyzing transaction frequency and consistency, fraud detection models can flag customers exhibiting stable and trustworthy behavior as loyal.
- Low-risk customers making frequent high-value transactions, such as travel bookings, can be targeted with personalized offers, such as travel benefits or premium concierge services.
- Positioning fraud prevention as a value-added service to reinforce customer trust while delivering tailored marketing initiatives.

---

#### 3. Can the Insights and Models Developed for Internal Fraud Detection Be Monetized by Offering Fraud Prevention Solutions to Other Businesses?

- Fraud detection systems can be repackaged into APIs for other companies to integrate into their platforms.
- Companies can sell or license their fraud prevention technologies to businesses across various industries, transforming internal tools into revenue-generating assets.
- The same models can be customized for industries beyond financial services, including e-commerce, travel, and insurance, thereby expanding their market potential.

---
## Technologies Used

- **Languages:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Tools:** Jupyter Notebook

---
## Licenses Used

- **Lisence name** MIT Lisence

---
## Future Work

- Implement more complex models like Random Forest, Gradient Boosting, or Neural Networks for improved accuracy.
- Perform feature engineering to identify more predictive features.
- Test on real-time transaction data for robust evaluation.

---
## References

- 	Lakshmi, S. V. S. S., & Kavila, S. D. (2018). Machine Learning for Credit Card Fraud Detection System. International Journal of Applied Engineering Research, 13(24), pp. 16819–16824.

---
## Contact Information

For questions, suggestions, or collaboration opportunities, please contact:

- **Name:** Manvanth Sundareshan
- **Email:** sundareshan.manvanth@stud.hs-fresenius.de
- **GitHub:** (https://github.com/codeflex98)
- **Steamlit URL for running this app:** https://creditcardfrauddetectionappio-ypke7mxdwvih4dfm6uxknn.streamlit.app/
