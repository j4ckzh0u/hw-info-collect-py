#! /usr/bin/env sh
# start flask web app
# auth: zhoujk
# date: 20190211
gunicorn flask-server:app -b 0.0.0.0:5000 --log-level debug
