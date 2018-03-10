


create table Website(
WebsiteID int PRIMARY KEY,
WebsiteName nvarchar(50)
)

create table Date_Time(
DateTimeID int PRIMARY KEY,
DateTimeFormat DateTime,
DateTimeValue DateTime
)



create table Category(
CategoryID bigint PRIMARY KEY,
CategoryName nvarchar(50),
CategoryDescription nvarchar(300),
)



create table Item(
ItemID int PRIMARY KEY,
ItemDescription nvarchar(200),
)

create table Addresses(
AddressID bigint PRIMARY KEY,
PostalAddress nvarchar(100),
City nvarchar(20),
Country nvarchar(20),
StateName nvarchar(20),
StateID smallint,
Territory nvarchar(20),
District nvarchar(20),
Zip bigint
)

create table Contact(
ContactID bigint PRIMARY KEY,
ContactName nvarchar(100),
ContactNumber bigint,
AlternateContactNumber bigint,
EmailAddress nvarchar(20),
AddressID bigint references Addresses(AddressID),
LanguageCode int,
LocaleID int,
NumberFormat nvarchar(10)
)




create table CustomerLoyalty(
LoyaltyID bigint PRIMARY KEY,
CustomerName nvarchar(50),
Gender char,
Age smallint,
LoyaltyPoints int ,
ContactID bigint references Contact(ContactID)
)

create table Trail(
TrailID bigint PRIMARY KEY,
Area int,
Aisle int,
EntryDateTimeID int references Date_Time(DateTimeID),
ExitDateTimeID int references Date_Time(DateTimeID),
LoyaltyID bigint references CustomerLoyalty(LoyaltyID) 
)

create table Scheme(
SchemeID int PRIMARY KEY,
SchemeDescription nvarchar(200)
)

create table Brand(
BrandID bigint PRIMARY KEY,
BrandName nvarchar(50),
BrandDescription nvarchar(200)
)

create table _Type(
TypeID bigint PRIMARY KEY,
TypeName nvarchar(50),
TypeDescription nvarchar(200)
)

create table ProductLine(
ProductLineID bigint PRIMARY KEY,
ProductLineName nvarchar(50),
ProductLineDescription nvarchar(200)
)


create table ProductClass(
ProductClassID bigint PRIMARY KEY,
ProductClassName nvarchar(50),
ProductClassDescription nvarchar(200)
)

create table ProductFamily(
ProductFamilyID bigint PRIMARY KEY,
ProductFamilyName nvarchar(50),
ProductFamilyDescription nvarchar(200)
)

create table ProductNeedFamily(
ProductNeedFamilyID bigint PRIMARY KEY,
ProductNeedFamilyName nvarchar(50),
ProductNeedFamilyDescription nvarchar(200)
)

create table Unit(
UnitID bigint PRIMARY KEY,
UnitName nvarchar(50),
UnitDescription nvarchar(200)
)


create table Company(
CompanyID int PRIMARY KEY,
CompanyName nvarchar(50),
CompanyDescription nvarchar(200)
)

create table Product(
ProductID bigint PRIMARY KEY,
ProductName nvarchar(50),
ItemID int,
ItemBasePrice float NOT NULL,
ProductDescription nvarchar(300),
CategoryID bigint references Category(CategoryID),
UnitID bigint references Unit(UnitID),
BrandID bigint references Brand(BrandID),
TypeID bigint references _Type(TypeID),
ProductLineID bigint references ProductLine(ProductLineID),
ProductClassID bigint references ProductClass(ProductClassID),
ProductFamilyID bigint references ProductFamily(ProductFamilyID),
ProductNeedFamilyID bigint references ProductNeedFamily(ProductNeedFamilyID),
ManufacturingDateTimeID int references Date_Time(DateTimeID),
ExpiryDatetimeID int references Date_Time(DateTimeID)
)


create table Store(
StoreID bigint PRIMARY KEY,
StoreName nvarchar(300),
StoreArea nvarchar(50),
ParentCompanyID int references Company(CompanyID),
ContactID bigint references Contact(ContactID)
)


create table Inventory(
InventoryID int PRIMARY KEY,
StoreID bigint references Store(StoreID),
)


create table InStoreLocation(
InStoreLocationID int PRIMARY KEY,
AreaID int,
StoreID bigint references Store(StoreID),
Aisle nvarchar(10),
Rack nvarchar(10),
RowColumn int
)

create table ProductLocationTransaction(
LocationTransactionID bigint PRIMARY KEY,
InstoreLocationID int references InstoreLocation(InstoreLocationID),
)

create table ProductLineLocation(
TransactionID bigint PRIMARY KEY,
StoreID bigint references Store(StoreID),
ProductLineID bigint references ProductLine(ProductLineID)
)

create table Customer(
CustomerID bigint PRIMARY KEY
)

create table Review(
ReviewID bigint PRIMARY KEY,
ReviewText nvarchar(200),
ReviewSummary nvarchar(50),
Rating smallint,
CustomerID bigint references Customer(CustomerID),
WebsiteID int references Website(WebsiteID),
ProductID bigint references Product(ProductID),
StoreID bigint references Store(StoreID)
)
create table Invoice(
InvoiceID bigint PRIMARY KEY,
TotalTaxAmount float NOT NULL,
TotalTransactionAmount float NOT NULL,
DateTimeID int references Date_Time(DateTimeID),
TrailID bigint references Trail(TrailID),
LoyaltyID bigint references CustomerLoyalty(LoyaltyID)
)

create table Transactions(
TransactionID bigint PRIMARY KEY,
ProductID bigint references Product(ProductID),
SchemeID int references Scheme(SchemeID),
SellingPrice float NOT NULL,
InvoiceID bigint references Invoice(InvoiceID)
)

