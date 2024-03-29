# -*- coding: utf-8 -*-
"""Day72.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KAH5dT56Sk2tvuBPc3peHfMZinT3qQhW
"""

import pandas as pd

df = pd.read_csv('/content/salaries_by_college_major.csv')

df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[43]

clean_df['Undergraduate Major'][43]

clean_df.loc[43]

clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmax()]

clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

clean_df['Starting Median Salary'].min()

clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmin()]

clean_df['Mid-Career Median Salary'].min()

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

clean_df.insert(1, 'Spread', spread_col)



clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

high_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
high_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

great_spread = clean_df.sort_values('Spread', ascending=False)
great_spread[['Undergraduate Major', 'Spread']].head()

clean_df.groupby('Group').count()

clean_df.groupby('Group').mean()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()

# Main dataframe to collect all data
table_from_html = pd.read_html("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
df = table_from_html[0].copy()
df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]

# Add tables from other pages to main dataframe
for page_no in range(2, 35):
    table_from_html = pd.read_html(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_no}")
    page_df = table_from_html[0].copy()
    page_df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
    df = df.append(page_df, ignore_index=True)

# Select necessary columns only
df = df[["Major", "EarlyCareerPay", "MidCareerPay"]]

# Clean columns
df.replace({"^Major:": "", "^Early Career Pay:\$": "", "^Mid-Career Pay:\$": "", ",": ""}, regex=True, inplace=True)

# Change datatype of numeric columns
df[["EarlyCareerPay", "MidCareerPay"]] = df[["EarlyCareerPay", "MidCareerPay"]].apply(pd.to_numeric)

df.head()