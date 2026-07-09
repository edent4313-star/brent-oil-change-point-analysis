import pymc as pm
import numpy as np



def build_change_point_model(series):

    try:

        if len(series)==0:

            raise ValueError(
                "Empty price series"
            )


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
                chains=2,
                cores=1,
                target_accept=0.90,
                return_inferencedata=True
            )


        return trace


    except Exception as e:

        raise RuntimeError(
            f"MCMC sampling failed: {e}"
        )