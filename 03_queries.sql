--1.	Get the average price for each coin by month.

select extract(year from file_date) year_var, 
       extract(month from file_date) month_var, 
       coin_id,
       avg(usd_price),
       sum(usd_price),
       count(1)
 from coins_data
 group by extract(year from file_date), 
       extract(month from file_date), 
       coin_id
 order by year_var, month_var, coin_id
       

--2.	Calculate for each coin, on average, how much its price has increased after it had dropped 
--     consecutively for more than 3 days. In the same result set include the current market cap in USD 
--    (obtainable from the JSON-typed column).  Use any time span that you find best. 

DROP TABLE IF EXISTS temp_coins_data_01
create table temp_coins_data_01 as
select a.coin_id, a.usd_price price_day1, b.usd_price price_day2,  a.json_response
from 
(select * from coins_data where file_date = '2022-09-30') a,
(select * from coins_data where file_date = '2022-10-01') b
where a.coin_id = b.coin_id
and b.usd_price < a.usd_price

DROP TABLE IF EXISTS temp_coins_data_02
create table temp_coins_data_02 as
select a.coin_id, a.price_day1, a.price_day2, b.usd_price price_day3, a.json_response
from 
temp_coins_data_01 a,
(select * from coins_data where file_date = '2022-10-02') b
where a.coin_id = b.coin_id
and b.usd_price < a.price_day2

DROP TABLE IF EXISTS temp_coins_data_03
create table temp_coins_data_03 as
select a.coin_id, a.price_day1, a.price_day2, a.price_day3, b.usd_price price_day4, a.json_response
from 
temp_coins_data_02 a,
(select * from coins_data where file_date = '2022-10-03') b
where a.coin_id = b.coin_id
and b.usd_price < a.price_day3


select a.coin_id, a.avg_price - b.price_day4 price_inc, a.avg_price avg_price_inc, b.price_day4 price_drop, 
b.json_response::json->'market_data'->'market_cap'->'usd' as market_cap_usd
from
(
select b.coin_id, avg(usd_price) avg_price
from temp_coins_data_03 a, coins_data b
where a.coin_id = b.coin_id
and b.file_date between '2022-10-04' and '2022-10-15'
group by b.coin_id
) a,
temp_coins_data_03 b
where a.coin_id = b.coin_id


