import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    database = 'postgres',
    user = 'postgres',
    password = 'muttdata'
)

cursor = conn.cursor()

query_str = 'DROP TABLE IF EXISTS coins_data'
cursor.execute(query_str)
conn.commit()
query_str = 'CREATE TABLE coins_data(' \
            'coin_id varchar(30),' \
            'usd_price float,' \
            'file_date date,' \
            'json_response json)'

cursor.execute(query_str)
conn.commit()

query_str = 'DROP TABLE IF EXISTS coins_agg'
cursor.execute(query_str)
conn.commit()
query_str = 'CREATE TABLE coins_agg(' \
            'coin_id varchar(30),' \
            'year_agg int,' \
            'month_agg int,' \
            'maximum float,' \
            'minimum  float)'

cursor.execute(query_str)
conn.commit()
cursor.close()
conn.close()
