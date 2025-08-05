@echo off
echo Starting Brent Oil Price Dashboard...
echo.

echo Starting Flask Backend...
cd backend
start "Flask Backend" cmd /k "python app.py"
cd ..

echo.
echo Starting React Frontend...
cd frontend
start "React Frontend" cmd /k "npm start"
cd ..

echo.
echo Dashboard is starting up...
echo Backend will be available at: http://localhost:5000
echo Frontend will be available at: http://localhost:3000
echo.
echo Press any key to exit this script (services will continue running)
pause > nul 