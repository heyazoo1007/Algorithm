-- 코드를 입력하세요
-- 가격을 만원 단위로 나누기 
SELECT TRUNCATE(price, -4) as price_group, count(*) as products
from product
group by price_group
order by price_group;