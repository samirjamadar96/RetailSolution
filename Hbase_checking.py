from ast import literal_eval
import happybase as hb

HB_HOST = '52.225.252.79'
connection = None
def connect_to_hbaase(HB_HOST):
    try:
        print('Establishing Connection...')
        global connection
        connection = hb.Connection(HB_HOST)
        print('Connection Etablished:%s' % str(HB_HOST))
    except Exception as e:
        print(' Error : %s ' % str(e.args))

def show_tables_names():
    try:
        global connection
        show_tableconnection = connection.tables()
        for item in show_tableconnection:
            if str(item).startswith('b\'dd_'):
                print(str(item).strip('b\''))
    except Exception as e:
        print(' Error : %s ' % str(e.args))

def read_table(table_name):
    try:
        print('\n\nTABLE NAME: %s ' % table_name )
        table = connection.table(table_name)
        for (key, data) in table.scan():
            print('index: %s ' % str(key).strip('b\''), str(data).strip('b\''))
    except Exception as e:
        print(' Error : %s ' % str(e.args))


    # def csv_to_hbase(row,batch):
    #      try:
    #          batch.put(row[0], {"data:kw": row[1], "data:sub": row[2], "data:type": row[3],
    #                             "data:town": row[4], "data:city": row[5], "data:zip": row[6],
    #                             "data:cdist": row[7], "data:open": row[8], "data:close": row[9],
    #                             "data:status": row[10], "data:origin": row[11], "data:loc": row[12]})
        # except Exception as e:
        #     print(' Error : %s ' % str(e.args))



if __name__ == '__main__':
    host = '52.225.252.79'
    connect_to_hbaase(host)
    show_tables_names()
    read_table('dd_Loyalty_sample_livepush')


