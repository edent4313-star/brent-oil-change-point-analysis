from flask import Blueprint
from flask import request
from flask import jsonify
from backend.services.data_service import load_price_data
from backend.services.event_service import load_events
from backend.services.statistics_service import get_statistics
from backend.services.volatility_service import get_volatility
from backend.services.change_point_service import load_change_point


api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


@api.route("/health")
def health():

    return jsonify({

        "status": "success",

        "message": "Backend is running"

    })
@api.route("/prices")
def prices():

    df = load_price_data()

    return jsonify(

        df.to_dict(
            orient="records"
        )

    )
@api.route("/events")
def events():

    df = load_events()

    return jsonify(

        df.to_dict(
            orient="records"
        )

    )
@api.route("/statistics")
def statistics():

    return jsonify(
        get_statistics()
    )

@api.route("/volatility")
def volatility():

    df = get_volatility()

    return jsonify(
        df.to_dict(
            orient="records"
        )
    )

@api.route("/change-point")
def change_point():

    return jsonify(
        load_change_point()
    )

@api.route("/filter")
def filter_prices():

    try:

        start = request.args.get("start")

        end = request.args.get("end")

        df = load_price_data()

        if start:

            df = df[
                df["Date"] >= start
            ]

        if end:

            df = df[
                df["Date"] <= end
            ]

        return jsonify(
            df.to_dict(
                orient="records"
            )
        )

    except Exception as e:

        return jsonify({

            "status":"error",

            "message":str(e)

        }),400