hydrolog
========

hydrolog

currently deploy to /devroot/hydrolog

to save air temp/humidity every 1 minute, add via crontab -e
*/1     *       *       *       *       /usr/bin/python /devroot/hydrolog/air_temp_humid.ex.py &> /dev/null
