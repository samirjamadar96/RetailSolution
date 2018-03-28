# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:50:31 2018

@author: JCHMUK3
"""
#TODO: index tables by time

import pandas as pd
import numpy as np
import happybase 
import datetime as dt
from thriftpy.transport import TTransportException

HB_HOST = "52.225.252.79"

def _create_table(connection, table_name):
    if table_name.rfind('dd_') is -1:
        raise ValueError('table name needs to be prefixed with \'dd_\'')
    connection.create_table(table_name, {'val':dict()})
    
def _delete_table(connection, table_name):
    if table_name.rfind('dd_') is -1:
        raise ValueError('table name needs to be prefixed with \'dd_\'')
    connection.delete_table(table_name, disable=True)

def _push_dict(data, connection, table_name):
    if table_name not in connection.tables():
        raise ValueError('Hbase does not contain the table: {}'
                         .format(table_name))
    tab = connection.table(table_name)
    with tab.batch(transaction=True) as b:
        for key, value in data.items():
            b.put(str(key), value)
        b.send()
        
#change column names to <cf>:<column name>, cast all df values to type 'str'
def _hbase_compat_dataframe(df):
    cf = 'val'
    hb_columns = []
    for column in df.columns:
        index=column.find(' ')
        if index is not -1:
            column = column.replace(' ','_')
        hb_columns.append(':'.join((cf, column)))
    df.columns =  hb_columns
    df = df.astype(str)
    return df

def establish_connection():
    try:
        connection = happybase.Connection(HB_HOST)
    except TTransportException as e:
        file = open("ErrorLogFile.txt","a")
        file.write(str(dt.datetime.now()) + '\t\t\t' + 'push_to_hbase' + '\t\t' + str(e) + '\n')
        file.close()
        return False
    return connection
def push_to_hbase(df, table_name, create_table=False, delete_table=False):
    print('establishing connection...')
    connection = establish_connection()
    if not connection:
        return 'Failure'
        
    else:
        print('connection established...')
        if create_table:
            _create_table(connection, table_name)
            print('new table created')
    
        df = _hbase_compat_dataframe(df)
        df = df.to_dict(orient='index')
    
        print('pushing to hbase...')
        _push_dict(df, connection, table_name)
    
        if delete_table:
            _delete_table(connection, table_name)
        
        connection.close()
        print("succesfull...")
        return 'Success'    
        
if __name__=='__main__':
    print('Running test')
    df = pd.DataFrame(np.random.randint(1,1000,size=(100,5)),
                     columns=['a','b','c','d','e'])
    con = push_to_hbase(df, 'dd_push_test', create_table=True,delete_table=True)
    print('Test succesfull')   