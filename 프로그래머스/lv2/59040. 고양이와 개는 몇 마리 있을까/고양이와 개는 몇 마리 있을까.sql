-- 코드를 입력하세요
-- 고양이와 개가 각각 몇 마리인지, 고양이 - 개 순서 
SELECT ANIMAL_TYPE, count(*)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE = "Cat" or ANIMAL_TYPE = "Dog"
ORDER BY ANIMAL_TYPE;