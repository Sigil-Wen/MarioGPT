import os
import openai
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


prompt = """You are a player controlling Mario. Your goal is to beat mario. Write the controls for mario.
# How to Play
* use LEFT/RIGHT/DOWN key to control player
* use key 'a' to JUMP
* use key 's' to SHOOT firewall or run

Write the controls for mario beating 1-1. You can use the following commands:

(LEFT, 4 seconds) //indicates it holds left for 4 seconds
(JUMP, 1 second) //indicates it holds jump for 1 second
(RIGHT JUMP, 1 second) //indicates it holds right and jump for 1 second
"""

summarization = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
print(summarization.choices[0].message.content)