import requests
import pandas as pd
import time

def lambda_handler(event, context):
    print('Begin!')

    myname = 'henry'

    url = f'https://api.nationalize.io/?name={myname}'

    r = requests.get(url).json()
    print(r)
    print('Keys are:')
    print(r.keys())

    df = pd.DataFrame(r['country'])
    print(df.sort_values(by=['probability'], ascending=False))

if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)
