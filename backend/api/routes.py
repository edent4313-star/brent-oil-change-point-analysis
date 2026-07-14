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
# --- 2. Data Loading (Standardized) ---
try:
    # 1. Load Prices and Force Standard Headers
    prices = pd.read_csv("data/BrentOilPrices.csv")
    
    # We take only the first two columns and force them to 'Date' and 'Price'
    # This prevents errors if your CSV uses 'date', 'price', or 'BP_Price'
    prices = prices.iloc[:, :2] 
    prices.columns = ["Date", "Price"] 
    
    # Clean and sort price data
    prices["Date"] = pd.to_datetime(prices["Date"], format='mixed')
    prices = prices.sort_values("Date").reset_index(drop=True)

    # 2. Load Events and Force Standard Headers
    events_df = pd.read_csv("data/events.csv")
    
    # Standardize event columns for the React Table/Drill-down
    # This ensures consistency even if the Excel file is edited manually
    events_df["Date"] = pd.to_datetime(events_df["Date"], format='mixed')
    events_df = events_df.sort_values("Date")

    print(f"Standardization Complete: {len(prices)} prices and {len(events_df)} events loaded.")
    
except Exception as e:
    print(f"FATAL ERROR during CSV loading: {e}")
    # Fallback to prevent server crash
    prices = pd.DataFrame(columns=["Date", "Price"])
    events_df = pd.DataFrame(columns=["Date", "Event", "Impact"])
# --- 3. API Routes ---

@api.route("/health")
def health():
    return jsonify({"status": "success", "message": "Backend is running"})

@api.route("/historical")
def get_historical():
    # 1. READ the dates sent from React
    start_date = request.args.get("start")
    end_date = request.args.get("end")
    
    # 2. Start with a fresh copy of standardized data
    df = prices.copy()
    
    # 3. APPLY FILTERS if they exist
    try:
        if start_date:
            df = df[df["Date"] >= pd.to_datetime(start_date)]
        if end_date:
            df = df[df["Date"] <= pd.to_datetime(end_date)]
    except Exception as e:
        print(f"Filter error: {e}")

    # 4. Format for JSON
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    return jsonify(df.to_dict(orient="records"))

@api.route("/kpis")
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
        "current_price": round(latest_price, 2),
        "percentage_change": round(percentage_change, 2),
        "volatility": round(volatility, 2),
        "total_records": len(prices),
        # ADD THIS LINE SO THE DASHBOARD KNOWS WHERE THE GREEN LINE GOES
        "change_point_date": "2005-05-28" 
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
        "mu_before": 21.27,
        "mu_after": 75.66,
        "message": "U.S.-led invasion of Iraq raised concerns about global oil supply..."
    })

@api.route("/event-correlation")
def event_correlation():
    correlation_results = []
    
    for _, event in events_df.iterrows():
        event_date = event['Date']
        
        # Look for price on the event day
        try:
            # Get price at event date, and 30 days later
            price_at_event = prices[prices['Date'] >= event_date].iloc[0]['Price']
            price_30d_after = prices[prices['Date'] >= (event_date + pd.Timedelta(days=30))].iloc[0]['Price']
            
            impact_val = ((price_30d_after - price_at_event) / price_at_event) * 100
            
            correlation_results.append({
                "Date": event_date.strftime('%Y-%m-%d'),
                "Event": event['Event'],
                "Price_At_Event": round(price_at_event, 2),
                "Post_30d_Impact": f"{round(impact_val, 2)}%",
                "Impact_Type": "Negative Correlation" if impact_val < 0 else "Positive Correlation"
            })
        except:
            continue # Skip if date is out of range
            
    return jsonify(correlation_results)
# --- 4. Registration and Execution ---

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


    