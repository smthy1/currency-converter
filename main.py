from api import converter
from database import records_list, create_table, specific_query

create_table()


while True:
    print('== Currency converter ==')
    print('1. Check currency value')
    print('2. List of records')
    print('3. Specific query')
    print('4. Exit')
    
    select = input('Choose: ')
       
    if select == '1':
        converter()
    
    elif select == '2':
        records_list()
    
    elif select == '3':
        specific_query()

    elif select == '4':
        print('Shutting down...')
        break
    
    else:
        print('Invalid option. Try again.')