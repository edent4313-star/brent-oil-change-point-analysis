import numpy as np



def extract_change_point(trace):

    try:

        tau_samples = (
            trace
            .posterior["tau"]
            .values
            .flatten()
        )


        tau = int(
            np.median(tau_samples)
        )


        return tau


    except Exception as e:

        raise RuntimeError(
            f"Cannot extract change point: {e}"
        )



def quantify_impact(
        df,
        tau
):

    try:

        before=df.iloc[:tau]

        after=df.iloc[tau:]


        before_mean=before["Price"].mean()

        after_mean=after["Price"].mean()


        change=((after_mean-before_mean)
                /before_mean)*100


        return {

            "before_mean":before_mean,

            "after_mean":after_mean,

            "percentage_change":change

        }


    except Exception as e:

        raise RuntimeError(
            f"Impact calculation failed: {e}"
        )