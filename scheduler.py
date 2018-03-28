import hbase_connector
import pandas as pd
import datetime as dt
import schedule
import time

def ShowCurrentTime():
	CurrentTime = pd.to_datetime(dt.datetime.now())
	print('Current time is : ',CurrentTime)

def UpdateTrailsDataToHbase():
	print('inside UpdateTrailsDataToHbase function')
	table_name = 'dd_trail_sample_livepush'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/trail_sample_livepush.csv')
	df['Exit Time'] = pd.to_datetime(df['Exit Time'])
	df3 = df[(df['Exit Time'].dt.date == dt.datetime.now().date()) & (df['Exit Time'].dt.hour == (dt.datetime.now().hour-1))]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting UpdateTrailsDataToHbase function')

def UpdateReviewsDataToHbase():
	print('inside UpdateReviewsDataToHbase function')
	table_name = 'dd_reviews_sample_livepush'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/ReviewsSample.csv')
	df['Timestamp'] = pd.to_datetime(df['Timestamp'])
	df3 = df[(df['Timestamp'].dt.date == dt.datetime.now().date())]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting UpdateReviewsDataToHbase function')

def UpdateLoyaltyDataToHbase():
	print('inside UpdateLoyaltyDataToHbase function')
	table_name = 'dd_Loyalty_sample_livepush'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/3yearsLoyalty.csv')
	df['FirstPurchaseDate'] = pd.to_datetime(df['FirstPurchaseDate'])
	df3 = df[(df['FirstPurchaseDate'].dt.date == dt.datetime.now().date()) & (df['FirstPurchaseDate'].dt.hour == (dt.datetime.now().hour-1))]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting UpdateLoyaltyDataToHbase function')

if __name__ == '__main__':
	schedule.clear()
	schedule.every(1).hours.do(ShowCurrentTime)
	schedule.every(1).hours.do(UpdateTrailsDataToHbase)
	schedule.every(1).day.do(UpdateReviewsDataToHbase)
	schedule.every(1).hours.do(UpdateLoyaltyDataToHbase)
	schedule.every(1).hours.do(ShowCurrentTime)

	while True:
	 	schedule.run_pending()
	 	time.sleep(1)
