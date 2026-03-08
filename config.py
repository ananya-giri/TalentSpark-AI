import os
import sys
from dotenv import load_dotenv

# Disable CrewAI telemetry immediately
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from crewai import LLM

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY or any(x in GOOGLE_API_KEY for x in ["your_gemini_api_key_here", "PASTE_YOUR_KEY_HERE"]):
    print("\n❌ ERROR: GOOGLE_API_KEY not found or is still a placeholder.")
    print("Please open the '.env' file and replace 'PASTE_YOUR_KEY_HERE' with your real API key.")
    print("You can get a free key at: https://aistudio.google.com/")
    sys.exit(1)

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