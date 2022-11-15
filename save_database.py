import psycopg2
import json
from datetime import datetime
import logging

def save_db_process(response,date_param):
    conn = psycopg2.connect(
        host = 'localhost',
        port = 5432,
        database = 'postgres',
        user = 'postgres',
        password = 'muttdata'
    )

    logging.basicConfig(filename=f'getting-crypto-data.log',
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    repos = json.loads(response.content.decode('utf-8'))
    cursor = conn.cursor()


    #print(query_str)

    try:
        query_str = f'insert into coins_data ' \
                    f'(coin_id,usd_price,file_date,json_response) ' \
                    f'values(' \
                    f"'{repos['id']}'," \
                    f'{float([val for key, val in repos["market_data"]["current_price"].items() if key == "usd"][0])},' \
                    f"'{datetime.strptime(date_param, '%d-%m-%Y').date()}'," \
                    f"'{response.content.decode('utf-8')}')"

        cursor.execute(query_str)
        conn.commit()

    except KeyError:
        logger.debug(f'Can not be saved day {date_param} because key error in json data')
        cursor.close()
        conn.close()
        return


    query_del = 'delete from coins_agg a ' \
                'where exists(select 1 ' \
			    'from coins_data b ' \
			    'where a.year_agg = extract(year from b.file_date) ' \
			    'and a.month_agg = extract(month from b.file_date)' \
			    ')'

    cursor.execute(query_del)
    conn.commit()

    query_agg = 'insert into coins_agg ' \
                '(coin_id, year_agg, month_agg, maximum, minimum) ' \
                'select ' \
                'coin_id, extract(year from file_date), extract(month from file_date), ' \
                'max(usd_price), min(usd_price) ' \
                'from coins_data ' \
                'group by coin_id, extract(year from file_date), extract(month from file_date)'

    cursor.execute(query_agg)
    conn.commit()
    cursor.close()
    conn.close()
