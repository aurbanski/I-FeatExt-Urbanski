from pythonosc import osc_message_builder
from pythonosc import udp_client
import argparse

while True:
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
            help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=6448,
            help="The port the OSC server is listening on")
        args = parser.parse_args()

        client = udp_client.SimpleUDPClient(args.ip, args.port)
        # Change this value to train
        message_to_send = 5.0

        client.send_message("/wek/inputs", message_to_send)
