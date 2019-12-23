# tweeter_api_flask_app  
### Requirements
<li> windows </li>
<li> kafka installed </li>
<li> python 3.x <li>  
  
# steps

<li> copy the kafka folder to any location in the drive ex: C:\kafka\kafka_2.x\  
     start the zookeeper service  and kafka service  
     cd .\kafka\kafka_2.12-2.3.1\
     > .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties  
     > .\bin\windows\kafka-server-start.bat .\config\server.properties  
</li>

<li>
  start the application  
  >  python app_ajax.py  
  go to 127.0.0.1:5000  
</li>

<li>
  enter the twitter hashtag to get the live tweets  
  then hit the "search for hashtag" button
  after sometime hit the "gettweets" button  
</li>

