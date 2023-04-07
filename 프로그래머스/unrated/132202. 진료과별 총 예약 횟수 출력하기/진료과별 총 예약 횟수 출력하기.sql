-- 코드를 입력하세요
-- 2022-05 날짜의 예약 환자 수 group by 진료과코드 order by 환자수, 진료과 코드 
SELECT MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from appointment
where date_format(APNT_YMD, "%Y-%m") = '2022-05'
group by MCDP_CD
order by count(*) ASC, MCDP_CD ASC;