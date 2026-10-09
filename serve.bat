@echo off
chcp 65001 > nul
cd /d "%~dp0"
title Game Jams Panel - Public Slide Deck (Port 3026)
echo ===================================================
echo   Game Jams: Thought to Thing in 48 Hours
echo   GeekGirlCon 2026 - Public Presentation Deck
echo ===================================================
echo.
echo Starting Production Slide Deck on Port 3026...
echo Access in browser: http://127.0.0.1:3026/
echo (Press Ctrl+C to stop the server)
echo ===================================================
echo.
python server.py
echo.
echo Server stopped or exited.
pause
