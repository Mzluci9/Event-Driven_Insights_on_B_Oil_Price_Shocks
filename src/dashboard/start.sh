#!/bin/bash

echo "Starting Brent Oil Price Dashboard..."
echo

echo "Starting Flask Backend..."
cd backend
python app.py &
BACKEND_PID=$!
cd ..

echo
echo "Starting React Frontend..."
cd frontend
npm start &
FRONTEND_PID=$!
cd ..

echo
echo "Dashboard is starting up..."
echo "Backend will be available at: http://localhost:5000"
echo "Frontend will be available at: http://localhost:3000"
echo
echo "Press Ctrl+C to stop all services"

# Function to cleanup processes on exit
cleanup() {
    echo "Stopping services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up signal handler
trap cleanup SIGINT SIGTERM

# Wait for user to interrupt
wait 