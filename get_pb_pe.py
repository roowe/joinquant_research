from jqdatasdk import *
import pandas as pd
import numpy as np
from datetime import timedelta, datetime, date
import os
import conf
auth(conf.user, conf.password)

#指数历史PEPB
def get_index_pe_pb(indexCode, start=None):
    if start is None:
        start = get_security_info(indexCode).start_date
        print(start)
        if start < date(2005, 1, 4): #只计算2005年以来的数据
            start = date(2005, 1, 4)
    
    indexPriceDF = get_price(indexCode, start_date=start, end_date=datetime.today(), frequency='daily', fields='close')
    ##print("indexPriceDF", indexPriceDF)
    dfgz=pd.DataFrame()
    for d, _row in indexPriceDF.iterrows():
        ##print("d", d)
        stocks = get_index_stocks(indexCode, d)    
        q = query(valuation).filter(valuation.code.in_(stocks))    
        df = get_fundamentals(q, d)
        ##print(df.iloc[0]["day"])
        if len(df)>0:
            pe = len(df)/sum([1/p if p>0 else 0 for p in df.pe_ratio])
            pb = len(df)/sum([1/p if p>0 else 0 for p in df.pb_ratio])
        else:
            pe = float('NaN')
            pb = float('NaN')
        ##print(d, pe, pb)
        dfgz=dfgz.append({'day':d.date(),'pe':pe,'pb':pb}, ignore_index=True)
    ##print(dfgz)        
    return dfgz


def main():
    indexCodes =['000016.XSHG', '000905.XSHG', '399300.XSHE', '000991.XSHG']
    for indexCode in indexCodes:
        print(indexCode, "start handle", )
        dataPath = 'data/%s_pe_pb.csv'%(indexCode)
        if os.path.exists(dataPath):
            dfgz = pd.read_csv(dataPath) 
            startDateTime = datetime.strptime(dfgz.iloc[-1]["day"], "%Y-%m-%d")
            startDateTime = startDateTime + timedelta(days=1)
            #print(start_date)
            #print(dfgz)
            dfgz = dfgz.append(get_index_pe_pb(indexCode, startDateTime.date()), ignore_index=True) 
        else:    
            dfgz = get_index_pe_pb(indexCode, date(2018,7,10))
        dfgz.to_csv(dataPath, index=False)
        print(indexCode, "done")

main()    
