import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAa9Z7LICLKXCx66MBuiLal4CinnWjROFQ"))

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("Write a short poem about AI and humans working together.")
print(response.text)
