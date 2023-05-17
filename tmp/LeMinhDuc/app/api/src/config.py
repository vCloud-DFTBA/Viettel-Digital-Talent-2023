import os

from dotenv import load_dotenv

# Prefer system environment variables
load_dotenv(override=False)

# Load specific environment variables
MONGO_URI = os.getenv("MONGO_URI")
