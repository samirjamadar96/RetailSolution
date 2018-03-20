import hbase_connector
import pandas as pd
import datetime as dt
import schedule
import time
def UpdateDataToHbase():
	print('inside function')
	table_name = 'dd_invoice_sample_live'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/sample.csv')
	df['Timestamp'] = pd.to_datetime(df['Timestamp'])
	df3 = df[(df['Timestamp'].dt.date == dt.datetime.now().date()) & (df['Timestamp'].dt.hour == (dt.datetime.now().hour-1))]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting function')

def UpdateTrailsDataToHbase():
	print('inside function')
	table_name = 'dd_trail_sample_livepush'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/trail_sample_livepush.csv')
	df['Exit Time'] = pd.to_datetime(df['Exit Time'])
	df3 = df[(df['Exit Time'].dt.date == dt.datetime.now().date()) & (df['Exit Time'].dt.hour == (dt.datetime.now().hour-1))]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting function')

def UpdateReviewsDataToHbase():
	print('inside function')
	table_name = 'dd_reviews_sample_livepush'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/ReviewsSample.csv')
	df['Timestamp'] = pd.to_datetime(df['Timestamp'])
	df3 = df[(df['Timestamp'].dt.date == dt.datetime.now().date())]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting function')

def UpdateLoyaltyDataToHbase():
	print('inside function')
	table_name = 'dd_Loyalty_sample_livepush'
	df = pd.read_csv('C:/Users/jjamads/Desktop/.NET WEB API/Data/3yearsLoyalty.csv')
	df['FirstPurchaseDate'] = pd.to_datetime(df['FirstPurchaseDate'])
	df3 = df[(df['FirstPurchaseDate'].dt.date == dt.datetime.now().date()) & (df['FirstPurchaseDate'].dt.hour == (dt.datetime.now().hour-1))]
	hbase_connector.push_to_hbase(df3, table_name, create_table=False, delete_table=False)
	print('exiting function')

if __name__ == '__main__':
	schedule.clear()
	schedule.every(1).hours.do(UpdateDataToHbase)	
	schedule.every(1).hours.do(UpdateTrailsDataToHbase)
	schedule.every(1).hours.do(UpdateReviewsDataToHbase)
	schedule.every(1).hours.do(UpdateLoyaltyDataToHbase)
	while True:
	 	schedule.run_pending()
	 	time.sleep(1)
