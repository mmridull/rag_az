#!/bin/bash
# startup.sh
echo "Starting server..."
exec gunicorn rag_app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
chmod +x startup.sh
