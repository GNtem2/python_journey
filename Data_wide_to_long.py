import pandas as pd
import numpy as np
import sys


path = r'C:\Users\andre\Desktop\FFR_data\Pressure_tracing-deID.csv'
df = pd.read_csv(path)


# create a unique ID
df['id'] = df.index

# rename columns
col = ['ID', 'Pos_Neg', 'Def']
for i in range(0, len(df.iloc[0, 3:-1])):
    col.append('index{var}'.format(var=i))
col.append('id')
df.columns = col

# convert data into long format
df = pd.wide_to_long(df, stubnames='index', i='id', j='col')

# create separate col for each observation
df_final = pd.DataFrame()
df_id = df.groupby(['ID'])
for i, row in enumerate(df_id):
    df_def = row[1].groupby(['Def'])
    if i == 0:
        for j, col in enumerate(df_def):
            if j == 0:
                cols_new = pd.DataFrame({'ID': list(col[1].loc[:, 'ID']), 'Pos_Neg': list(col[1].loc[:, 'Pos_Neg'])}, columns=['ID', 'Pos_Neg'])
                df_final = pd.concat([df_final, cols_new], axis=1)
                HR = pd.DataFrame(list(col[1].iloc[:, 3]), columns=[str(col[0])])
                df_final = pd.concat([df_final, HR], axis=1)
            else:
                new_obs = (pd.DataFrame(list(col[1].iloc[:, 3]), columns=[str(col[0])]))
                df_final = pd.concat([df_final, new_obs], axis=1)
    else:
        df_hold = pd.DataFrame()
        for j, col in enumerate(df_def):
            if j == 0:
                cols_new = pd.DataFrame({'ID': list(col[1].loc[:, 'ID']), 'Pos_Neg': list(col[1].loc[:, 'Pos_Neg'])}, columns=['ID', 'Pos_Neg'])
                df_hold = pd.concat([df_hold, cols_new], axis=1)
                HR = pd.DataFrame(list(col[1].iloc[:, 3]), columns=[str(col[0])])
                df_hold = pd.concat([df_hold, HR], axis=1)
            else:
                new_obs = (pd.DataFrame(list(col[1].iloc[:, 3]), columns=[str(col[0])]))
                df_hold = pd.concat([df_hold, new_obs], axis=1)
        df_final = pd.concat([df_final, df_hold], axis=0)
df_final = df_final.dropna()
df_final.to_csv(r'C:\Users\andre\Desktop\FFR_data\Tracing_long_AC.csv')


