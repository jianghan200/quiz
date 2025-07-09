from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import uvicorn

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.usernames: dict = {}  # Map WebSocket to username

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.usernames[websocket] = username
        # Notify all clients about new user joining, better to add "joined the chat" as postfix
        await self.broadcast(f"{username} joined the chat") 

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            username = self.usernames.get(websocket, "Unknown")
            self.active_connections.remove(websocket)
            if websocket in self.usernames:
                del self.usernames[websocket]
            return username
        return None

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                # Remove disconnected clients
                self.active_connections.remove(connection)
                if connection in self.usernames:
                    del self.usernames[connection]

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            
            # Broadcast message with username prefix
            message = f"{username}: {data}"
            await manager.broadcast(message)
            
    except WebSocketDisconnect:
        # Handle client disconnection
        disconnected_username = manager.disconnect(websocket)
        if disconnected_username:
            await manager.broadcast(f"{disconnected_username} left the chat!")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 