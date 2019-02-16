#!/usr/bin/env bash
kill -9 "$(< /home/pi/Documents/logs/pid/pid_rgb_d.log)"
kill -9 "$(< /home/pi/Documents/logs/pid/pid_ai_mode.log)"

#kill -9 "$(< pid_stream.log)"
#kill -9 "$(< pid_ffserver.log)"

