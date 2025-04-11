import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ 1. Load the Data
orders = pd.read_csv(r'DVivek katariyaSkillsdata analystE-commerce data analysis project 1List of Orders.csv')
order_details = pd.read_csv(r'DVivek katariyaSkillsdata analystE-commerce data analysis project 1Order Details.csv')
targets = pd.read_csv(r'DVivek katariyaSkillsdata analystE-commerce data analysis project 1Sales target.csv')

# ✅ 2. Clean Column Names
orders.columns = orders.columns.str.strip()
order_details.columns = order_details.columns.str.strip()
targets.columns = targets.columns.str.strip()

# ✅ 3. Convert Order Date
orders['Order Date'] = pd.to_datetime(orders['Order Date'], dayfirst=True)

# ✅ 4. Identify correct columns for Unit Price and Quantity
unit_price_col = [col for col in order_details.columns if 'unit' in col.lower() and 'price' in col.lower()]
qty_col = [col for col in order_details.columns if 'quantity' in col.lower()]

# ✅ 5. Calculate Total Price
if unit_price_col and qty_col
    order_details['Total Price'] = order_details[unit_price_col[0]]  order_details[qty_col[0]]
else
    raise KeyError(Could not find 'Unit Price' or 'Quantity' columns.)

# ✅ 6. Merge Orders with Details
df = pd.merge(order_details, orders, on='Order ID', how='inner')

# ✅ 7. Total Sales by Product
product_perf = df.groupby('Order ID')['Total Price'].sum().reset_index()
product_perf = product_perf.sort_values(by='Total Price', ascending=False)

# ✅ 8. Monthly Sales Trend per Product
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby(['Order ID', 'Month'])['Total Price'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

# ✅ 9. ABC Analysis
product_perf['Cumulative %'] = product_perf['Total Price'].cumsum()  product_perf['Total Price'].sum()
product_perf['ABC Category'] = pd.cut(product_perf['Cumulative %'], bins=[0, 0.2, 0.5, 1.0], labels=['A', 'B', 'C'])

# ✅ 10. Merge with Target
if 'Order ID' in targets.columns
    perf_vs_target = pd.merge(product_perf, targets, on='Order ID', how='left')
else
    perf_vs_target = product_perf.copy()

# ✅ 11. Visualizations

# 1. Top 10 Products by Sales
plt.figure(figsize=(10,5))
sns.barplot(data=product_perf.head(10), x='Total Price', y='Order ID', hue='ABC Category', palette='viridis')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Order ID')
plt.tight_layout()
plt.show()

# 2. ABC Category Distribution
plt.figure(figsize=(5,4))
sns.countplot(data=product_perf, x='ABC Category', palette='Set2')
plt.title('Product Distribution by ABC Category')
plt.show()

# 3. Monthly Trend for Top Product
top_product = product_perf.iloc[0]['Order ID']
top_trend = monthly_sales[monthly_sales['Order ID'] == top_product]

plt.figure(figsize=(10,4))
sns.lineplot(data=top_trend, x='Month', y='Total Price', marker='o')
plt.title(f'Monthly Sales Trend for Top Product {top_product}')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Cumulative Sales Contribution Plot (Optional)
plt.figure(figsize=(8,4))
sns.lineplot(data=product_perf.sort_values(by='Total Price', ascending=False).reset_index(drop=True),
             y='Cumulative %', x=product_perf.index)
plt.title(Cumulative Sales Contribution)
plt.ylabel(Cumulative % of Sales)
plt.xlabel(Products (Ranked))
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ 12. Save cleaned script for download
cleaned_code = '''your cleaned Python script goes here as a multiline string'''
with open(ecommerce_analysis_cleaned.py, w, encoding=utf-8) as f
    f.write(cleaned_code)
print(✅ Cleaned script saved as 'ecommerce_analysis_cleaned.py')
