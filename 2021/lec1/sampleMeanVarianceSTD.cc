#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <math.h>       /* for the sqrt funcion */

int main ()
{
    float x [] = {3, 2, 4, 1, 2, 3, 4, 3, 4, 4};
    unsigned int N = sizeof(x)/sizeof(x[1]);  // N = 10, but in that way we can add/remove elements from x array and the code will still work

    float sumX  = 0;
    float sumX2 = 0;

    for(unsigned int i = 0 ; i < N; ++i)
    {
	float z= x[i];
        sumX  += z;
        sumX2 += z*z;
    }

    float meanX  = sumX/N;
    float sigma2 = sumX2/N - meanX*meanX;
    float sigma  = sqrt(sigma2);

    printf("N = %d   mean = %2.3f   sigma = %2.3f \n", N, meanX, sigma);

    return 0;
}

/*
outputs
N = 10   mean = 3.000   sigma = 1.000 
*/
