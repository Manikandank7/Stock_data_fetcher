import yfinance as yf
import pandas as pd

# Get the data
company_name="TCS.NS"
start_date="2021-6-1"
end_date='2021-6-27'
data = yf.download(company_name,start_date,end_date,interval="5m")
data.to_csv(company_name+'_data.csv')
    

