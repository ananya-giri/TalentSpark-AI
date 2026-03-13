import os
import sys
import streamlit as st  # ADD THIS LINE
from dotenv import load_dotenv

# Disable CrewAI telemetry immediately
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from crewai import LLM

# Load environment variables
load_dotenv()

# MODIFIED: Check Streamlit secrets FIRST, then .env file
def get_api_key():
    # Try Streamlit secrets first (for cloud)
    try:
        return st.secrets["GOOGLE_API_KEY"]
    except:
        # Fall back to .env file (for local)
        return os.getenv("GOOGLE_API_KEY")

GOOGLE_API_KEY = get_api_key()

# MODIFIED: Better error handling without sys.exit()
if not GOOGLE_API_KEY or any(x in GOOGLE_API_KEY for x in ["your_gemini_api_key_here", "PASTE_YOUR_KEY_HERE"]):
    print("\n❌ ERROR: GOOGLE_API_KEY not configured correctly.")
    print("\n📌 **For Local Development:**")
    print("   - Open the '.env' file and replace 'PASTE_YOUR_KEY_HERE' with your real API key")
    print("\n📌 **For Cloud Deployment (Streamlit Community Cloud):**")
    print("   - Go to your app dashboard → Settings → Secrets")
    print("   - Add: GOOGLE_API_KEY = \"your-actual-api-key-here\"")
    print("\n🔑 Get a free key at: https://aistudio.google.com/")
    
    # DON'T use sys.exit() - it crashes the app
    # Instead, set a flag that your app can check
    GOOGLE_API_KEY = None  # This will cause graceful failure later

# Only proceed if we have a valid key
if GOOGLE_API_KEY:
    # Set API keys
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GEMINI_API_KEY"] = GOOGLE_API_KEY

    # CrewAI Gemini configuration
    llm = LLM(
        model="gemini/gemini-2.5-flash",
        temperature=0.2,    api_key=GOOGLE_API_KEY
    )

    AGENT_CONFIG = {
        "llm": llm,
        "verbose": True,
        "allow_delegation": False
    }
else:
    # Create empty config - your app should handle this gracefully
    llm = None
    AGENT_CONFIG = {}
    print("⚠️ API key not configured. Please check the instructions above.")
