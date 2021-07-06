#!/usr/bin/env bash
# This code write by Mr.nope
# Installing Matrix 1.3.1
if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    clear
    echo "Installing..."
    sleep 2
    chmod +x run.py
    pkg install update
    pkg install upgrade
    pkg install python3
    pkg install python
    echo ""
    echo "Installing..., Finish...!"
    echo ""
    exit 1
else
  if [[ "$(id -u)" -ne 0 ]]; then
    chmod +x run.py
    echo ""
    echo "Please, Run This Programm as Root!"
    exit 1
  fi
  clear
  echo "Installing..."
  sleep 2
  chmod +x run.py
  apt update
  apt upgrade
  apt install python
  apt install python3
  echo ""
  echo "Installing..., Finish...!"
  echo ""
  exit 1
fi