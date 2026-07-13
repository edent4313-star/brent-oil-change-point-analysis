import pymc as pm
import numpy as np

from src.preprocessing import prepare_change_point_series


def build_change_point_model(Log_Return):

    try:

        if len(Log_Return)==0:

            raise ValueError(
                "Empty price series"
            )


        series = prepare_change_point_series(Log_Return)
        n=len(series)

        index=np.arange(n)


        with pm.Model() as model:


            tau = pm.DiscreteUniform(
                "tau",
                lower=0,
                upper=n-1
            )


            mu1 = pm.Normal(
                "mu1",
                mu=np.mean(series),
                sigma=np.std(series)*2
            )


            mu2 = pm.Normal(
                "mu2",
                mu=np.mean(series),
                sigma=np.std(series)*2
            )


            sigma = pm.HalfNormal(
                "sigma",
                sigma=np.std(series)
            )


            mean = pm.math.switch(
                index < tau,
                mu1,
                mu2
            )


            pm.Normal(
                "price",
                mu=mean,
                sigma=sigma,
                observed=series
            )


        return model



    except Exception as e:

        raise RuntimeError(
            f"Model creation failed: {e}"
        )



def build_change_point_model_fast(series):
    # Ensure we are using the series passed in
    n = len(series)
    index = np.arange(n)
    
    # Calculate starting guesses based ONLY on the input series
    data_mean = np.mean(series)
    data_std = np.std(series)

    with pm.Model() as model:
        # 1. Latent Tau (Time)
        tau_latent = pm.Uniform("tau_latent", 0, 1)
        tau = pm.Deterministic("tau", tau_latent * n)

        # 2. Means (Before and After)
        # We use the mean of the [0,1] data as the starting point
        mu1 = pm.Normal("mu1", mu=data_mean, sigma=data_std * 2)
        mu2 = pm.Normal("mu2", mu=data_mean, sigma=data_std * 2)

        # 3. Standard Deviation (Noise)
        sigma = pm.HalfNormal("sigma", sigma=data_std)

        # 4. The Sigmoid Switch
        weight = pm.math.sigmoid((index - tau) * 10) 
        mean = pm.Deterministic("mean", (1 - weight) * mu1 + weight * mu2)

        # 5. Observed Data
        pm.Normal("obs", mu=mean, sigma=sigma, observed=series)

    return model

def run_sampler(
        model,
        draws=1000,
        tune=1000
):

    try:

        with model:

            trace = pm.sample(
                draws=draws,
                tune=tune,
                chains=4,
                cores=4,
                target_accept=0.90,
                return_inferencedata=True
            )


        return trace


    except Exception as e:

        raise RuntimeError(
            f"MCMC sampling failed: {e}"
        )
    
