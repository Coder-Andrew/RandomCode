import speedtest
import time
import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'Speed_Log_4.txt'

st = speedtest.Speedtest()

count = 1
initial_time = time.time()



with open(file_name,'a') as file:
    file.write('Test No,Time from Start,UL Spd,DL Spd,Ping\n')

while True:
    st.get_best_server()
    download = st.download()
    upload = st.upload()
    ping = st.results.ping

    test_time = time.time()
    with open(file_name,'a') as file:
        file.write('{},{:.2f},{:.4f},{:.4f},{:.4f}\n'.format(count,test_time-initial_time,download/1000000,upload/1000000,ping))

    print('Done {} speedtests'.format(count))
    count += 1

    time.sleep(60)
