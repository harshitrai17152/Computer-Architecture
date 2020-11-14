#include "learning_gem5/add_number.hh"
#include "debug/MATRIX.hh"
#include "debug/RESULT.hh"
#include <iostream>

AddNumber::AddNumber(AddNumberParams *params) :
    SimObject(params), event([this]{processEvent();},name())

{
    std::cout << "Finding Inverse of the given matrix" << std::endl;
}

void
AddNumber::processEvent()
{
  	int adj[N][N];                 
    float inv[N][N];      

  	adjoint(A,adj);
  	bool ans=inverse(A,inv);
  		
  	std::cout<<"\n";    
  	if(DTRACE(MATRIX))
  	{
		std::cout<<"Size Of Matrix is: "<<N;    
	  	std::cout<<"\n";    
	  	std::cout<<"Input Matrix is as follows:\n";    
	  	for(int i=0;i<N;i++) 
  		{
			for(int j=0;j<N;j++) 
    	    	std::cout<<A[i][j]<<"  ";
    	    std::cout<<"\n";    
  		}
  	}
  	  
  	std::cout<<"\n";    
  	if(DTRACE(RESULT))
  	{
		if(ans)
		{ 	
		  	std::cout<<"Inverse of Matrix is as follows:\n";    
		  	for(int i=0;i<N;i++) 
  			{
				for(int j=0;j<N;j++) 
    		    	std::cout<<inv[i][j]<<"  ";
    		    std::cout<<"\n";    
  			}
  		}
  		else
  			std::cout<<"Inverse does not exist\n";    
  	}
  	std::cout<<"\n";    
}

void
AddNumber::adjoint(int A[N][N],int adj[N][N]) 
{
	if(N==1) 
    { 
       	adj[0][0]=1; 
        return; 
    } 
    
    int temp[4][4];
    int sign=1;
    for(int i=0;i<N;i++) 
    { 
        for(int j=0;j<N;j++) 
        { 
            getCofactor(A,temp,i,j,N); 
            sign=((i+j)%2==0)?1:-1;
            adj[j][i]=(sign)*(determinant(temp,N-1)); 
        } 
    } 
    
}

int
AddNumber::determinant(int A[N][N],int n)
{
	int D=0;

    if(n==1) 
    	return(A[0][0]); 

    int temp[4][4];
    int sign=1;    
    for(int f=0;f<n;f++) 
    { 
        getCofactor(A,temp,0,f,n); 
        D+=sign*A[0][f]*determinant(temp,n-1); 
        sign=-sign; 
    } 
  
    return(D);
}

void
AddNumber::getCofactor(int A[N][N],int temp[N][N],int p,int q,int n) 
{
	int i=0,j=0; 

    for(int row=0;row<n;row++) 
    { 
        for (int col=0;col<n;col++) 
        { 
            if(row!=p && col!=q) 
            { 
                temp[i][j++]=A[row][col];
                if(j==n-1) 
                { 
                    j=0; 
                    i++; 
                } 
            } 
        } 
    }
}

bool
AddNumber::inverse(int A[N][N],float inverse[N][N]) 
{ 
	int adj[N][N];                     
    int det=determinant(A,N); 
    if(det==0) 
    	return(false);     	

    adjoint(A,adj); 
    for(int i=0;i<N;i++) 
    {
    	for(int j=0;j<N;j++) 
	    	inverse[i][j]=adj[i][j]/float(det); 
    }
  
    return(true); 
} 

void
AddNumber::startup()
{
    schedule(event,100);
}

AddNumber*
AddNumberParams::create()
{
    return new AddNumber(this);
}
