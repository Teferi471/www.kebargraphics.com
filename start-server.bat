@echo off
echo Starting Kebar Graphics Website Server...
echo.
echo Your website will be available at:
echo http://localhost:8000
echo.
echo To access from phone (same WiFi):
echo 1. Find your computer's IP address (run: ipconfig)
echo 2. Use http://YOUR-IP-ADDRESS:8000 on phone
echo.
echo Press Ctrl+C to stop the server
echo.
python server.py
pause