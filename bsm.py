

from scipy import stats, log, sqrt, exp
import datetime

# defining black scholes formula here with variables


def blackscholes_price(Spot, Strike, TimetoMaturity, riskFreeInterestRate, ImpliedVolatility):
    d1 = (log(Spot/Strike) + (riskFreeInterestRate+ImpliedVolatility *
                              ImpliedVolatility/2)*TimetoMaturity)/(ImpliedVolatility*sqrt(TimetoMaturity))
    d2 = d1 - ImpliedVolatility*sqrt(TimetoMaturity)

    price = Spot*stats.norm.cdf(d1) - Strike * \
        exp(-riskFreeInterestRate*TimetoMaturity)*stats.norm.cdf(d2)

    return price
