# 📊 Business Data Analysis with Python

## About this Project

This project was created to practice data analysis with Python and Pandas using a fictional company's datasets.

The goal was to answer some common business questions by working with different datasets, cleaning the data, combining tables, and calculating useful metrics.

Although the datasets are in Portuguese, all the analysis and code were written in English to make the project easier for an international audience.

---

## Datasets

The project uses three datasets:

| File | Description |
|------|-------------|
| CadastroFuncionarios.csv | Employee information |
| CadastroClientes.csv | Client information |
| BaseServiçosPrestados.xlsx | Service contracts |

These files were provided as part of a learning project and kept with their original names.

---

## Technologies

- Python
- Pandas
- Matplotlib

---

## Business Questions

This project answers the following questions:

### 1. What is the company's total payroll cost?

The total employee cost was calculated by adding:

- Base salary
- Taxes
- Benefits
- Transportation allowance (VT)
- Meal allowance (VR)

---

### 2. What is the company's total revenue?

Revenue was calculated by multiplying:

- Monthly contract value
- Contract duration (months)

---

### 3. What percentage of employees have closed at least one contract?

The project compares:

- Employees who closed contracts
- Total number of employees

This shows the company's employee closing rate.

---

### 4. Which department closed the most contracts?

Using the employee ID, the services dataset was combined with the employees dataset to identify which departments generated the highest number of contracts.

---

### 5. How many employees work in each department?

The number of employees in each department was calculated to better understand the company's workforce distribution.

---

### 6. What is the average monthly contract value?

The average monthly contract value was calculated using the clients dataset.

---

## What I Practiced

During this project I practiced:

- Reading CSV and Excel files
- Data cleaning
- Selecting and removing columns
- Creating new columns
- Merging datasets
- Aggregating data
- Calculating business KPIs
- Working with Pandas
- Basic data visualization with Matplotlib

---

## Project Structure

```
Business-Data-Analysis/
│
├── data/
│   ├── CadastroClientes.csv
│   ├── CadastroFuncionarios.csv
│   └── BaseServiçosPrestados.xlsx
│
├── analysis.py
├── README.md
├── requirements.txt
└── images/
```

---

## How to Run

Clone this repository:

```bash
git clone https://github.com/yourusername/business-data-analysis.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python analysis.py
```

---

## Sample Output

The script calculates:

- Total payroll cost
- Total company revenue
- Employee closing rate
- Contracts per department
- Employees per department
- Average monthly contract value

---

## Future Improvements

Some ideas to improve this project in the future:

- Create more charts to visualize the results.
- Export the analysis to Excel.
- Build an interactive dashboard with Power BI.
- Create visualizations with Plotly.
- Organize the code into functions.

---

## Author

**Rafael Bonadia**

Python | Pandas | SQL | Excel | Power BI

Currently learning Data Analytics and building projects to improve my skills.