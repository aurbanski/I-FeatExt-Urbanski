from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
# import pandas as pd
import re
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client
import argparse
# import matplotlib.pyplot as plt

# Based on http://adilmoujahid.com/posts/2014/07/twitter-analytics/

access_token = "377135231-oGgtj8unrSCSaxqsehC80g9BZCiukT9fpdnnB1y7"
access_token_secret = "XucJ82KGGWpHAite0K5DLjQa9bz41zC1TQa0wL3wCwbSs"
consumer_key = "IZ8u1kNdtQTPYs1F3DdcsF5ty"
consumer_secret = "WhrhP4GknpNJcY6ZGX2USb13PBGSjSBR7NJJcDFAVIyJlkTw7r"

time = time.time()
print(time)

class StdOutListener(StreamListener):

    def on_data(self, data):
        m = 0.0
        # print data
        try:
            data = json.loads(data)
            regex = re.compile(r"[Kk]anye")
            m = regex.findall(data["text"])
            if(len(m) == 0):
                print(data["text"])
                # print(data["entities"]["hashtags"])
            print(len(m))
            # print(data["text"])
        except:
            pass

        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
            help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=6448,
            help="The port the OSC server is listening on")
        args = parser.parse_args()

        client = udp_client.SimpleUDPClient(args.ip, args.port)
        message_to_send = float(len(m))
        client.send_message("/wek/inputs", message_to_send)

        # print("========")
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Kanye', 'kanye'])
