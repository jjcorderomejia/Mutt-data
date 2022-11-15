 

python getting_crypto_data_01.py bitcoin database $(date -d "-4 days" +%d-%m-%Y)
python getting_crypto_data_01.py cardano database $(date -d "-65 days" +%d-%m-%Y) $(date -d "-1 days" +%d-%m-%Y)


sudo service docker start
sudo service docker status
docker run --name postgres-db-mutt -e POSTGRES_PASSWORD=muttdata -p 5432:5432 -d postgres
docker container ls
psql -h localhost  -p 5432  -d postgres  -U postgres  -W

sudo apt-get install python3.8
sudo apt-get install python3.8-venv
python3.8 -m venv mutt-venv
source mutt-venv/bin/activate

sudo apt install postgresql-client-common

pip install sqlalchemy
pip install psycopg2-binary

pip install tweepy
pip install dotenv
pip3 list
pip3 install python-dotenv
pip install pyspark
