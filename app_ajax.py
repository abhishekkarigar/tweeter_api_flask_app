#!C:\Python36\python
from flask import Flask, render_template, send_file,request
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json 
from kafka import SimpleProducer,KafkaClient
from kafka import KafkaConsumer
from bs4 import BeautifulSoup as Soup

''' the following keys and tokens needs  to be updated for the new twitter developer account'''
ckey='XXXXXXX' 
csecret='XXXXXXX'
atoken='XXXXXXX'
asecret='XXXXXXX'

app = Flask(__name__)

class Listener(StreamListener):

    def on_data(self, raw_data):
        try:
            tweet = raw_data.split(',"text":"')[1].split(',"source"')[0]
            tweet = str(time.time())+" :: "+tweet
            tweet.encode('utf-8')
            print (tweet)
            producer.send_messages("tests", bytes(tweet,encoding='utf-8'))
            #producer.send_messages("tests",str(tweet))
        except BaseException as e:
            print("error"+str(e))
            time.sleep(5)

    def on_error(self, status_code):
        print(status_code)

    def on_limit(self, track):
        print("rate limit exceeded , sleep for 15 minutes")
        time.sleep(15*60)
        return True


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/getfromserver",methods=['POST','GET'])
def getfromserver():
	if request.method=='POST':
		data = request.form.get('mydata')
		return data
	else:
		return "invalid request method\n"

@app.route('/searchfromtwitter',methods=['POST','GET'])
def searchtweets():
	if request.method=='POST':
		result = request.form.get('mydata')
		auth = OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)
		twitterStream = Stream(auth, Listener())
		twitterStream.filter(track=[result])

@app.route('/gettweets',methods=['GET','POST'])
def gettweets():
    try:
        consumer = KafkaConsumer('tests',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',enable_auto_commit=True)
        for msg in consumer:
            #msg.value.decode('utf-8')
            #return msg.value
            time.sleep(5)
            return str(msg.value)
    except Exception as e:
        print(str(e))

'''	
@app.route("/getfiles",methods=["POST","GET"])
def getfiles():
	try:
		return send_file('./templates/data.txt')
	except Exception as e:
		return str(e)
'''
		
if __name__=="__main__":
	kafka = KafkaClient('localhost:9092')
	producer = SimpleProducer(kafka)
	app.run(debug=True)
	