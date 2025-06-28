import express from 'express';
import fetch from 'node-fetch';
import dotenv from 'dotenv';
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.post('/chat', async (req, res) => {
  const { message } = req.body;

  console.log('Received message:', message);

  if (!message) {
    return res.status(400).json({ error: 'No message provided' });
  }

  try {
    const openaiRes = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: message }]
      })
    });

    const data = await openaiRes.json();
    console.log('OpenAI response:', data);

    if (data.error) {
      return res.status(500).json({ error: data.error.message });
    }

    res.status(200).json({ response: data.choices[0].message.content });
  } catch (err) {
    console.error('Error talking to OpenAI:', err);
    res.status(500).json({ error: 'Something went wrong.' });
  }
});

app.get('/', (req, res) => {
  res.send('AI Proxy is running.');
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
