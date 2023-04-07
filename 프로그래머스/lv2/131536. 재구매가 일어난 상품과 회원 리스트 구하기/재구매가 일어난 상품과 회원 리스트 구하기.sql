-- 코드를 입력하세요
-- 같은 회원 ID, 상품 Id 가 반복됨 -> 재구매
-- order by user_id, product_id;
SELECT user_id, product_id
from online_sale
group by user_id, product_id
having count(*) >= 2
order by user_id asc, product_id desc;