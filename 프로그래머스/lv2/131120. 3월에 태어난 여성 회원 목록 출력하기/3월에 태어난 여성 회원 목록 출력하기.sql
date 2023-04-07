-- 코드를 입력하세요
-- 생일 3월, 전화번호 is NOT NULL인 로우, order by member_id
SELECT member_id, member_name, gender, date_format(date_of_birth, "%Y-%m-%d")
from member_profile
where TLNO is not null and date_format(date_of_birth, "%m") = '03' and gender = 
'W'
order by member_id;