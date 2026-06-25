#!/bin/bash

PORT=8001

echo "Serving directory: $(pwd)"
echo "Port: $PORT"

while true; do
  echo "[INFO] Starting server at $(date)"
  caffeinate -dims python3 -m http.server "$PORT"
  echo "[WARN] Server stopped/crashed at $(date)"
  echo "[INFO] Restarting in 2 seconds..."
  sleep 2
done
