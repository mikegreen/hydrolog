hydrolog
========

hydrolog

## Raspberry Pi setup:

currently deploy to /devroot/hydrolog

# make lib/Adafruit_DHT executable
# run from console
cd /devroot/hydrolog/lib
chmod 744 Adafruit_DHT

# rename and update dbCreds_example.py to dbCreds.py with your mysql server info
mv dbCreds_example.py dbCreds.py
nano /devroot/hydrolog/dbCreds.py

# test
cd /devroot/hydrolog
python hydrologUpdate.py

# to save air temp/humidity every 1 minute, add via crontab -e
# the &> /dev/null prevents emails from queuing up if you dont have an email server for cron status emails
*/1     *       *       *       *       /usr/bin/python /devroot/hydrolog/air_temp_humid.ex.py &> /dev/null


## Database setup

run sqls in ddl folder, will create:
sensor_readings table
vw_current_values view
vw_dht22_readnings view

todo: make db names better

## Web server setup
todo