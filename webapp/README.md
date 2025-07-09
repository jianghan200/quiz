# WebSocket Chat Application

A real-time chat application built with FastAPI and WebSockets that allows multiple clients to connect and exchange messages in real-time.

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

## Backend server
1. Start the server:
```bash
python main.py
```

## Frontend (Vue3) 

1. 进入 `frontend` 目录：
   ```bash
   cd frontend
   ```
2. 安装依赖（如未安装）：
   ```bash
   npm install
   ```
3. 启动开发服务器：
   ```bash
   npm run dev
   ```
4. open http://localhost:5173 to chat 


## Usage

1. **Connect to the chat**: Enter your username and click "Connect"
2. **Send messages**: Type your message and press Enter or click "Send"
3. **View messages**: All messages from other users will appear in the chat area
4. **Disconnect**: Close the browser tab or refresh the page to disconnect


## API Endpoints
- `WebSocket /ws/{username}` - WebSocket endpoint for real-time chat

## Architecture

The application consists of:

- **FastAPI Server** (`main.py`): Handles WebSocket connections and message broadcasting
- **ConnectionManager**: Manages active WebSocket connections and usernames
- **Vue3 Frontend** (`frontend/`): Modern web interface for the chat, built with Vue3 and Vite

## WebSocket Protocol

- **Connection**: `ws://localhost:8000/ws/{username}`
- **Message Format**: Plain text messages
- **Broadcast Format**: `{username}: {message}`


