import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def return_dict(res_dict):
    new_dict = {}
    for k,v in res_dict.items():
        flag = 0
        for val in v:
            if val is None:
                flag = 1
            else:
                flag = 0 
                break
        if flag == 0:
            new_dict[k] = v
    return new_dict

@data_loader
def load_data_from_api(*args, **kwargs):
    
    headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
    }
    
    """
    Template for loading data from API
    """
    url = "https://stockanalysis.com/api/symbol/s/aapl/financials/r/q"


    response = requests.get(url, headers=headers)

    json_response = response.json()
    res_dict = json_response['data']['data']
    new_dict = return_dict(res_dict)
    return pd.DataFrame.from_dict(new_dict)


@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
