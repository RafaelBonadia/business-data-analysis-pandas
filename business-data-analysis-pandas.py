import pandas as pd
import matplotlib.pyplot as plt


# Files path
# I used r before the path to avoid problems with backslashes in Windows
employees_file = r'01 Project_data\CadastroFuncionarios.csv'
clients_file = r'01 Project_data\CadastroClientes.csv'
services_file = r'01 Project_data\BaseServi�osPrestados.xlsx'


# Reading the CSV files
# sep=';' because the files use semicolon as separator
# decimal=',' because the numbers use comma as decimal separator
employees_df = pd.read_csv(
    employees_file,
    sep=';',
    decimal=','
)

clients_df = pd.read_csv(
    clients_file,
    sep=';',
    decimal=','
)


# Reading the Excel file
# Excel files don't need sep because Pandas already understands the structure
services_df = pd.read_excel(
    services_file
)


# Printing the tables to check if everything was loaded correctly
print("\n" + "=" * 60 + "\n")
print(services_df)

print("\n" + "=" * 60 + "\n")
print(clients_df)

print("\n" + "=" * 60 + "\n")
print(employees_df)


print("\n" + "=" * 60 + "\n")


# ============================================================
# 1. Total employee payroll cost
# ============================================================

# The company wants to know how much it spends with employees.
# The calculation includes:
# Salary + Taxes + Benefits + Transportation + Meal allowance


# Removing columns that are not useful for this analysis
employees_df = employees_df.drop(
    ['Estado Civil', 'Cargo'],
    axis=1
)


# Selecting all columns related to employee costs
# axis=1 means Pandas will calculate the sum by row
# If I used axis=0, it would sum each column separately

employee_total_cost = employees_df[
    [
        'Salario Base',
        'Impostos',
        'Beneficios',
        'VT',
        'VR'
    ]
].sum(axis=1)


# Creating a new column with the total cost of each employee
employees_df['TOTAL'] = employee_total_cost


# Sum all employees to find the company's total cost
total_payroll = employee_total_cost.sum()


print(employees_df[['TOTAL']])

print(
    f"Total payroll cost: R$ {total_payroll:,.2f}"
)


print("\n" + "=" * 60 + "\n")


# ============================================================
# 2. Company total revenue
# ============================================================

# To calculate revenue, I need to connect clients and services tables.
# Both datasets have ID Cliente, so I used merge to combine them.

contracts_df = clients_df.merge(
    services_df,
    on='ID Cliente'
)


# Calculating the revenue of each contract
# Monthly contract value multiplied by contract duration

contract_revenue = (
    contracts_df['Valor Contrato Mensal'] *
    contracts_df['Tempo Total de Contrato (Meses)']
)


# Adding all contracts revenue together
total_revenue = contract_revenue.sum()


print(
    f"Total company revenue: R$ {total_revenue:,.2f}"
)


print("\n" + "=" * 60 + "\n")


# ============================================================
# 3. Percentage of employees who closed contracts
# ============================================================

# In the services dataset we have the employees who closed contracts.
# I need to compare this number with the total number of employees.

employees_with_contracts = services_df[
    'ID Funcionário'
].nunique()


total_employees = employees_df[
    'ID Funcionário'
].nunique()


closing_rate = (
    employees_with_contracts /
    total_employees
)


print(
    f"Employee closing rate: {closing_rate * 100:.2f}%"
)


print("\n" + "=" * 60 + "\n")

# ============================================================
# 4. Total contracts closed by department
# ============================================================

# The services dataset only has the employee ID.
# I need to connect it with the employees dataset
# to know which department closed each contract.

contracts_by_department_df = services_df[
    ['ID Funcionário']
].merge(
    employees_df[
        ['ID Funcionário', 'Area']
    ],
    on='ID Funcionário'
)


# value_counts() counts how many times each department appears
# This shows how many contracts each department closed

contracts_per_department = (
    contracts_by_department_df['Area']
    .value_counts()
)


print(contracts_per_department)


print("\n" + "=" * 60 + "\n")


# ============================================================
# 5. Number of employees per department
# ============================================================

# Counting how many employees exist in each department

employees_per_department = (
    employees_df['Area']
    .value_counts()
)


print(
    f"Employees per department:\n{employees_per_department}"
)


# I could also create a bar chart to visualize this information

# employees_per_department.plot(kind='bar')
# plt.show()


print("\n" + "=" * 60 + "\n")


# ============================================================
# 6. Average monthly contract value
# ============================================================

# Calculating the average monthly value of all contracts
# using mean()

average_monthly_contract = (
    clients_df['Valor Contrato Mensal']
    .mean()
)


print(
    f"Average monthly contract value: R$ {average_monthly_contract:,.2f}"
)


print("\n" + "=" * 60 + "\n")


# ============================================================
# Final notes
# ============================================================

# This project helped me practice:
# - Reading CSV and Excel files
# - Cleaning data
# - Removing unnecessary columns
# - Creating new columns
# - Merging different datasets
# - Using Pandas functions like sum(), mean(), nunique() and value_counts()
# - Answering business questions with data