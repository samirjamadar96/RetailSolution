Use DataDay

/* FTData Table */
IF OBJECT_ID('dbo.FTData', 'U') IS NOT NULL 
	DROP TABLE dbo.FTData; 
CREATE TABLE FTData (
    SerialNo bigint,
    Category varchar(50),
	FDate date,
	Financial_Turnover decimal(10,0),
    PRIMARY KEY (SerialNo)
);

BULK INSERT dbo.FTData
FROM 'C:\Users\jjamads\Desktop\.NET WEB API\Data\FTData.csv'
WITH
(
FIRSTROW = 2, -- secopnd row if header row in file
FIELDTERMINATOR = ',',  --CSV field delimiter
ROWTERMINATOR = '\n',   --Use to shift the control to next row
TABLOCK
)