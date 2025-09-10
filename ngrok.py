from pyngrok import ngrok
import threading, time, os

def run_streamlit():
    os.system("streamlit run app.py --server.headless true --server.port 8501")

threading.Thread(target=run_streamlit).start()
time.sleep(5)

public_url = ngrok.connect(8501)
print("🌐 PharmaPal is live at:", public_url)
