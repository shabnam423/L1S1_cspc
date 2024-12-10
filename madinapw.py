import time
import math

#function for the curve y = sqrt(1 - x^2)
def semicircle(x):
    return math.sqrt(1-x**2)
def trapezoidMethod(N):
    a=-1     #start of the interval
    b=1      #end of the interval
    h=(b-a)/N  #width of each trapezoid
    totalArea=0.5*(semicircle(a)+semicircle(b))
    for i in range(1,N):
        x=a+i*h
        totalArea+=semicircle(x)
    totalArea*=h
    #since it's a cemicircle, we multiply it by 2
    approxPi=2*totalArea
    return approxPi
#writing main function to test pi for diffent values of N and measure accuracy 
def main():
    values=[10, 100, 1000, 10000, 1000000]
    piTrue= math.pi  # actual value of Pi
    for N in values:
        startTime=time.time()
        approxPi= trapezoidMethod(N)
        computationTime=time.time()-startTime
        error=abs(piTrue-approxPi)
        print(f"N = {N}")
        print(f"Approximated Pi = {approxPi}")
        print(f"Error = {error}")
        print(f"Computation Time = {computationTime:.6f} seconds \n")
main()