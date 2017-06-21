# Visa-Working-Flow-Chat-Bot
Working Flow Chat Bot for Visa Card.

## How to run
* dowload the ChatScript engine from https://github.com/bwilcox-1234/ChatScript
* execute command "cp -R
Visa-Working-Flow-Chat-Bot/data/* ChatScript/RAWDATA/". copy the files in "Visa-Working-Flow-Chat-Bot/data" to "ChatScript/RAWDATA/".
* cd ChatScript/BINARIES
* run the ChatScript engine by exexute "./ChatScript port=1092"
* cd ~/Visa-Working-Flow-Chat-Bot/
* start the server by running command "nohup python CS_web_server.py &"
* testing the bot by running "python server_test.py"