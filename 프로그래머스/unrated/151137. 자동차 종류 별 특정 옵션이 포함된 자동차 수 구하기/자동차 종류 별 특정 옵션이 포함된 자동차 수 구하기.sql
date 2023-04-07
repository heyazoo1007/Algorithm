-- 코드를 입력하세요
-- options in ('통풍시트', '열선시트', '가죽시트')
-- 자동차 타입 별로, 각 몇 대인지
SELECT car_type, count(*) as CARS
from car_rental_company_car 
where options like '%통풍시트%' or options like '%열선시트%' or options like '%가죽시트%' 
group by car_type
order by car_type;