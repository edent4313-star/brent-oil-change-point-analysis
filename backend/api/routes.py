from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

# --- 1. Initialization ---
app = Flask(__name__)
CORS(app)

# Define Blueprint once with a prefix. 
# This means every route below will start with /api
api = Blueprint('api', __name__, url_prefix='/api')

# --- 2. Data Loading ---
# We load this once at the top so all routes can use it
try:
    # Load Prices
    prices = pd.read_csv("data/BrentOilPrices.csv")
    prices["Date"] = pd.to_datetime(prices["Date"], format='mixed')
    prices = prices.sort_values("Date")

    # Load Events from CSV
    events_df = pd.read_csv("data/events.csv")
    events_df["Date"] = pd.to_datetime(events_df["Date"], format='mixed')
    events_df = events_df.sort_values("Date")
    print("Successfully loaded prices and events.")
    
except Exception as e:
    print(f"Error loading CSV files: {e}")
    prices = pd.DataFrame()
    events_df = pd.DataFrame()

# --- 3. API Routes ---

@api.route("/health")
def health():
    return jsonify({"status": "success", "message": "Backend is running"})

@api.route("/historical")
def historical():
    data = prices.copy()
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")
    return jsonify(data.to_dict(orient="records"))

@app.route("/kpis")
def kpis():

    latest_price = prices["Price"].iloc[-1]

    first_price = prices["Price"].iloc[0]


    percentage_change = (

        (latest_price-first_price)
        /
        first_price
        *
        100

    )


    volatility = (

        prices["Price"]
        .pct_change()
        .std()
        *
        np.sqrt(252)
        *
        100

    )


    return jsonify({

        "current_price":
            round(latest_price,2),

        "percentage_change":
            round(percentage_change,2),

        "volatility":
            round(volatility,2),

        "total_records":
            len(prices)

    })

@api.route("/volatility")
def get_volatility_data(): # Renamed to avoid conflict
    df = prices.copy()
    df["returns"] = df["Price"].pct_change()
    df["volatility"] = df["returns"].rolling(30).std() * np.sqrt(252) * 100
    df = df.dropna()
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    return jsonify(df[["Date", "volatility"]].to_dict(orient="records"))

@api.route("/events")
def get_events():
    if events_df.empty:
        return jsonify([]) # Return empty list if file is missing

    # Create a copy and format dates as strings for JSON
    data = events_df.copy()
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")
    
    # Return as list of records
    return jsonify(data.to_dict(orient="records"))

@api.route("/filter")
def filter_prices():
    try:
        start = request.args.get("start")
        end = request.args.get("end")
        df = prices.copy()
        if start:
            df = df[df["Date"] >= pd.to_datetime(start)]
        if end:
            df = df[df["Date"] <= pd.to_datetime(end)]
        
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@api.route("/change-point")
def change_point():
    # Placeholder for your Bayesian result
    return jsonify({
        "change_point_date": "2005-05-28",
        "confidence": 0.90,
        "message": "U.S.-led invasion of Iraq raised concerns about global oil supply..."
    })

# --- 4. Registration and Execution ---

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)