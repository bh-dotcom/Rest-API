# Flask Transaction API

Simple REST API built using Flask, MySQL, and Redis.

## Features
- REST endpoint to fetch user transactions
- Indexed MySQL column for performance
- Redis caching to reduce DB load
- Health check endpoint

## Tech Stack
- Flask
- MySQL
- Redis

## Setup

1. Create virtual environment:
   python -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run application:
   python run.py
