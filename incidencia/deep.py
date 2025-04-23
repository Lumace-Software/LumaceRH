from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Eres un asistente de RRHH profesional que debe ayudar a gestionar las incidencias."},
        {"role": "user", "content": "Hola, cual es tu objetivo?"},
    ],
    stream=False
)

respuesta = response.choices[0].message.content