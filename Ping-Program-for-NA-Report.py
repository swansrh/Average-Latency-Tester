
#First before use make sure to add new resource pythonping this can be done by the console
#use the following command $pip install pythonping 
#if you have any trouble their website is linked here https://pypi.org/project/pythonping/
#pythonping is a more easy to use traffic analysis tool for python
from pythonping import ping
#creating a data file
f = open("pingdata.dat", "w")
#ping and record data on the traffic 
def ping_host(host):
    #giving the ping command a target, a count of how many ICMP packets it will send and a waiting length for reply in seconds
    pingAnalysis = ping(target=host, count=20, timeout=3)
    #writing average ping and packet loss to file
    f.write("Average Latency : " +str(pingAnalysis.rtt_avg_ms)+"  Packet Loss "+str(pingAnalysis.packet_loss)+"\n")
    #returning values to console
    return {
        'Current Host IP': host,
        'Average Latancey that is produced': pingAnalysis.rtt_avg_ms,
        'Packet loss for the entire round trip': pingAnalysis.packet_loss
    }
print("Starting Traffic Analysis")
# running analysis x times
for host in range(40):
    print(ping_host("192.168.1.1"))
print("Traffic Analysis Completed")