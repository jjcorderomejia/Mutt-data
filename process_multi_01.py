import logging
import datetime
from process_one_01 import process_one_file
import time

def process_multi_file(id_param, save_param,  date_begin, date_end):
    logging.basicConfig(filename=f'getting-crypto-data.log',
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Welcome to the 'Getting crypto multi data' app")
    date_var_begin = datetime.datetime.strptime(date_begin, "%d-%m-%Y")
    date_var_end = datetime.datetime.strptime(date_end, "%d-%m-%Y")
    while date_var_begin <= date_var_end:
        process_one_file(id_param, save_param, date_var_begin.strftime("%d-%m-%Y"))
        date_var_begin = date_var_begin + datetime.timedelta(days=1)
        time.sleep(2)
    logger.debug("End 'Getting crypto multi data' app")

