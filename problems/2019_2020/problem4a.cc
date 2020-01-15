// for the random number: http://www.cplusplus.com/reference/cstdlib/rand/
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <math.h>       /* sqrt and more */ 

double U(double b, double a) {return (b - a)*((double) rand() / (RAND_MAX)) + a; }
double f(double x, double y) {return (20/13.)*(x + y); }

int main ()
{
    /* initialize random seed: */
    srand (time(NULL)); // if you comment out this line, you take the same random sequence in all executions of the program (same random seed)

    // crude and hit-or-miss in one-go
    int N         = 1000;
    double sumf   = 0;
    double sumf2  = 0;
    int M         = 0;
    int N0        = 0; // this for hit-or-miss
    for(int i = 0 ; i < N; ++i)
    {
	double x = U(0, 1);
        double y = U(0, 1);
        double u = U(0, f(1,1));   // lazy, better to store f(1,1) in another var e.g., fmax 
        if(x*x <= y) 
	{
	    sumf  += f(x, y);		
	    sumf2 += f(x, y)*f(x,y); // lazy, implies twice function calls, but OK		
            M     += 1;
            if(u <= f(x,y)) N0++;  // this is for hit-or-miss
	}
    }
 
    // --- crude ---
    double V1       = 2/3.; // exact
    double meanf    = sumf/M;
    double sigmaf2  = sumf2/M - meanf*meanf; // =  <f**2> - <f>**2
    sigmaf2         = sigmaf2*(M/(M-1));  // correction for the sample variance https://en.wikipedia.org/wiki/Variance#Population_variance_and_sample_variance
    double I1       = V1*meanf;
    double dI1      = V1*sqrt(sigmaf2/M);
    printf("--- crude --- \n");
    printf("I1 = %2.4f +/- %2.4f \n", I1, dI1);
  

    // --- hit-or-miss ---
    double V2     = (1 - 0)*(1 - 0)*(f(1,1) - 0); // volume of hit-or-miss
    double p      = double(N0)/N; 
    double I2     = V2*p;
    double dI2    = V2*sqrt( (p-p*p)/N);
    printf("--- hit-or-miss --- \n");
    printf("I2 = %2.4f +/- %2.4f \n", I2, dI2);

    return 0;
}
/*
outputs

--- crude --- 
I1 = 1.0094 +/- 0.0167 
--- hit-or-miss --- 
I2 = 0.9754 +/- 0.0453 

*/
