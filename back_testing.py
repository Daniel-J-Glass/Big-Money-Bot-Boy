
import requests
import time

#Takes in constraints and writes bitfinex candle data from given constraints to file
#Prints verification
#Returns nothing
def write_data(pair, time_frame, start_date, limit):
    final_data = []
    time_frame_string = str(time_frame)+'m';

    for _ in range(0,100):
        url = 'https://api.bitfinex.com/v2/candles/trade:'+time_frame_string+':t'+pair+'/hist?sort=1&limit='+str(limit)+'&start='+str(start_date)

        r = requests.get(url)

        temp_data = r.json()
        final_data = final_data + temp_data

        if len(temp_data) == limit:
            start_date = int(temp_data[len(temp_data)-1][0])+time_frame*60*limit
        else:
            start_date = int(temp_data[len(temp_data)-2][0])+time_frame*60*limit
            break

        time.sleep(3)

    with open('BFX_'+pair+'_'+time_frame_string+'.json', 'w') as f:
        f.write(str(final_data))
    print('Completed writing '+pair+' '+time_frame_string+' data.')

def main():
    limit = 1000
    time_frame_array = [5,15,30] #5m, 15m, 30m
    start_date = 1514764800*limit # Jan 01 2018
    pair = 'XRPUSD' #XRPBTC,
    for time_frame in time_frame_array:
        write_data(pair, time_frame, start_date, limit)

if __name__ == '__main__':
    main()
