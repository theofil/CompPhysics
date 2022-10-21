// example of C code on how to generate uniformly distributed randoms in [0,1) using stdlib and time
#include <time.h>
#include <stdlib.h>
#include<stdio.h>

int main()
{
    srand(time(NULL));   // Initialization, should only be called once.


    for (int i = 0; i<20; ++i)
    {
        int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
	printf("r = %d   r/RAND_MAX = %2.3f \n", r, float(r)/RAND_MAX);
    }
   

    return 0;
}
// --- printout
//r = 770611717   r/RAND_MAX = 0.359 
//r = 197252562   r/RAND_MAX = 0.092 
//r = 1656542213   r/RAND_MAX = 0.771 
//r = 1526974183   r/RAND_MAX = 0.711 
//r = 1425512031   r/RAND_MAX = 0.664 
//r = 1253139085   r/RAND_MAX = 0.584 
//r = 1136475466   r/RAND_MAX = 0.529 
//r = 1023600644   r/RAND_MAX = 0.477 
//r = 164527591   r/RAND_MAX = 0.077 
//r = 1403768248   r/RAND_MAX = 0.654 
//r = 877598194   r/RAND_MAX = 0.409 
//r = 875158962   r/RAND_MAX = 0.408 
//r = 681176031   r/RAND_MAX = 0.317 
//r = 290230860   r/RAND_MAX = 0.135 
//r = 974701683   r/RAND_MAX = 0.454 
//r = 805926865   r/RAND_MAX = 0.375 
//r = 1033458426   r/RAND_MAX = 0.481 
//r = 488028846   r/RAND_MAX = 0.227 
//r = 1060766829   r/RAND_MAX = 0.494 
//r = 2046341256   r/RAND_MAX = 0.953 
