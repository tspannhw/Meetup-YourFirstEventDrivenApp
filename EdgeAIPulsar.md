```python
import pulsar
client = pulsar.Client('pulsar://nvidia-desktop:6650')
producer = client.create_producer('persistent://meetup/newjersey/first')
producer.send(('Simple Text Message').encode('utf-8'))
client.close()

```

    2021-12-03 08:14:45.970 INFO  [0x118a2c600] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:14:45.971 INFO  [0x118a2c600] ConnectionPool:84 | Created connection for pulsar://nvidia-desktop:6650
    2021-12-03 08:14:45.982 INFO  [0x700011ac5000] ClientConnection:376 | [192.168.1.223:56665 -> 192.168.1.210:6650] Connected to broker
    2021-12-03 08:14:45.992 INFO  [0x700011ac5000] HandlerBase:55 | [persistent://meetup/newjersey/first, ] Getting connection from pool
    2021-12-03 08:14:45.997 INFO  [0x700011ac5000] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:14:45.997 INFO  [0x700011ac5000] ConnectionPool:84 | Created connection for pulsar://127.0.0.1:6650
    2021-12-03 08:14:46.001 INFO  [0x700011ac5000] ClientConnection:378 | [192.168.1.223:56666 -> 192.168.1.210:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
    2021-12-03 08:14:46.010 INFO  [0x700011ac5000] ProducerImpl:175 | [persistent://meetup/newjersey/first, ] Created producer on broker [192.168.1.223:56666 -> 192.168.1.210:6650] 
    2021-12-03 08:14:46.021 INFO  [0x118a2c600] ClientImpl:485 | Closing Pulsar client with 1 producers and 0 consumers
    2021-12-03 08:14:46.021 INFO  [0x118a2c600] ProducerImpl:583 | [persistent://meetup/newjersey/first, standalone-21-403] Closing producer for topic persistent://meetup/newjersey/first
    2021-12-03 08:14:46.023 INFO  [0x700011ac5000] ProducerImpl:626 | [persistent://meetup/newjersey/first, standalone-21-403] Closed producer
    2021-12-03 08:14:46.024 INFO  [0x700011ac5000] ClientConnection:1508 | [192.168.1.223:56666 -> 192.168.1.210:6650] Connection closed
    2021-12-03 08:14:46.024 INFO  [0x700011ac5000] ClientConnection:1508 | [192.168.1.223:56665 -> 192.168.1.210:6650] Connection closed



```python
import pulsar
client = pulsar.Client('pulsar://nvidia-desktop:6650')
consumer = client.subscribe('persistent://meetup/newjersey/first',subscription_name='my-sub')
while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)
client.close()

```

    2021-12-03 08:15:12.199 INFO  [0x118a2c600] Client:88 | Subscribing on Topic :persistent://meetup/newjersey/first
    2021-12-03 08:15:12.200 INFO  [0x118a2c600] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:15:12.200 INFO  [0x118a2c600] ConnectionPool:84 | Created connection for pulsar://nvidia-desktop:6650
    2021-12-03 08:15:12.206 INFO  [0x700011ac5000] ClientConnection:376 | [192.168.1.223:56771 -> 192.168.1.210:6650] Connected to broker
    2021-12-03 08:15:12.215 INFO  [0x700011ac5000] HandlerBase:55 | [persistent://meetup/newjersey/first, my-sub, 0] Getting connection from pool
    2021-12-03 08:15:12.219 INFO  [0x700011ac5000] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:15:12.219 INFO  [0x700011ac5000] ConnectionPool:84 | Created connection for pulsar://127.0.0.1:6650
    2021-12-03 08:15:12.223 INFO  [0x700011ac5000] ClientConnection:378 | [192.168.1.223:56772 -> 192.168.1.210:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
    2021-12-03 08:15:12.242 INFO  [0x700011ac5000] ConsumerImpl:220 | [persistent://meetup/newjersey/first, my-sub, 0] Created consumer on broker [192.168.1.223:56772 -> 192.168.1.210:6650] 
    Received message: 'b'Simple Text Message''



```python
import pulsar
client = pulsar.Client('pulsar://nvidia-desktop:6650')
consumer = client.subscribe('persistent://public/default/iotjetsonjson',subscription_name='jupyter-sub')
i = 0
while i < 5000:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)
    i = i + 1
client.close()
```

    2021-12-03 08:18:47.785 INFO  [0x116098600] Client:88 | Subscribing on Topic :persistent://public/default/iotjetsonjson
    2021-12-03 08:18:47.786 INFO  [0x116098600] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:18:47.786 INFO  [0x116098600] ConnectionPool:84 | Created connection for pulsar://nvidia-desktop:6650
    2021-12-03 08:18:47.800 INFO  [0x70000e7d5000] ClientConnection:376 | [192.168.1.223:57685 -> 192.168.1.210:6650] Connected to broker
    2021-12-03 08:18:47.807 INFO  [0x70000e7d5000] HandlerBase:55 | [persistent://public/default/iotjetsonjson, jupyter-sub, 0] Getting connection from pool
    2021-12-03 08:18:47.810 INFO  [0x70000e7d5000] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:18:47.810 INFO  [0x70000e7d5000] ConnectionPool:84 | Created connection for pulsar://127.0.0.1:6650
    2021-12-03 08:18:47.815 INFO  [0x70000e7d5000] ClientConnection:378 | [192.168.1.223:57686 -> 192.168.1.210:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
    2021-12-03 08:18:47.839 INFO  [0x70000e7d5000] ConsumerImpl:220 | [persistent://public/default/iotjetsonjson, jupyter-sub, 0] Created consumer on broker [192.168.1.223:57686 -> 192.168.1.210:6650] 
    Received message: 'b'{"uuid":"xav_uuid_video0_ssc_20211203131856","camera":"/dev/video0","ipaddress":"192.168.1.210","networktime":24.957056045532227,"top1pct":10.394287109375,"top1":"wig","cputemp":"29.5","gputemp":"29.5","gputempf":"85","cputempf":"85","runtime":"6","host":"nvidia-desktop","filename":"/home/nvidia/nvme/images/out_video0_wdn_20211203131856.jpg","host_name":"nvidia-desktop","macaddress":"70:66:55:15:b4:a5","te":"5.759700775146484","systemtime":"12/03/2021 08:19:02","cpu":19.0,"diskusage":"23379.5 MB","memory":81.1,"imageinput":"/home/nvidia/nvme/images/img_video0_hni_20211203131856.jpg"}''
    Received message: 'b'{"uuid":"xav_uuid_video0_vhf_20211203131910","camera":"/dev/video0","ipaddress":"192.168.1.210","networktime":24.945663452148438,"top1pct":13.1591796875,"top1":"wig","cputemp":"30.0","gputemp":"30.0","gputempf":"86","cputempf":"86","runtime":"6","host":"nvidia-desktop","filename":"/home/nvidia/nvme/images/out_video0_jux_20211203131910.jpg","host_name":"nvidia-desktop","macaddress":"70:66:55:15:b4:a5","te":"5.581151962280273","systemtime":"12/03/2021 08:19:16","cpu":18.5,"diskusage":"23379.5 MB","memory":81.0,"imageinput":"/home/nvidia/nvme/images/img_video0_dlt_20211203131910.jpg"}''
    Received message: 'b'{"uuid":"xav_uuid_video0_qyx_20211203131924","camera":"/dev/video0","ipaddress":"192.168.1.210","networktime":24.946720123291016,"top1pct":9.27734375,"top1":"neck brace","cputemp":"30.0","gputemp":"30.0","gputempf":"86","cputempf":"86","runtime":"6","host":"nvidia-desktop","filename":"/home/nvidia/nvme/images/out_video0_ylq_20211203131924.jpg","host_name":"nvidia-desktop","macaddress":"70:66:55:15:b4:a5","te":"5.620406150817871","systemtime":"12/03/2021 08:19:30","cpu":20.1,"diskusage":"23379.5 MB","memory":81.1,"imageinput":"/home/nvidia/nvme/images/img_video0_jww_20211203131924.jpg"}''
    Received message: 'b'{"uuid":"xav_uuid_video0_ofc_20211203131938","camera":"/dev/video0","ipaddress":"192.168.1.210","networktime":25.11359977722168,"top1pct":21.875,"top1":"bathing cap, swimming cap","cputemp":"30.0","gputemp":"30.5","gputempf":"87","cputempf":"86","runtime":"6","host":"nvidia-desktop","filename":"/home/nvidia/nvme/images/out_video0_tkl_20211203131938.jpg","host_name":"nvidia-desktop","macaddress":"70:66:55:15:b4:a5","te":"5.6493799686431885","systemtime":"12/03/2021 08:19:44","cpu":18.9,"diskusage":"23379.5 MB","memory":81.1,"imageinput":"/home/nvidia/nvme/images/img_video0_dfq_20211203131938.jpg"}''
    2021-12-03 08:28:47.807 INFO  [0x70000e7d5000] ConsumerStatsImpl:70 | Consumer [persistent://public/default/iotjetsonjson, jupyter-sub, 0] , ConsumerStatsImpl (numBytesRecieved_ = 2373, totalNumBytesRecieved_ = 2373, receivedMsgMap_ = {[Key: Ok, Value: 4], }, ackedMsgMap_ = {[Key: {Result: Ok, ackType: 0}, Value: 4], }, totalReceivedMsgMap_ = {[Key: Ok, Value: 4], }, totalAckedMsgMap_ = {[Key: {Result: Ok, ackType: 0}, Value: 4], })



```python
from pyhive import presto
presto_conn = presto.connect(
     host='nvidia-desktop',
     port=8081,
     catalog='pulsar',
     schema='public/default'
)
presto_cur = presto_conn.cursor()   
presto_cur.execute('SELECT * FROM iotjetsonjson LIMIT 25')
print(presto_cur.fetchall())
```


```python
import pulsar
import json

client = pulsar.Client('pulsar://nvidia-desktop:6650')
consumer = client.subscribe('persistent://public/default/iotjetsonjson',subscription_name='jupyter-sub2')
msg = consumer.receive()
print("Received message: '%s'" % msg.data())
print("Message id: %s" % msg.message_id())
fields = json.loads(msg.data())
print("top1: %s" % fields["top1"])
consumer.acknowledge(msg)
client.close()
```

    2021-12-03 08:52:56.895 INFO  [0x116098600] Client:88 | Subscribing on Topic :persistent://public/default/iotjetsonjson
    2021-12-03 08:52:56.895 INFO  [0x116098600] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:52:56.895 INFO  [0x116098600] ConnectionPool:84 | Created connection for pulsar://nvidia-desktop:6650
    2021-12-03 08:52:56.899 INFO  [0x70000ec70000] ClientConnection:376 | [192.168.1.223:58835 -> 192.168.1.210:6650] Connected to broker
    2021-12-03 08:52:56.905 INFO  [0x70000ec70000] HandlerBase:55 | [persistent://public/default/iotjetsonjson, jupyter-sub2, 0] Getting connection from pool
    2021-12-03 08:52:56.914 INFO  [0x70000ec70000] ClientConnection:190 | [<none> -> pulsar://nvidia-desktop:6650] Create ClientConnection, timeout=10000
    2021-12-03 08:52:56.914 INFO  [0x70000ec70000] ConnectionPool:84 | Created connection for pulsar://127.0.0.1:6650
    2021-12-03 08:52:56.919 INFO  [0x70000ec70000] ClientConnection:378 | [192.168.1.223:58836 -> 192.168.1.210:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
    2021-12-03 08:52:56.936 INFO  [0x70000ec70000] ConsumerImpl:220 | [persistent://public/default/iotjetsonjson, jupyter-sub2, 0] Created consumer on broker [192.168.1.223:58836 -> 192.168.1.210:6650] 
    Received message: 'b'{"uuid":"xav_uuid_video0_dxc_20211203135304","camera":"/dev/video0","ipaddress":"192.168.1.210","networktime":24.936447143554688,"top1pct":9.674072265625,"top1":"wig","cputemp":"31.0","gputemp":"31.0","gputempf":"88","cputempf":"88","runtime":"6","host":"nvidia-desktop","filename":"/home/nvidia/nvme/images/out_video0_zvt_20211203135304.jpg","host_name":"nvidia-desktop","macaddress":"70:66:55:15:b4:a5","te":"5.505628347396851","systemtime":"12/03/2021 08:53:09","cpu":18.2,"diskusage":"23379.5 MB","memory":82.6,"imageinput":"/home/nvidia/nvme/images/img_video0_hsa_20211203135304.jpg"}''
    Message id: (77688,7,-1,0)
    top1: wig
    2021-12-03 08:53:15.244 INFO  [0x116098600] ClientImpl:485 | Closing Pulsar client with 0 producers and 1 consumers
    2021-12-03 08:53:15.244 INFO  [0x116098600] ConsumerImpl:874 | [persistent://public/default/iotjetsonjson, jupyter-sub2, 0] Closing consumer for topic persistent://public/default/iotjetsonjson
    2021-12-03 08:53:15.260 INFO  [0x70000ec70000] ConsumerImpl:930 | [persistent://public/default/iotjetsonjson, jupyter-sub2, 0] Closed consumer 0
    2021-12-03 08:53:15.260 INFO  [0x70000ec70000] ClientConnection:1508 | [192.168.1.223:58836 -> 192.168.1.210:6650] Connection closed
    2021-12-03 08:53:15.261 INFO  [0x70000ec70000] ClientConnection:1508 | [192.168.1.223:58835 -> 192.168.1.210:6650] Connection closed
    2021-12-03 08:58:47.809 INFO  [0x70000e7d5000] ConsumerStatsImpl:70 | Consumer [persistent://public/default/iotjetsonjson, jupyter-sub, 0] , ConsumerStatsImpl (numBytesRecieved_ = 588, totalNumBytesRecieved_ = 2961, receivedMsgMap_ = {[Key: Ok, Value: 1], }, ackedMsgMap_ = {}, totalReceivedMsgMap_ = {[Key: Ok, Value: 5], }, totalAckedMsgMap_ = {[Key: {Result: Ok, ackType: 0}, Value: 4], })
    2021-12-03 09:08:47.811 INFO  [0x70000e7d5000] ConsumerStatsImpl:70 | Consumer [persistent://public/default/iotjetsonjson, jupyter-sub, 0] , ConsumerStatsImpl (numBytesRecieved_ = 0, totalNumBytesRecieved_ = 2961, receivedMsgMap_ = {}, ackedMsgMap_ = {}, totalReceivedMsgMap_ = {[Key: Ok, Value: 5], }, totalAckedMsgMap_ = {[Key: {Result: Ok, ackType: 0}, Value: 4], })
    2021-12-03 09:18:47.811 INFO  [0x70000e7d5000] ConsumerStatsImpl:70 | Consumer [persistent://public/default/iotjetsonjson, jupyter-sub, 0] , ConsumerStatsImpl (numBytesRecieved_ = 0, totalNumBytesRecieved_ = 2961, receivedMsgMap_ = {}, ackedMsgMap_ = {}, totalReceivedMsgMap_ = {[Key: Ok, Value: 5], }, totalAckedMsgMap_ = {[Key: {Result: Ok, ackType: 0}, Value: 4], })



```python

```
