from iqoptionapi.api import IQOptionAPI
import json
import iqoptionapi.constants as api_constants
from time import gmtime, strftime
import time



api = IQOptionAPI("iqoption.com", "genesiscrew@hotmail.com", "ad318717")
api.connect()
time.sleep(5);

#api.setactives([api_constants.ACTIVES["EURUSD"], api_constants.ACTIVES["EURUSD-OTC"]])
api.setactives([1, 1])
time.sleep(5);
api.getcandles(1,1)
time.sleep(5);
data = api.candles.candles_data
print(api.candles.candles_data)

print("local time is")
sec = strftime("%S", gmtime())
while True:
    sec = strftime("%S", gmtime())
    if sec == "59":

        print("should be here")
        api.buy(1, 1, "binary", "put")
        time.sleep(5);



#for key in api_constants.ACTIVES:
    #print key, 'corresponds to', api_constants.ACTIVES[key]

#api.timesync.expiration_time = 0






profile = api.getprofile()
res = json.loads(profile._content)

balance = res['result']['balance']

print("banlance")
print(balance)


