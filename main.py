import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: Create NumPy array and calculate mean
numbers = np.arange(1, 11)
mean_value = np.mean(numbers)
print(f"\nTask 1 - NumPy Array Mean:")
print(f"Array: {numbers}")
print(f"Mean: {mean_value}")

# Task 2: Create and analyze DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000]
}
df = pd.DataFrame(data)
print(f"\nTask 2 - DataFrame Summary Statistics:")
print(df.describe())

# Task 3: Fetch data from public API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
bitcoin_price = response.json()['bpi']['USD']['rate']
print(f"\nTask 3 - Bitcoin Price:")
print(f"Current Bitcoin Price (USD): {bitcoin_price}")

# Task 4: Create a line plot
x = range(10)
y = [i**2 for i in x]
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o')
plt.title('Simple Line Graph: Square Numbers')
plt.xlabel('Number')
plt.ylabel('Square')
plt.grid(True)
plt.savefig('line_plot.png')
plt.close()