#!/usr/bin/env bash


set -e

echo "Pulling latest code..."
git pull origin main

echo " Stopping old container..."
sudo docker stop quiz-game || true
sudo docker rm quiz-game || true
echo " Building new image..."
sudo docker build -t quiz-game .
echo "▶️ Starting container..."
sudo docker run -d \
  -p 8501:8501 \
  --name quiz-game \
  --restart unless-stopped \
  quiz-game
echo "✅ Deployment complete"

