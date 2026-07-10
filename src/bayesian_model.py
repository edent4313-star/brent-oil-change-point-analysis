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


def build_change_point_model_fast(prices):
    series = prepare_change_point_series(prices)
    n = len(series)
    index = np.arange(n)

    with pm.Model() as model:
        # 1. We use a continuous Uniform for tau (this allows the fast NUTS sampler)
        # We scale it between 0 and 1 for stability, then multiply by n
        tau_latent = pm.Uniform("tau_latent", 0, 1)
        tau = pm.Deterministic("tau", tau_latent * n)

        # 2. Priors (keep these the same)
        mu1 = pm.Normal("mu1", mu=np.mean(series), sigma=np.std(series)*2)
        mu2 = pm.Normal("mu2", mu=np.mean(series), sigma=np.std(series)*2)
        sigma = pm.HalfNormal("sigma", sigma=np.std(series))

        # 3. The "Fast Switch" (Sigmoid)
        # Instead of index < tau, we use a steep curve. 
        # This allows the sampler to calculate "gradients" and move 100x faster.
        weight = pm.math.sigmoid((index - tau) * 10) 
        mean = pm.Deterministic("mean", (1 - weight) * mu1 + weight * mu2)

        # 4. Likelihood
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