--Студент – [FullName] Народився BirthDate. Має електронну пошту eMail та отримує 
--стипендію в грн. 

/*SELECT TOP 20 PERCENT N'Студент - '+ FirstName+ ' '  +LastName + N'. Народився - '+ CAST(BirthDay AS nvarchar(10))
+ N'. Має електронну адресу - '+eMail+ N' та отримує стіпендію в ' + CAST (Money AS nvarchar(10))
+ N' грн.' AS [Студенти]
FROM Student;


SELECT FirstName +' '+ LastName AS [Full Name], BirthDay, Money 
FROM Student 
--WHERE MONTH(BirthDay) >=9 AND MONTH(BirthDay) <= 11; 
--WHERE YEAR(BirthDay) % 2 = 0 AND DAY(BirthDay) % 2 <> 0; 
--WHERE NOT Money = 900.00;
ORDER BY Money ASC, BirthDay DESC;

SELECT FirstName +' '+ LastName AS [Full Name],eMail, BirthDay, Money 
FROM Student 
--WHERE YEAR(BirthDay) = 2002 OR YEAR(BirthDay) = 2010 OR YEAR(BirthDay) = 2014
--WHERE YEAR(BirthDay) IN (2002,2010,2014)
--WHERE BirthDay >='1980-01-01' AND BirthDay <= '1999-12-31'
--WHERE BirthDay BETWEEN '1980-01-01' AND '1999-12-31'
WHERE eMail LIKE '%ak%'

--ORDER BY BirthDay DESC

INSERT INTO Student (FirstName,LastName,eMail,Phone,BirthDay,Lerning) 
VALUES				('Aleksy','Kornienko','aks@gmail.com','+38000000','1998-01-10',1);


INSERT INTO dbo.RezultTabel (FullName,email,birthday) 
SELECT FirstName +' '+ LastName, eMail, BirthDay 
FROM Student 

SELECT FirstName, LastName, eMail, BirthDay,Money  
INTO tmp4 
FROM Student
--WHERE YEAR(BirthDay) > 2010;

UPDATE tmp3 SET Money = 100.00 WHERE Money IS NULL
*/
SELECT * FROM tmp4 WHERE Money IS NULL
DELETE FROM tmp4 WHERE Money IS NULL









