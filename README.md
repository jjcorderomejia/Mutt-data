# exam-juan-cordero
Please review this instructions

Definitions:
The solution was developed using the next tools:
* Local environment Ubuntu operative system
* psql as terminal-based front-end to PostgreSQL

![image](https://user-images.githubusercontent.com/108158389/198953157-f4ac03ba-dd0c-496d-9ed7-91c9482ce471.png)

* SQL Workbench for Postgres development

![image](https://user-images.githubusercontent.com/108158389/198953382-f697f870-e220-4ac1-ab58-e1c66e77d8d4.png)

* Pycharm as IDE developing solution

![image](https://user-images.githubusercontent.com/108158389/198952601-e25b6644-d91f-4772-a777-fe066aafeef2.png)


The file commands.cmd contains all necessary commands executed prior to start developing. It is  necessary to copy all files in one specific folder in ubuntu filesystem and ran all commands from there.

# PROJECT ANSWERS

## 1. Getting crypto token data 

For this item please check the files:
- getting_crypto_data_01.py --> Main process that is in charge of executing the solutions for processing one or multi file
- process_one_01.py  --> It process one file
- process_multi_01.py  --> It processes multiple files

for executing the filegetting_crypto_data_01.py please in command line execute this sentence 
### For processing just one date
it requires 3 parameters
- 01: coin_type: bitcoin / ethereum / cardano
- 02: destination:  filesystem / database --> This parameter allows to process either to filesystem or postgres database
- 03: date begin  format dd-mm-yyyy

Examples

python getting_crypto_data_01.py bitcoin database $(date -d "-4 days" +%d-%m-%Y)

python getting_crypto_data_01.py bitcoin filesystem 10-06-2022

### For processing  a range date
it requires 4 parameters
- 01: coin_type: bitcoin / ethereum / cardano
- 02: destination:  filesystem / database
- 03: date begin
- 04: date end

Example:

python getting_crypto_data_01.py cardano database $(date -d "-65 days" +%d-%m-%Y) $(date -d "-1 days" +%d-%m-%Y)

## 2. Loading data into the database

For this item please check the files:
create_table_02.py --> It creates two tables structures in postgres database.
It can be executed standalone in command line prior to generate the data.

Example

python create_table_02.py

save_database.py  --> It is integrated with the solution from first requirement. It contains the logic for save the json files into postgres database

Example

python getting_crypto_data_01.py cardano database $(date -d "-65 days" +%d-%m-%Y) $(date -d "-1 days" +%d-%m-%Y)

## 3. Analysing coin data with SQL

For this item please check the file:

03_queries.sql --> It contains SQL Postgres logic for two questions resolutions for this Requirement.  This query was run in SQL Workbench. Please see my configuration

![image](https://user-images.githubusercontent.com/108158389/198957228-4df7abdc-c7da-442a-8642-857f18b5bc4c.png)

## 4. Python/Spark and Twitter 

For this item please check the files:

twitter_04.py --> It containts python resolution for taks 1. It can be executed standalone in command line.
.env  --> Credentials file for accesing twitter API.

It receives one parameter:
###01: query: it is any query that is going to be searched on twitter

Example
python twitter_04.py guayaquil

spark_04.py  --> It containts python resolution for taks 2

python spark_04.py
