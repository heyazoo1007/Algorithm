-- 코드를 입력하세요
SELECT ii.ingredient_type, sum(fh.total_order) as total_order
from first_half fh
join icecream_info ii 
on ii.flavor = fh.flavor
group by ingredient_type
order by fh.total_order;