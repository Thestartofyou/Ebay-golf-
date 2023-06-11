import pandas as pd

# Load the eBay sales data (CSV file)
ebay_data = pd.read_csv('ebay_sales_data.csv')

# Display the first few rows of the dataset
print("First 5 rows of the eBay sales data:")
print(ebay_data.head())

# Get the total number of sales records
total_sales = len(ebay_data)
print("Total number of sales records:", total_sales)

# Get the average price of golf clubs sold
average_price = ebay_data['Price'].mean()
print("Average price of golf clubs sold:", average_price)

# Get the maximum and minimum prices of golf clubs sold
max_price = ebay_data['Price'].max()
min_price = ebay_data['Price'].min()
print("Maximum price of golf clubs sold:", max_price)
print("Minimum price of golf clubs sold:", min_price)

# Calculate the total revenue from golf club sales
total_revenue = ebay_data['Price'].sum()
print("Total revenue from golf club sales:", total_revenue)

# Get the most common golf club brands
top_brands = ebay_data['Brand'].value_counts().head(5)
print("Top 5 most common golf club brands:")
print(top_brands)

# Calculate the average duration of sales listings
ebay_data['Duration'] = pd.to_timedelta(ebay_data['End Date']) - pd.to_timedelta(ebay_data['Start Date'])
average_duration = ebay_data['Duration'].mean()
print("Average duration of sales listings:", average_duration)

# Calculate the number of sales per day of the week
ebay_data['Start Date'] = pd.to_datetime(ebay_data['Start Date'])
sales_per_day = ebay_data['Start Date'].dt.day_name().value_counts()
print("Number of sales per day of the week:")
print(sales_per_day)
