-- 코드를 입력하세요
-- 카테고리 = '경제' -> book_id, author_name, published_date, order by 출판일 
SELECT b.book_id, a.author_name, date_format(b.published_date, "%Y-%m-%d")
from book b
join author a
on b.author_id = a.author_id
where b.category = '경제'
order by b.published_date;