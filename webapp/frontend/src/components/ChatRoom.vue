<template>
  <div class="chat-container">
    <div class="header">WebSocket Chat</div>
    <div class="connection-form" v-if="!connected">
      <input v-model="username" @keyup.enter="connect" placeholder="Enter your username" :disabled="connecting" />
      <button @click="connect" :disabled="connecting || !username">{{ connecting ? 'Connecting...' : 'Connect' }}</button>
    </div>
    <div class="status" :class="connected ? 'connected' : 'disconnected'">
      {{ connected ? 'Connected' : 'Disconnected' }}
    </div>
    <div class="chat-area" v-if="connected">
      <div class="messages">
        <div v-for="(msg, idx) in messages" :key="idx" :class="['message', msg.type]">
          {{ msg.text }}
        </div>
      </div>
      <div class="message-input">
        <input v-model="message" @keyup.enter="sendMessage" placeholder="Type your message..." :disabled="!connected" />
        <button @click="sendMessage" :disabled="!message || !connected">Send</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref('')
const message = ref('')
const messages = ref([])
const connected = ref(false)
const connecting = ref(false)
let ws = null

function connect() {
  if (!username.value) return
  connecting.value = true
  ws = new WebSocket(`ws://localhost:8000/ws/${encodeURIComponent(username.value)}`)
  ws.onopen = () => {
    connected.value = true
    connecting.value = false
  }
  ws.onmessage = (event) => {
    const text = event.data
    // 没有冒号的消息视为系统消息
    if (!text.includes(':')) {
      messages.value.push({ text, type: 'system' })
    } else if (text.startsWith(username.value + ': ') && text.length > username.value.length + 2) {
      messages.value.push({ text, type: 'own' })
    } else {
      messages.value.push({ text, type: 'other' })
    }
    scrollToBottom()
  }
  ws.onclose = () => {
    connected.value = false
    connecting.value = false
    ws = null
  }
  ws.onerror = () => {
    connected.value = false
    connecting.value = false
  }
}

function sendMessage() {
  if (message.value && ws && ws.readyState === WebSocket.OPEN) {
    ws.send(message.value)
    message.value = ''
  }
}

function scrollToBottom() {
  setTimeout(() => {
    const el = document.querySelector('.messages')
    if (el) el.scrollTop = el.scrollHeight
  }, 0)
}
</script>

<style scoped>
.chat-container {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  width: 100%;
  max-width: 1200px;
  min-width: 600px;
  margin: 40px auto;
  display: flex;
  flex-direction: column;
  padding: 0;
  height: 70vh;
}
.header {
  background: #f5f5f5;
  color: #333;
  padding: 20px;
  text-align: center;
  font-size: 1.4em;
  font-weight: bold;
  border-bottom: 1px solid #eee;
}
.connection-form {
  display: flex;
  gap: 8px;
  padding: 16px;
  border-bottom: 1px solid #eee;
}
.status {
  padding: 8px 16px;
  font-size: 0.95em;
  text-align: center;
  background: #f8f8f8;
  color: #888;
}
.status.connected {
  color: #2e7d32;
}
.status.disconnected {
  color: #c62828;
}
.chat-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  /* 允许flex子项溢出时滚动 */
}
.messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background: #fafafa;
  min-height: 0;
  display: flex;
  flex-direction: column;
}
.message {
  margin-bottom: 10px;
  padding: 8px 12px;
  border-radius: 6px;
  max-width: 80%;
  word-break: break-all;
  font-size: 1em;
  display: inline-block;
}
.message.own {
  background: #e3f2fd;
  color: #1976d2;
  align-self: flex-end;
  margin-left: auto;
  margin-right: 0;
  text-align: right;
}
.message.other {
  background: #f1f1f1;
  color: #333;
  align-self: flex-start;
  margin-right: auto;
  margin-left: 0;
  text-align: left;
}
.message.system {
  background: transparent;
  color: #bbb;
  text-align: center;
  margin: 10px auto;
  font-style: italic;
  box-shadow: none;
  max-width: 100%;
  font-size: 0.85em;
}
.message-input {
  display: flex;
  gap: 8px;
  padding: 16px 20px;
  border-top: 1px solid #eee;
  background: #fff;
}
.message-input input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1em;
}
.message-input button {
  padding: 10px 20px;
  background: #1976d2;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  font-size: 1em;
  transition: background 0.2s;
}
.message-input button:disabled {
  background: #bdbdbd;
  cursor: not-allowed;
}
</style> 