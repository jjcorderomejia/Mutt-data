import requests
import logging
from save_database import save_db_process

def process_one_file(id_param, save_param, date_param):
    logging.basicConfig(filename=f'getting-crypto-data.log',
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Welcome to the 'Getting crypto data' app")
    link = f'https://api.coingecko.com/api/v3/coins/{id_param}/history?date={date_param}'
    logger.debug(f'The content to be saved is: {link}')
    response = requests.get(link)
    logger.debug(f'The response por getting the content is: {response}')
    if save_param == 'filesystem':
        dest_file = f'getting-crypto-data-{date_param}.json'
        # create the file "getting-crypto-data-dd-mm-yyyy.json" and save the content in the new file
        with open(dest_file, "w") as f:
            f.write(response.text)
        logger.debug(f'Destination file {dest_file} properly saved in your current path')
    if save_param == 'database':
        save_db_process(response,date_param)
    logger.debug(f'Please review logging file getting-crypto-data.log in your current path, Thank you')
