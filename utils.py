import os
from pathlib import Path
from dotenv import load_dotenv
from config import PROJECT_ROOT

def init_env() -> None:
    load_dotenv(PROJECT_ROOT/"myenv.env")