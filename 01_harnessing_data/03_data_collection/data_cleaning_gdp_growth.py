import pandas as pd

FILEPATH = './API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_11/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_11.csv'
countries = [
    "United States", "Hong Kong", "Germany", "United Kingdom", "China", 
    "Costa Rica", "Ecuador", "Venezuela", "Peru", "El Salvador", 
    "Brazil", "Mexico", "France", "South Korea", "India", 
    "Italy", "Chile", "Argentina", "Netherlands", "Spain", 
    "Japan", "Indonesia", "United Arab Emirates", "Canada", 
    "Panama", "Russia", "Switzerland", "Australia", "Singapore"
]
years = [
        '2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
        2020, 2021, 2022, 203
        ]
def open_file(filepath):
        df = pd.read_csv(filepath, skiprows=3)
        return df

def filter_countries(df: pd.DataFrame, countries_list: list) -> pd.DataFrame:
    df = df.drop(df.columns[1:4], axis=1)
    # Use `isin` to filter rows
    filtered_df = dataframe[dataframe['Country Name'].isin(countries_list)]
    return filtered_df

        
data_cleaned = open_file(FILEPATH)
data_filtered = filter_countries(data_cleaned, countries)
print(data_filtered)

