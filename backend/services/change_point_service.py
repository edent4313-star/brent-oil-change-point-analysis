import json

from backend.config import MODEL_RESULTS


def load_change_point():

    try:

        with open(MODEL_RESULTS) as file:

            return json.load(file)

    except FileNotFoundError:

        raise FileNotFoundError(
            "model_results.json not found."
        )