import pandas_datareader.data as pdr
import datetime as dt

ticker = "AMZN"
start_date = dt.date.today() - dt.timedelta(365)
end_date = dt.date.today()

data = pdr.get_data_yahoo(ticker, start_date, end_date)
data.to_csv('out.csv', encoding='utf-8', index=False)

print(data)
