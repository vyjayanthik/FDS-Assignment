import pandas as pd #Inputing file, Data-processing
import numpy as np #Numerical operation
import matplotlib.pyplot as plt #creating visualizations
from scipy.stats import norm #For numerical integration

# Replace the following with your actual sample data
df = pd.read_csv('data4-2.csv', header=None, names=['salary'])
sample_data = df['salary']

plt.figure(figsize=(10, 6))  # Specify the figure size

# Create histogram with a different color (e.g., green)
plt.hist(sample_data, bins=30, density=True, alpha=0.5, color='darkcyan', label='Sample Data')

# Fit a normal distribution to the data
mu, std = norm.fit(sample_data)

# p = norm.pdf(x, mu, std)
# plt.plot(x, p, 'purple', linewidth=2, label=f'Fit results: $\mu={mu:.2f}$, $\sigma={std:.2f}$')

# Calculate mean annual salary (~W) and use a different color (e.g., orange)
mean_salary = np.mean(sample_data)
plt.axvline(mean_salary, color='orange', linestyle='--', linewidth=2, label=f'Mean Salary: ${mean_salary:.2f}')

# Calculate X such that 25% of people have a salary below X with a different color (e.g., blue)
X = norm.ppf(0.25, mu, std)
plt.axvline(X, color='blue', linestyle='--', linewidth=2, label=f'X for 25% below: ${X:.2f}')

# Add labels, title, and legend
plt.xlabel('Annual Salary')
plt.ylabel('Probability Density')
plt.title('Salary Distribution Analysis')
plt.legend()

# Show the plot
plt.show()
