#!/bin/bash
# Script for running Paperclip server
# Location: /mnt/c/Users/olivia/Documents/website_book/run-paperclip.sh

cd /mnt/c/Users/olivia/Documents/website_book

# Run Paperclip in background
npx @paperclip-ui/paperclip@latest dev --port 3100 &

echo "Paperclip server starting on port 3100..."
echo "Waiting for server to be ready..."

# Wait for server to be ready
for i in {1..30}; do
    if curl -s http://localhost:3100/api/adapters > /dev/null 2>&1; then
        echo "Paperclip is ready!"
        curl -s http://localhost:3100/api/adapters
        exit 0
    fi
    sleep 1
done

echo "Timeout waiting for Paperclip to start"
exit 1