import os
import pandas as pd


def clean_data_extract():
    data_path_economy = '/tmp/economy.csv'
    data_path_business = '/tmp/business.csv'
    ## Load data into DataFrame
    data_economic = pd.read_csv(data_path_economy, header=None)
    data_business = pd.read_csv(data_path_business, header=None)
    
    data_economic['stop'] = data_economic['stop'].str.replace(r'[\t"]', '', regex=True)
    data_economic['stop'] = data_economic['stop'].str.replace(r'[\n"]', '', regex=True)
    data_economic['stop'] = data_economic['stop'].str.replace(' ', '', regex=True)

    data_business['stop'] = data_business['stop'].str.replace(r'[\t"]', '', regex=True)
    data_business['stop'] = data_business['stop'].str.replace(r'[\n"]', '', regex=True)
    data_business['stop'] = data_business['stop'].str.replace(' ', '', regex=True)

    data_economic.to_csv(data_path_economy, index=False, mode='w')
    data_business.to_csv(data_path_business, index=False, mode='w')



    
