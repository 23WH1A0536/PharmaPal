from pyngrok import ngrok
import threading
import os
import time

def run():
    os.system("streamlit run app.py")

threading.Thread(target=run).start()
time.sleep(5)
public_url = ngrok.connect(addr="8501")
print(f"🔗 Your app is live: {public_url}")
