/*
Lecture's 1 example with C/C++ and graphics libraries from ROOT

-- not for pedestrians 

Under Linux compile this puppy with

  g++ sampleMeanVarianceSTD_withGraphics.cc -o sampleMeanVarianceSTD_withGraphics.cc.exec `root-config --glibs --cflags`

Then run the executable with

  ./sampleMeanVarianceSTD_withGraphics.cc.exec

If you have troubles with compilation and linking, don't write to me but instead check the ROOT docs and FAQs
*/
#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <iomanip>
#include <stdlib.h>
#include <sys/types.h>
#include <dirent.h>

#include "TFile.h"    // ROOT libraries
#include "TH1F.h"
#include "TCanvas.h"

#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <math.h>       /* for the sqrt funcion */


 
int main ()
{
    float x [] = {3, 2, 4, 1, 2, 3, 4, 3, 4, 4};
    unsigned int N = sizeof(x)/sizeof(x[1]);  // N = 10, but in that way we can add/remove elements from x array and the code will still work

    float sumX  = 0;
    float sumX2 = 0;

    TH1F * h1 = new TH1F("h1",";x;entries",8,0,8); // [0,8) in 8 bins
    
    for(unsigned int i = 0 ; i < N; ++i)
    {
	float z= x[i];
        sumX  += z;
        sumX2 += z*z;
        h1->Fill(z);  
    }

    float meanX  = sumX/N;
    float sigma2 = sumX2/N - meanX*meanX;
    float sigma  = sqrt(sigma2);

    printf("N = %d   mean = %2.3f   sigma = %2.3f \n", N, meanX, sigma);

    TCanvas c1;
    c1.cd();
     
    h1->Draw();
    c1.SaveAs("output.png");
     
    return 0;
}

/*
outputs
N = 10   mean = 3.000   sigma = 1.000 
output.png
*/
