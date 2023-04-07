-- 코드를 입력하세요
-- Neutered가 있으면 O, Spayed가 있으면 x로 표시하기
SELECT ANIMAL_ID, 
       NAME, 
       CASE 
            WHEN SEX_UPON_INTAKE like 'Neutered%' or SEX_UPON_INTAKE like 'Spayed%' 
            THEN 'O'
            WHEN SEX_UPON_INTAKE like 'Intact%' 
            THEN 'X'
      END AS 중성화
FROM ANIMAL_INS;
