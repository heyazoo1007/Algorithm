-- 코드를 입력하세요
-- 9시부터 19시까지 시간대별로 로우 수 
select date_format(DATETIME, "%H") AS hour, count(*)
from ANIMAL_OUTS
where date_format(DATETIME, "%H") between '09' and '19'
group by hour
order by hour;