import requests
from dotenv import load_dotenv
from database import add_record
import os

load_dotenv()


def converter():
    currency_base = input('Define currency base: ').strip().lower()
    currency_target = input('Define currency target: ').strip().lower()
    key = os.getenv('EXCHANGERATE_API_KEY')
    
    if not key:
        print('Error: key not configured. Add the key in the .env file.')
        exit(1)

    url = f'https://v6.exchangerate-api.com/v6/{key}/pair/{currency_base}/{currency_target}'

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Erro de requisição {response.status_code}')
            return
        
        data = response.json()

        if data['result'] != 'success':
            print(f'Conversion error: {data.get('error-type', 'unknown error')}')
            return
        
        base_code = data['base_code']
        target_code = data['target_code']
        conversion_rate = data['conversion_rate']
        
        print('== Currency converter ==')
        print(f"{base_code} to {target_code}: {conversion_rate:.2f}")
        print('='*100)
        
        pick = input('Do you want to add to the records list? [Y/N]\nSelect: ').strip().lower()
        
        while pick not in 'yn':
            print('Invalid answer. Try again.')
            pick = input('Do you want to add to the records list? [Y/N]\nSelect: ').strip().lower()
        
        if pick == 'y':
            add_record(base_code, target_code, conversion_rate)

    except Exception as erro:
        print(f'{erro}')