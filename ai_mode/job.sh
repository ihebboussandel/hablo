#!/usr/bin/env bash
nohup python /home/pi/Documents/rgb_contr/rgb_d.py> /home/pi/Documents/logs/rgb_d.log & 2>&1 
echo $! > /home/pi/Documents/logs/pid/pid_rgb_d.log
echo 'light module stated'
nohup python /home/pi/Documents/ai_mode/main.py> /home/pi/Documents/logs/ai_mode.log & 2>&1 
echo $! > /home/pi/Documents/logs/pid/pid_ai_mode.log
echo 'aimode started';
