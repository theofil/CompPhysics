// for the random numbers: http://www.cplusplus.com/reference/cstdlib/rand/
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <math.h>       /* sqrt and more */ 

double U(double b, double a) {return (b - a)*((double) rand() / (RAND_MAX)) + a; }
double f(double x, double y, double z) {return (12/31.)*(x*x + y*z); }

int main ()
{
    /* initialize random seed: */
    srand (time(NULL)); // if you comment out this line, you take the same random sequence in all executions of the program (same random seed)

    // crude and hit-or-miss in one-go
    int N         = 1000;
    double sumf   = 0;
    double sumf2  = 0;
    int N0        = 0; // this for hit-or-miss
    for(int i = 0 ; i < N; ++i)
    {
	double x = U(0, 1);
        double y = U(1, 2);
        double z = U(1, 2);
        double u = U(0, f(1, 2, 2));   // lazy, better to store f(1, 2, 2) in another var e.g., fmax 
        
	sumf  += f(x, y, z);		
	sumf2 += f(x, y, z)*f(x, y, z); // lazy, implies twice function calls, but OK		
	if(u <= f(x, y, z)) N0++;  // this is for hit-or-miss
    }
 
    // --- crude ---
    double V1       = 1; // exact
    double meanf    = sumf/N;
    double sigmaf2  = sumf2/N - meanf*meanf; // =  <f**2> - <f>**2
    sigmaf2         = sigmaf2*(N/(N-1));     // correction for the sample variance https://en.wikipedia.org/wiki/Variance#Population_variance_and_sample_variance
    double I1       = V1*meanf;
    double dI1      = V1*sqrt(sigmaf2/N);
    printf("--- crude --- \n");
    printf("I1 = %2.4f +/- %2.4f \n", I1, dI1);
  

    // --- hit-or-miss ---
    double V2     = f(1, 2, 2); // volume of hit-or-miss
    double p      = double(N0)/N; 
    double I2     = V2*p;
    double dI2    = V2*sqrt( (p-p*p)/N );
    printf("--- hit-or-miss --- \n");
    printf("I2 = %2.4f +/- %2.4f \n", I2, dI2);

    return 0;
}
/*
outputs

--- crude --- 
I1 = 1.0005 +/- 0.0086 
--- hit-or-miss --- 
I2 = 1.0084 +/- 0.0306 

*/
