-- 코드를 입력하세요
-- 상품코드 별 매출액 합계를 출력 
-- 결과는 매출액을 기준으로 desc 정렬, product_code asc 
SELECT p.product_code, sum(os.sales_amount) * p.price as SALES
from product p 
join offline_sale os
on p.product_id = os.product_id
group by p.product_code
order by sum(os.sales_amount) * p.price desc, p.product_code asc;
