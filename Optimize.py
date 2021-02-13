
import math
from scipy.optimize import fmin_bfgs



def initial_S_star(X,S_star_inf,h2):
        
   return X + (S_star_inf-X)*(1.0 - math.exp(h2))
       
       
def solve(S_initial,X,h2):
    
   Objective = lambda S_star_inf:(S_initial - initial_S_star(X,S_star_inf,h2))**2
   return fmin_bfgs(Objective, 1, disp = False)[0]
