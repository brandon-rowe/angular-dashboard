import requests, datetime, pathlib, json
from bs4 import BeautifulSoup


def todaysdate():
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    date="{}{}{}".format(year,month,day)
    return date


def main():
    date = todaysdate()
    jsonFilePath = pathlib.Path('ethereumData.json').parent.absolute().as_posix() + '/ethereum/ethereumData.json'
    response = requests.get('https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130428&end='+date)
    soup = BeautifulSoup(response.text,'html.parser')
    td = soup.find_all('td')
    Headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']
    data = {}
    temp = []
    for i in td:
        temp.append(i.contents[0].contents[0])
        if len(temp) == len(Headers):
            data[temp[0]] = {Headers[0]: temp[0], Headers[1]: temp[1], Headers[2]: temp[2], Headers[3]: temp[3], Headers[4]: temp[4], Headers[5]: temp[5], Headers[6]: temp[6]} 
            temp = []
    
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


main()

