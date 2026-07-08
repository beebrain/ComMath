#!/bin/bash

echo "=== Google Chrome Remote Debugging Launcher ==="
echo "This script starts a separate, clean instance of Google Chrome"
echo "with remote debugging enabled on port 9222 so the AI agent can control it."
echo ""
echo "Launching Google Chrome in debug mode..."

# Run Chrome with remote debugging and a temporary profile directory
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/chrome_dev_profile" \
  >/dev/null 2>&1 &

echo "Waiting for Chrome to initialize on port 9222..."
for i in {1..6}; do
  sleep 1
  if curl -s http://localhost:9222/json/version | grep -q "webSocketDebuggerUrl"; then
    echo ""
    echo "[SUCCESS] Google Chrome Debugging is now active on port 9222!"
    echo "The AI agent can now connect to and control this browser window."
    exit 0
  fi
  echo -n "."
done

echo ""
echo "[ERROR] Failed to connect to Chrome remote debugging on port 9222."
echo "Please make sure Google Chrome is installed in /Applications/Google Chrome.app."
exit 1
