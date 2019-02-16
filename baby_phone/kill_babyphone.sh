#!/usr/bin/env bash
kill -9 "$(< /home/pi/Documents/logs/pid/pid_rgb.log)"
kill -9 "$(< /home/pi/Documents/logs/pid/pid_stream.log)"
kill -9 "$(< /home/pi/Documents/logs/pid/pid_ffserver.log)"

