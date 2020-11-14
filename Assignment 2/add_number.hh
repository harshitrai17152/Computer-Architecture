#ifndef __LEARNING_GEM5_ADD_NUMBER_HH__
#define __LEARNING_GEM5_ADD_NUMBER_HH__

#include "params/AddNumber.hh"
#include "sim/sim_object.hh"

class AddNumber : public SimObject
{	
  private:
    void processEvent();
    EventFunctionWrapper event;

  public:
    AddNumber(AddNumberParams *p);
    void startup();

	static const int N = 4;       
	int A[N][N] = { { 5,-2, 2, 7}, 
                    { 1, 0, 0, 3}, 
                    {-3, 1, 5, 0}, 
                    { 3,-1,-9, 4} };        
                    
    void adjoint(int A[N][N],int adj[N][N]);
    void getCofactor(int A[N][N],int temp[N][N],int p,int q,int n); 
    int determinant(int A[N][N],int n);
    bool inverse(int A[N][N],float inverse[N][N]);	
};

#endif
