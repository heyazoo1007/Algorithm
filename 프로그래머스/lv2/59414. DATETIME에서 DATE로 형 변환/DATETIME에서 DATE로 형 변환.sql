-- 코드를 입력하세요
-- 각 동물의 아이디, 이름, 들어온 날짜 조회 SQL, id로 ORDER BY 
SELECT animal_id, name, date_format(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS
ORDER BY animal_id;