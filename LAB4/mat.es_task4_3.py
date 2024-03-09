import paho.mqtt.client as mqtt  
import time  
import json  
data = [] 


def on_connect(client, userdata, flags, rc):  
    print("Connection returned result: " + str(rc))  
    client.subscribe("ece180d/test/team6/#", qos=1)  

def on_disconnect(client, userdata, rc):  
    if rc != 0:  
        print('Unexpected Disconnect')  
    else:  
        print('Expected Disconnect')  

def on_message(client, userdata, message):  
    mes = message.payload 
    mes_decoded = mes.decode()  

    try:  
        data.append(json.loads(mes_decoded))  
        if len(data) > 5:  
            data.pop(0)  
        
        forward = all(sample['acceleration']['x'] > 70 for sample in data[-5:])
        up = all(sample['acceleration']['z'] < 980 for sample in data[-5:])
        backward = all(sample['acceleration']['y'] > 70 for sample in data[-5:])
        idle = all(sample['acceleration']['x']< 40 and sample['acceleration']['y'] < 40 and sample['acceleration']['z'] > 990 and sample['acceleration']['z'] < 1040 for sample in data)
        
        if forward:  
            print("forward")  
        if up:  
            print("up")
        if  backward:
            print("backward")  
        if idle:  
            print("idle")  

    except json.JSONDecodeError as e:  
        print(f"Error decoding JSON: {e}") 

client = mqtt.Client()  
client.on_connect = on_connect  
client.on_disconnect = on_disconnect  
client.on_message = on_message 

client.connect_async('mqtt.eclipseprojects.io')  
client.loop_start()  

while True:  
    pass  

client.loop_stop()  
client.disconnect()  
