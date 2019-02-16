host="$(hostname -I)"
echo "${host}"
host=${host//[[:blank:]]/}
echo "50:100:0" > /var/www/html/logs/color_status.log

#nohup python ../rgb_contr/rgb_d.py > rgb_d.log & 2>&1 
#echo $! > pid_rgb.log
#echo 'led api started '

nohup ffserver > ffserver.log & 2>&1 
echo $! > pid_ffserver.log
echo 'ffserver started'
echo $host

nohup ffmpeg -re -f alsa -ac 2 -i plughw:CARD=Device -ar 44100 -filter:a "volume=-20dB" -ab 38k http://${host}:8090/feed1.ffm > stream.log & 2>&1 
echo $! > pid_stream.log
echo 'ffserver started';
