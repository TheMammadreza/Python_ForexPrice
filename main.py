import datetime as dtm
import requests as rq
import pandas as pd
import matplotlib.pyplot as plt

def getSeries(baseCurrency, quoteCurrency, dayCount):
# Constant and declaration
    urlAPI = 'https://api.exchangerate.host/timeseries'
    amount = 1
    endDate = dtm.datetime.now()
    startDate = (endDate - dtm.timedelta(days=dayCount))

# Get series
    paramList = {'base': baseCurrency, 'amount': amount, 'start_date': startDate.date(), 'end_date': endDate.date()}
    response = rq.get(urlAPI, params=paramList)
    data = response.json()

# Prepare data for demonstrate
    pairHistory = {}
    historyPrice = []

    for item in data['rates']:
        pairPrice = data['rates'][item][quoteCurrency]
        pairHistory[item] = [pairPrice]
        historyPrice.append(pairPrice)
    
# Show price and date together
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(pairHistory).transpose()
    df.columns = ['Rate']
    print(df)

# Plot the chart
    plt.plot(historyPrice)
    plt.title(f'{baseCurrency}{quoteCurrency} {historyPrice[-1]}')
    plt.show()

# Example to use
getSeries('EUR', 'USD', 200)