/*SELECT N'Студент - '+FirstName+' '+LastName AS [ПІБ],eMail AS [Пошта],Phone,BirthDay,
GroupsID, CafedraID,CAST(Money*1.20 AS nvarchar(20)) +' UAH' AS [Стіпендія],Link
FROM Student;

SELECT  N'Студент - '+FirstName+' '+LastName AS [ПІБ],eMail AS [Пошта],Phone,BirthDay,
GroupsID, CafedraID,CONVERT(nvarchar(20), Money*1.20 ) +' UAH' AS [Стіпендія],Link
FROM Student;

SELECT  N'Студент - '+FirstName+' '+LastName AS [ПІБ],eMail AS [Пошта],Phone,BirthDay,
GroupsID, CafedraID,CONVERT(nvarchar(20), Money*1.20 ) +' UAH' AS [Стіпендія],Link
FROM Student WHERE Phone IS NOT NULL 
ORDER BY MONTH(BirthDay) ASC;

--Money > 1000 OR YEAR(BirthDay) > 2010 ;

SELECT FirstName + ' ' + LastName AS [Fulls Names], BirthDay 
FROM Student
WHERE FirstName IN('Oleg','Olga','Andrey')


SELECT FirstName + ' ' + LastName AS [Fulls Names], BirthDay 
FROM Student
WHERE BirthDay BETWEEN '2002-01-01' AND '2002-12-31' */
SELECT FirstName + ' ' + LastName AS [Fulls Names], BirthDay, eMail
FROM Student
WHERE eMail LIKE '%gmail.com';