# 🧹 Pandas Data Cleaning Practice 

## 🚫 Issue
The script made several common data quality issues:
* **Inconsistent Text**
* **Mixed Types**
* **Duplicates**
* **Missing Data** 
* **Wrong Data Types**

## ✅ Solution (Methods used)
* `.str.strip()` to clean text fields.
* `.str.replace()` methods to strip currency symbols.
* **Type Coercion:**
  * `pd.to_numeric(errors='coerce')` to handle non-numeric values like "Unknown".
  * `pd.to_datetime()` to convert string dates into true TimeStamp objects.
  * `pd.to_datetime(format='mixed')` to handle the mixed data formats.
* `.dropna()` to remove rows with missing data.
* `.drop_duplicates()`. to remove dupes

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `numpy`

* ## 🚀 How to Run

### Prerequisites
Ensure you have Python installed. You can install the required libraries using pip:

```bash
pip install pandas numpy
```
1. **Clone the repo:**
```bash
pip install pandas numpy
```
1. **Navigate to directory**
```bash
cd data-cleaning-toolkit
```
3. **Run script**
```bash
python cleaning_practice.py
```

## 📊 Results (Before vs. After)
<<img width="331" height="479" alt="{17FEE7B3-8A12-47E3-B91F-815D7030611E}" src="https://github.com/user-attachments/assets/ed089b23-b971-4166-860d-052ff2049986" />

