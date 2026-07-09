def find_nearest_event(
        events,
        change_date
):

    try:

        if events.empty:

            raise ValueError(
                "Event dataset empty"
            )


        events=events.copy()


        events["Difference"] = abs(
            events["Date"]
            -
            change_date
        )


        return (
            events
            .sort_values(
                "Difference"
            )
            .iloc[0]
        )


    except Exception as e:

        raise RuntimeError(
            f"Event matching failed: {e}"
        )