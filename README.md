# Codedox AI Proxy

This is a simple Node.js and Express server that forwards messages to OpenAI's GPT model.

## Usage
1. Deploy to Render
2. Set the environment variable: `OPENAI_API_KEY`
3. POST to /chat with JSON: { "message": "your text" }

## Example Request
POST /chat
{
  "message": "Hello"
}
