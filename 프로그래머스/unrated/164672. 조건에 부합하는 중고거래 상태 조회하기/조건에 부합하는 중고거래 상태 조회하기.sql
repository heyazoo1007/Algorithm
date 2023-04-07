-- 코드를 입력하세요
-- 등록일이 2022-10-05인 로우, 거래 상태별로 분류하기 
-- order by board_id desc;
SELECT board_id, writer_id, title, price, 
case 
    when status = 'SALE'
    then '판매중'
    when status = 'RESERVED'
    then '예약중'
    when status = 'DONE'
    then '거래완료'
end as STATUS
from used_goods_board
where date_format(created_date, '%Y-%m-%d') = '2022-10-05'
order by board_id desc;