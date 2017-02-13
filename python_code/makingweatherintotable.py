import pprint
import metoffer1
api_key = '8057bc82-1b58-4b7d-a54e-c7d275935300'
M = metoffer1.MetOffer(api_key)
x = M.nearest_loc_forecast(352409, metoffer1.THREE_HOURLY)
y = metoffer1.parse_val(x)
pprint.pprint(y.data)