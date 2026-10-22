@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo ========================================================
echo   Syncing Heather Coles Art to Dev ^& Public Assets
echo ========================================================
echo.

if not exist "private\dev_site\assets\slides" mkdir "private\dev_site\assets\slides"
if not exist "private\dev_site\assets\games" mkdir "private\dev_site\assets\games"
if not exist "assets\slides" mkdir "assets\slides"
if not exist "assets\games" mkdir "assets\games"

echo [1/2] Copying Kitten Clicker Title Screen (Slide 6)...
copy /Y "private\intake\Kitten_Clicker_title_screen_HeatherColes.png" "private\dev_site\assets\slides\Kitten_Clicker_title_screen_HeatherColes.png"
copy /Y "private\intake\Kitten_Clicker_title_screen_HeatherColes.png" "private\dev_site\assets\games\Kitten_Clicker_title_screen_HeatherColes.png"
copy /Y "private\intake\Kitten_Clicker_title_screen_HeatherColes.png" "assets\slides\Kitten_Clicker_title_screen_HeatherColes.png"
copy /Y "private\intake\Kitten_Clicker_title_screen_HeatherColes.png" "assets\games\Kitten_Clicker_title_screen_HeatherColes.png"

echo [2/2] Copying Kitten Clicker Animation GIF (Slide 7)...
copy /Y "private\intake\kitten_Clicker_animation-HeatherColes01WEB.gif" "private\dev_site\assets\slides\kitten_Clicker_animation-HeatherColes01WEB.gif"
copy /Y "private\intake\kitten_Clicker_animation-HeatherColes01WEB.gif" "private\dev_site\assets\games\kitten_Clicker_animation-HeatherColes01WEB.gif"
copy /Y "private\intake\kitten_Clicker_animation-HeatherColes01WEB.gif" "assets\slides\kitten_Clicker_animation-HeatherColes01WEB.gif"
copy /Y "private\intake\kitten_Clicker_animation-HeatherColes01WEB.gif" "assets\games\kitten_Clicker_animation-HeatherColes01WEB.gif"

echo.
echo ========================================================
echo [OK] Art synchronized to both Dev and Public production!
echo ========================================================
pause
