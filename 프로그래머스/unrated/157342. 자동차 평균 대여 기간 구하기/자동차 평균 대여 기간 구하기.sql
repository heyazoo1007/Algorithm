-- 코드를 입력하세요
-- avg(대여기간) >= 7 (소수 두번째 자리 반올림)
-- order by avg(대여기간) desc, car_id desc
SELECT car_id, round(sum(datediff(end_date, start_date)) / count(car_id), 1) + 1 as average_duration
from car_rental_company_rental_history
group by car_id
having average_duration >= 7
order by average_duration desc, car_id desc;

-- car_id 별로 대여일을 모두 더한 뒤 count(car_id)로 나눈 값 