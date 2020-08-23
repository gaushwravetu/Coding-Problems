#include <bits/stdc++.h>
using namespace std;

 char sud[7][7];
 set<int> a;
 set<int>b;
 set<int> c;
 set<int> d;
 set<int>e;
 set<int>f;
 set<int>h;

bool possible(int grid[][7],int i, int j , int k)

{
      for(int p=0;p<7;p++)
      {
          if(grid[i][p]==k)  // same row
          {
              return false;
          }
          if(grid[p][j]==k)  // same column
          return false;
      }
      
      
       
                if(i<7 and  j<7 and sud[i][j]=='a')
                {
                    if(a.find(k)!=a.end())
                    return false;
                }
                if(i<7 and  j<7 and sud[i][j]=='b')
                {
                    if(b.find(k)!=b.end())
                    return false;
                }
                if(i<7 and j<7 and sud[i][j]=='c')
                {
                    if(c.find(k)!=c.end())
                    return false;
                }
                if(i<7 and  j<7 and sud[i][j]=='d')
                {
                    if(d.find(k)!=d.end())
                    return false;
                }
                if(i<7 and  j<7 and sud[i][j]=='e')
                {
                   if(e.find(k)!=e.end())
                    return false;
                }
                if(i<7 and  j<7 and sud[i][j]=='f')
                {
                    if(f.find(k)!=f.end())
                    return false;
                }
                
                if(i<7 and  j<7 and sud[i][j]=='h')
                {
                    if(h.find(k)!=h.end())
                    return false;
                }
       
       
       return true;
       
      
}
bool suduko(int grid[][7],int i, int j)
{
    
    
    
    if(i==6 and  j==7)
    {
        return true;
    }
    
    
    if(j==7  and  i<6)
    {
        i++;
        j=0;
    }
    //cout<<i<<" "<<j<<endl;
    if(grid[i][j]!=0):
    {
        suduko(grid,i,j+1);
    }
    else:
    {
        for k in range(1,8):
        {//cout<<i<<" "<<j<<" "<<k<<endl;
            if(i<7 and  j<7 and possible(grid,i,j,k))
            {
                grid[i][j]=k;
                 if(i<7 and  j<7 and sud[i][j]=='a')
                {
                    a.insert(k);
                }
               else if(i<7 and  j<7 and sud[i][j]=='b')
                {
                    b.insert(k);
                }
                else if(i<7 and  j<7 and sud[i][j]=='c')
                {
                    c.insert(k);
                }
                else if(i<7 and  j<7 and sud[i][j]=='d')
                {
                    d.insert(k);
                }
                else if(i<7 and  j<7 and sud[i][j]=='e')
                {
                    e.insert(k);
                }
               else if(i<7 and  j<7 and sud[i][j]=='f')
                {
                    f.insert(k);
                }
                
               else  if(i<7 and  j<7 and sud[i][j]=='h')
                {
                    h.insert(k);
                }
                
                 if(i<7 and  j<7 and suduko(grid,i,j+1))
                {
                    return true;
                }
            }
            
            grid[i][j]=0;
            
            if(i<7 and  j<7 and sud[i][j]=='a' and a.find(k)!=a.end() )
                {
                    a.erase(a.find(k));
                }
              else  if(i<7 and  j<7 and sud[i][j]=='b' and b.find(k)!=b.end())
                {
                    b.erase(b.find(k));
                }
              else  if(i<7 and  j<7 and sud[i][j]=='c' and c.find(k)!=c.end())
                {
                    c.erase(c.find(k));
                }
               else if(i<7 and  j<7 and sud[i][j]=='d' and d.find(k)!=d.end())
                {
                    d.erase(d.find(k));
                }
               else if(i<7 and  j<7 and sud[i][j]=='e' and e.find(k)!=e.end())
                {
                   e.erase(e.find(k));
                }
               else if(i<7 and  j<7 and sud[i][j]=='f' and f.find(k)!=f.end())
                {
                   f.erase(f.find(k));
                }
                
               else if(i<7 and  j<7 and sud[i][j]=='h' and h.find(k)!=h.end())
                {
                    h.erase(h.find(k));
                }
            
        }
        
        return false;
    }
    
}

int main() {
    int grid[7][7];
    for(int i=0;i<7;i++)
    {
        
        for(int j=0;j<7;j++)
        {
           cin>>grid[i][j];
        }
    }
    
    char pr[7];
    set<char> check;
    int k=0;
    for(int i=0;i<7;i++)
    {
        
        for(int j=0;j<7;j++)
        {
           cin>>sud[i][j];
           if(check.find(sud[i][j])==check.end())
           {
               //cout<<sud[i][j]<<" ";
               pr[k]=sud[i][j];
               check.insert(sud[i][j]);
               k++;
               
           }
        }
    }
    
    
    for( k=0;k<7;k++)
    {
        char ch='a'+k;
    for(int i=0;i<7;i++)
    {
        
        for(int j=0;j<7;j++)
        {
           
           if(sud[i][j]==pr[k])
           {
               sud[i][j]=ch;
           }
        }
    }
        
    }
  
   
    
    for(int i=0;i<7;i++)
    {
        for(int j=0;j<7;j++)
        {
            if(grid[i][j]!=0)
            {
                if(sud[i][j]=='a')
                {
                    a.insert(grid[i][j]);
                }
                if(sud[i][j]=='b')
                {
                    b.insert(grid[i][j]);
                }
                if(sud[i][j]=='c')
                {
                    c.insert(grid[i][j]);
                }
                if(sud[i][j]=='d')
                {
                    d.insert(grid[i][j]);
                }
                if(sud[i][j]=='e')
                {
                    e.insert(grid[i][j]);
                }
                if(sud[i][j]=='f')
                {
                    f.insert(grid[i][j]);
                }
                
                if(sud[i][j]=='h')
                {
                    h.insert(grid[i][j]);
                }
            }
        }
    }
    
    
    if(suduko(grid,0,0))
    {
        //cout<<"upto this"<<endl;
        for(int i=0;i<7;i++)
        {
            for(int j=0;j<7;j++)
            {
                cout<<grid[i][j]<<" ";
                //cout<<sud[i][j]<<" ";
            }
            cout<<endl;
        }
        
    }
    
    
	return 0;
}
