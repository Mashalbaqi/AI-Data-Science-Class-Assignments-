import pandas as pd
#check the missing data
df =pd.read_csv(r'C:\Users\ACC\Desktop\training\train.csv')
                                                    #Handling Missing Data
#show missing data
print("Missing values per column:\n", df.isnull().sum())



#dropping rows with any missing values
df_dropped_rows = df.dropna()
print("\nshow the data after dropping rows with missing values:")
print(df_dropped_rows)



#droping Columns with any missing Data
df_dropped_cols = df.dropna(axis=1, how='all')
print("\nshow the data after dropping columns with all values missing:")
print(df_dropped_cols)



# fill the missing values with a specific value
df_filled_value = df.fillna(22)
print("\nshow the data after filling missing values with 22:")
print(df_filled_value)


# Creating a new Column

df['new_column'] = "new data"
print(df)
                                                         #Filtiring
#filtiring the passengers ID above 780
filtered_df1 = df[df['PassengerId'] > 780]
print("\nFiltered rows where 'PassengerId' > 50:")
print(filtered_df1)

#shows the data from Embarked Column with value S
filtered_df2 = df[df['Embarked'] == 'S']
print("\nFiltered rows where 'Embarked' equals 'S':")
print(filtered_df2)


























