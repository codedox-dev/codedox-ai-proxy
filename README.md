# Codedox AI Proxy (Render Version)

This is a Node.js + Express backend for securely forwarding messages to OpenAI.

## 🚀 How to Deploy on Render

1. Push this project to a new GitHub repo (e.g. `codedox-ai-proxy`)
2. Go to [https://render.com](https://render.com)
3. Click **New Web Service**
4. Connect your GitHub repo
5. Set these values:
   - **Environment = Node**
   - **Build Command = npm install**
   - **Start Command = npm start**
   - **Environment Variable**:
     - `OPENAI_API_KEY = your-secret-api-key`
6. Click **Deploy**

Your AI proxy server will be live!
