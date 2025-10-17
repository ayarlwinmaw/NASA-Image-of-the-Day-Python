import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# Prepare API Key & URL
api_key = os.getenv('API_KEY')
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

print(api_key)

# Get the request data as a dictionary
response = requests.get(url)
data = response.json()

# Extract the image title, url and explanation
title= data['title']
image_url = data['url']
explanation = data['explanation']

# Download the image
image_filepath = "image.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)


