#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pulsar
client = pulsar.Client('pulsar://nvidia-desktop:6650')
producer = client.create_producer('persistent://meetup/newjersey/first')
producer.send(('Simple Text Message').encode('utf-8'))
client.close()


# In[ ]:


import pulsar
client = pulsar.Client('pulsar://nvidia-desktop:6650')
consumer = client.subscribe('persistent://meetup/newjersey/first',subscription_name='my-sub')
while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)
client.close()


# In[ ]:


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


# In[ ]:


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


# In[4]:


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


# In[ ]:




