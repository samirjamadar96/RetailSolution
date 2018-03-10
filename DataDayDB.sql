Use DataDay

/* Category Table */
IF OBJECT_ID('dbo.Category', 'U') IS NOT NULL 
	DROP TABLE dbo.Category; 
CREATE TABLE Category (
    CategoryID char,
    CategoryName varchar(50),
    PRIMARY KEY (CategoryID)
);

BULK INSERT dbo.Category
FROM 'C:\Users\jjamads\Desktop\.NET WEB API\Data\Category.csv'
WITH
(
FIRSTROW = 2, -- second row if header row in file
FIELDTERMINATOR = ',',  --CSV field delimiter
ROWTERMINATOR = '\n',   --Use to shift the control to next row
TABLOCK
)

/* ProductDetails Table */
IF OBJECT_ID('dbo.ProductDetails', 'U') IS NOT NULL 
	DROP TABLE dbo.ProductDetails; 
CREATE TABLE ProductDetails (
    ProductID nvarchar(200),
    CategoryID char references Category(CategoryID), 
	AisleNo int,
	PrductName nvarchar(300),
    PRIMARY KEY (ProductID),
);

BULK INSERT dbo.ProductDetails
FROM 'C:\Users\jjamads\Desktop\.NET WEB API\Data\ProductDetails.csv'
WITH
(
FIRSTROW = 2, -- second row if header row in file
FIELDTERMINATOR = ',',  --CSV field delimiter
ROWTERMINATOR = '\n',   --Use to shift the control to next row
TABLOCK
)

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
FIRSTROW = 2, -- second row if header row in file
FIELDTERMINATOR = ',',  --CSV field delimiter
ROWTERMINATOR = '\n',   --Use to shift the control to next row
TABLOCK
)