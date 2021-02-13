
import math
from  Optimize import solve
import bsm
from scipy import stats,log
class BaroneAdesiWhaley:
    
    def __init__(self,S,X,sigma_sqr,time_sqrt,b,r,nn,m,K,q2):
        
        self.S = S
        self.X = X
        self.sigma_sqr = sigma_sqr
        self.sigma = self.sigma_sqr**2
        self.time_sqrt = time_sqrt
        self.time = self.time_sqrt**2
        self.b = b
        self.r = r
        self.nn = nn
        self.m = m
        self.K = K
        self.q2 = q2
        self.q2_inf = 0.5 * ( (-self.nn-1.0) + math.sqrt(math.pow((self.nn-1),2.0)+4.0*self.m));
        self.S_star_inf = self.X / (1.0 - 1.0/self.q2_inf);
        self.h2 = -(self.b*self.time+2.0*self.sigma*self.time_sqrt)*(self.X/(self.S_star_inf-self.X));
        self.q2_inf = 0.5 * ( (-self.nn-1.0) + math.sqrt(math.pow((self.nn-1),2.0)+4.0*self.m));
        
   
    def approximate_value(self):
       
        euro_call = bsm.blackscholes_price(self.S,self.X,self.time,self.r, self.sigma)
        S_initial = self.X + (self.S_star_inf-self.X)*(1.0 - math.exp(self.h2))
        #self.opt = optimize()
        #self.opt.set_parameters(self.X,self.S_star_inf,self.h2)
        S_star= solve(S_initial,self.X,self.h2)
        if (self.S>=S_star):
	         C=self.S - self.X

        else:
	         d1 = (log(S_star/self.X)+(self.b+0.5*self.sigma_sqr)*self.time)/(self.sigma*self.time_sqrt)
	         A2 =  (1.0-math.exp((self.b-self.r)*self.time))*stats.norm.cdf(d1)* (S_star/self.q2)
	         C = euro_call+A2*math.pow((self.S/S_star),self.q2)

        return max(C,euro_call) 
   

    
        
def create_model(S,X,r,b,sigma,time):
    '''
    Instantiates an instance of the class BaroneAdesiWhaley

            Parameters:
                    S (float):       Initial stock price
                    X (float):       Strike price
                    r (float):       risk-free-rate
                    b (float):       dividen yield
                    sigma (float) :  volatility
                    time (float) :   time to maturity in years
           
    '''
    
    sigma_sqr = sigma*sigma
    time_sqrt = math.sqrt(time)
    nn = 2.0*b/sigma_sqr 
    m = 2.0*r/sigma_sqr 
    K = 1.0-math.exp(-r*time)
    q2 = (-(nn-1)+math.sqrt(math.pow((nn-1),2.0)+(4*m/K)))*0.5
     
    return BaroneAdesiWhaley(S,X,sigma_sqr,time_sqrt,b,r,nn,m,K,q2)



mdl = create_model(40,30,0.01,0.02,0.30,1.0)

mdl.approximate_value()
