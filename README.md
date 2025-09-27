# Reseller Performance & Fraud Detection System

##  Overview 🎯

This project is an end-to-end analysis of an e-commerce platform's reseller network, designed to solve two key business problems: identifying top-performing sellers for growth opportunities and proactively detecting high-risk sellers to mitigate fraud. The analysis moves from foundational business intelligence to advanced risk assessment using SQL and culminates in a predictive machine learning model built with Python.

This project was developed as a case study for a Business Analyst role at a social commerce company like Meesho.

---

## Technologies Used 🛠️

* **Database:** `SQL (MySQL)`
* **Data Analysis & ML:** `Python`
* **Python Libraries:** `Pandas`, `Scikit-learn`, `SQLAlchemy`
* **Tools:** `MySQL Workbench`, `Jupyter Notebook`

---

## Project Workflow 📊

The project was executed in three main phases:

### 1. Foundational Business Intelligence (SQL)
* **Database Setup:** Loaded a 100k+ order dataset from multiple CSVs into a relational schema in a MySQL database.
* **Performance Analysis:** Wrote SQL queries to identify the top 10 resellers by total sales revenue and order volume.
* **Geographic Analysis:** Analyzed sales data to uncover the geographic concentration of top sellers, revealing that the state of São Paulo (SP) is the dominant market.

### 2. Advanced Risk Assessment (SQL)
* **Fraud Detection:** Developed SQL queries using `CASE` statements to calculate reseller-specific metrics like order cancellation rates, identifying sellers with rates significantly above the platform average.
* **Multi-Factor 'Risk Score':** Built a sophisticated query using **Common Table Expressions (CTEs)** to combine multiple risk factors (high cancellation rates, low average review scores) into a single, weighted **'Risk Score'**. This created an actionable tool to rank and prioritize sellers for review.

### 3. Predictive Modeling (Python & AI)
* **Feature Engineering:** Created a balanced dataset by querying both the highest and lowest-risk sellers from the SQL analysis.
* **Model Training:** Trained a **Logistic Regression** model using Scikit-learn to predict whether a seller is likely to be high-risk based on their performance metrics.
* **Evaluation:** The final model achieved **83.33% accuracy**, proving its capability as a proactive tool to flag potentially fraudulent sellers early.

---

## How to Run This Project 🚀

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/devadharshan11-design/Reseller-Performance-Analysis-/tree/main
    ```
2.  **Download the Dataset:**
    * The raw data is not included in this repository due to its size.
    * Download the Olist E-commerce dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
    * Place the unzipped CSV files into a folder named `olist_data` inside the main project directory.
3.  **Setup the Database:**
    * Ensure you have a running MySQL server.
    * Create a new schema (e.g., `meesho_project`).
    * Update your MySQL credentials (`DB_USER`, `DB_PASSWORD`, `DB_NAME`) in the Python scripts (`importingtable.py`, `AICODE.py`).
4.  **Run the Scripts:**
    * Execute `importingtable.py` to load the data into your MySQL database.
    * Run the `.sql` files in MySQL Workbench to see the analysis.
    * Execute `AICODE.py` to train and evaluate the machine learning model.