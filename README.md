# Customer Segmentation – X Securities Company

## Project Overview
This project analyzes and segments customers of **X Securities Company** into clusters using **K-Means clustering**, then compares the results against the company’s existing **rule-based segmentation**.

The aim is to:
- Evaluate whether machine learning-based segmentation aligns with existing business rules.
- Identify potential improvements to customer classification.
- Provide actionable insights for targeted marketing and customer engagement.

---

## Data Overview
The project uses **three main datasets**, each representing a different customer activity status:

1. **Active**  
   - Customers who have **traded within the last 12 months**.
2. **Inactive**  
   - Customers who have traded **in the past**, but **no transactions in the last 12 months**.
3. **Nonactive**  
   - Customers who have **opened a securities account** but **never made a transaction**.

Each dataset is stored in a separate folder:
📁 active/
📁 inactive/
📁 nonactive/


---

## Methodology
For each dataset (`active`, `inactive`, `nonactive`):

1. **Data Preprocessing**
   - Clean missing values.
   - Handle outliers in transaction amounts and frequency.
   - Standardize numerical features for K-Means.

2. **Feature Engineering**
   - Calculate key behavioral metrics:
     - **Recency (R)** – Days since last transaction.
     - **Frequency (F)** – Number of transactions over the period.
     - **Monetary (M)** – Total transaction value.
     - **NAV (N)** – Current Net Asset Value.
   - Transform skewed variables (e.g., log transformation).

3. **K-Means Clustering**
   - Determine optimal **k** using the **Elbow method** and **Silhouette score**.
   - Fit K-Means on standardized features.
   - Assign cluster labels to customers.

4. **Cluster Profiling**
   - Summarize R, F, M, N for each cluster.
   - Describe behavioral traits of each segment.

5. **Comparison with Rule-Based Segmentation**
   - Map clusters to the company’s existing segmentation categories.
   - Identify mismatches where ML clustering suggests reclassification.

---

## Example Output
For each dataset, the analysis produces:
- **Cluster distribution charts**.
- **RFMN heatmaps**.
- **Mapping tables** showing differences between ML-based and rule-based segments.
- **Business recommendations** for each segment.

---

## Tools & Technologies
- **Programming Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Environment**: Jupyter Notebook

---

