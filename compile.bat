@echo off
echo Building...
pyinstaller --noconfirm --onefile --windowed .\lmao.pyw
if %ERRORLEVEL% NEQ 0 goto ERR
goto EOF


:ERR
echo ERROR!!!!!! >>>:((
pause

:EOF
echo Done. Exitting in 5 seconds...
timeout 5 > NUL
