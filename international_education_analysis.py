import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv('International_Education_Costs.csv',sep=",")

#average tuition cost by country
avg_tuition = df.groupby('Country')['Tuition_USD'].mean().round(0).astype(int).sort_values(ascending=False).reset_index()
#average rent cost by country
avg_rent = df.groupby('Country')['Rent_USD'].mean().round(0).astype(int).sort_values(ascending=False).reset_index()

plt.figure(figsize=(12,6))
sns.barplot(data=avg_tuition, x='Country', y='Tuition_USD', palette='viridis')
plt.title('Average Tuition Cost by Country')
plt.xticks(rotation=90,fontsize=11)
plt.tight_layout()
plt.savefig('average_tuition_cost_by_country.png')
plt.show()
 
plt.figure(figsize=(12,6))
sns.barplot(data=avg_rent, x='Country', y='Rent_USD', palette='magma')
plt.title('Average Rent Cost by Country')
plt.xticks(rotation=90,fontsize=11)
plt.tight_layout()
plt.savefig('average_rent_cost_by_country.png')
plt.show()

df['Total_Annual_Cost'] = (df['Tuition_USD'] + (df['Rent_USD'] * 12) + df['Visa_Fee_USD'] + df['Insurance_USD'])

sorted_unis = df.groupby('University', as_index=False)['Total_Annual_Cost'].mean()
sorted_unis = sorted_unis.sort_values(by='Total_Annual_Cost')

bottom5 = sorted_unis.head(3)

middle_index = len(sorted_unis) // 2
middle5 = sorted_unis.iloc[middle_index-1:middle_index+2]

top5 = sorted_unis.tail(3)

compare_unis = pd.concat([top5, middle5, bottom5]).sort_values(by='Total_Annual_Cost', ascending=False).reset_index(drop=True)

compare_unis['Group'] = ['Top']*3 + ['Middle']*3 + ['Bottom']*3

plt.figure(figsize=(12,7))
sns.barplot(data=compare_unis, 
            x='Total_Annual_Cost', 
            y='University', 
            hue='Group', 
            dodge=False,
            palette='Set2')
plt.title('Top 3 vs Middle 3 vs Bottom 3 Universities by Total Annual Cost')
plt.xlabel('Total Annual Cost (USD)')
plt.ylabel('University')
plt.tight_layout()
plt.savefig('universities_total_annual_cost_comparison.png')
plt.show()