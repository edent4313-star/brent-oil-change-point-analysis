from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

BRENT_DATA = DATA_DIR / "BrentOilPrices.csv"

EVENT_DATA = DATA_DIR / "events.csv"

MODEL_RESULTS = DATA_DIR / "model_results.json"