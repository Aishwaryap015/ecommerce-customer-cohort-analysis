# 📊 E-Commerce Customer Cohort Analysis

This project performs an in-depth **E-Commerce customer behavior and cohort analysis** using transactional data to understand **customer retention, churn patterns, and revenue trends**.

---

## 🧠 Objective
- Analyze customer purchase behavior over time
- Identify retention patterns using cohort analysis
- Visualize revenue growth and customer lifetime behavior

---

## 📁 Dataset
- **Source**: UK Online Retail Dataset
- **Time Period**: 2010–2011
- **Records**: ~500,000 transactions
- **Key Fields**:
  - InvoiceNo
  - CustomerID
  - InvoiceDate
  - Quantity
  - UnitPrice
  - Country

---

## 🛠️ Tools & Technologies
- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

---

## 🔍 Analysis Performed

### 1️⃣ Data Cleaning
- Removed missing Customer IDs
- Converted date columns to datetime format
- Created total revenue per transaction

### 2️⃣ Basic Business Metrics
- Total Customers
- Total Orders
- Total Revenue

### 3️⃣ Monthly Revenue Trend
- Visualized revenue growth over time
- Identified peak revenue months

### 4️⃣ Cohort Analysis
- Grouped customers by first purchase month
- Calculated customer retention over time
- Built a cohort retention heatmap

---

## 📊 Key Visualizations
- Monthly Revenue Trend Line Chart
- Customer Retention Cohort Heatmap

---

## 💡 Key Insights
- Customer retention is highest in the first **2–3 months**
- Retention declines steadily over time indicating churn
- A small group of repeat customers contributes significantly to revenue
- Seasonal trends affect purchasing behavior

---

## 📂 Project Structure

ecommerce-customer-cohort-analysis/
│
├── data/
│ └── ecommerce_data.csv
│
├── notebooks/
│ └── ecommerce_cohort_analysis.ipynb
│
├── scripts/
│ └── data_cleaning.py
│
├── outputs/
│ └── cohort_heatmap.png
│
├── README.md
└── requirements.txt


---

## 🚀 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/Aishwaryap015/ecommerce-customer-cohort-analysis.git

# Navigate into the project
cd ecommerce-customer-cohort-analysis

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook

👩‍💻 Author

Aishwarya Priydarshni
🎓 Final-Year B.Tech CSE (Data Science) Student
🧠 Aspiring Data Scientist | Python • Pandas • Machine Learning • Data Visualization
📊 Passionate about transforming data into insights and impact

✨ About Me

I am a final-year Computer Science (Data Science) student with a strong interest in data science, analytics, and machine learning. I enjoy working with real-world datasets, building analytical workflows, and extracting meaningful business insights through data-driven approaches.

This project demonstrates my hands-on experience with customer cohort analysis, data preprocessing, and visual storytelling using Python.

💡 Skills Highlighted in This Project

Python (Pandas, NumPy)

Data Cleaning & Feature Engineering

Cohort Analysis & Retention Modeling

Data Visualization (Matplotlib, Seaborn)

Jupyter Notebook

Git & GitHub

📌 Project Note

This project is part of my data science learning journey and reflects my ability to:

Structure end-to-end data science projects

Handle real-world transactional data

Apply analytical thinking to customer behavior problems

Communicate insights clearly through visuals