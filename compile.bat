@echo off
echo Building...
pyinstaller --exclude matplotlib --exclude scipy --exclude pandas --noconfirm --onefile --windowed .\lmao.pyw
if %ERRORLEVEL% NEQ 0 goto ERR
goto EOF


:ERR
echo ERROR!!!!!! >>>:((
pause

:EOF
move .\dist\*.exe .\
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__
pause
echo Done. Exitting in 5 seconds...
timeout 5 > NUL
