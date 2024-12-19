import pandas as pd

FILEPATH = './API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_11/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_11.csv'
countries_list = ['colombias']
def open_file(filepath):
        df = pd.read_csv(filepath, skiprows=3)
        df = df.drop(df.columns[1:44], axis=1)
        return df
        
file = open_file(FILEPATH)
print(file)

def filter_countries(dataframe):
        pass