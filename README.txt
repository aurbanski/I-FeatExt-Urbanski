KanyeStream

Link for Download
[Github](https://github.com/aurbanski/KanyeStream/)

Goals

I wanted to always know the frequency that the name of our savior Kanye West was being used on Twitter.

Tools

I used python-osc to send OSC messages, tweepy to stream Twitter, json to load twitter data, and re to match regex expressions.

What I Accomplished

I made a Twitter streamer that streams tweets about Kanye and outputs the frequency, I used it with Wekinator and the number/color classifier to real time update the number of times Kanye is mentioned in a Kanye related tweet.

Model Used

I used a neural network because it was the default, but any model would work fine because I was outputting messages at discrete intervals. As far as I can tell it works fine with regression type models but classification models would work fine too.

What Can It Be Used For?

It can be used to stream the frequency of someones name in the most recent tweets about that person. And it is setup
to send OSC messages with that data.

Setup

To run the streaming, you can simply run `$python Assignment5.py` and this will start the streaming. In order to set it 
up with Wekinator I also have the file Assignment5Train.py which I used to train. I just changed the message_to_send
variable so that I could train different classes before I started the streamer. 

I used http://adilmoujahid.com/posts/2014/07/twitter-analytics/ as a reference to learn how to stream tweets with
python
