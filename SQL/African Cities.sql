/*
- 2026-01-13(1)
- 문제 : continent가 Africa인 city이름 구하기
- 접근법:
    - city와 country를 city.countrycode = country.code로 JOIN
    - WHERE절로 continent가 Africa인 것을 필터링
*/

SELECT          city.name
FROM            city
INNER JOIN      country
ON              city.countrycode = country.code
WHERE           country.continent = 'Africa'