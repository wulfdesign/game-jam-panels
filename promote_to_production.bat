@echo off
chcp 65001 > nul
cd /d "%~dp0"
title Game Jam Panels - Promote Dev to Public Production
echo ========================================================
echo   Promoting Dev Deck ^& Assets to Public Production
echo ========================================================
echo.

python "private\promote_to_production.py"

echo.
echo ========================================================
echo   Promotion Process Complete!
echo ========================================================
pause
