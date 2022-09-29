import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', 8)

# Read CSV files from 3 hospitals
general, prenatal, sports = pd.read_csv('test/general.csv'), pd.read_csv('test/prenatal.csv'), pd.read_csv(
    'test/sports.csv')

# Change columns + merge tables + delete unnamed columns and empty rows + standardize gender to f/m
hosp_df = pd.concat(
    [general, prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}),
     sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})], ignore_index=True).drop(
    columns='Unnamed: 0').dropna(axis=0, how='all').replace(['female', 'male', 'woman', 'man'], ['f', 'm', 'f', 'm'])

# Fill NaN values
hosp_df.fillna({'gender': 'f', 'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0,
                'ultrasound': 0, 'mri': 0, 'xray': 0, 'children': 0, 'months': 0}, inplace=True)

# First question - What is the most common age of a patient among all hospitals?
hosp_df.plot(y='age', kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()
print('The answer to the 1st question: 15-35')

# Second question - What is the most common diagnosis among patients in all hospitals?
hosp_df['diagnosis'].value_counts().plot(kind='pie')
plt.show()
print('The answer to the 2nd question: pregnancy')

# Third question - What is the main reason for the gap in values? Why there are two peaks, which correspond to the
# relatively small and big values?
ax = sns.violinplot(x="hospital", y="height", data=hosp_df)
ax.set_title('Distribution of height', fontsize=16)
plt.show()
print('The answer to the 3rd question: the main reason for the gap in values is the different measurement unit of '
      'height in hospitals')
