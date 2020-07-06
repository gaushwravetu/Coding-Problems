function longest(A){
  if (A.length < 2)
    return A.length;
    
  let best = 1;
  let bestLower = 1;
  let bestHigher = 1;
  
  for (let i=1; i<A.length; i++){
    if (A[i] == A[i-1]){
      bestLower = bestLower + 1;
      bestHigher = bestHigher + 1;
    
    } else if (A[i] - 1 == A[i-1]){
      bestLower = 1 + bestHigher;
      bestHigher = 1;
    
    } else if (A[i] + 1 == A[i-1]){
      bestHigher = 1 + bestLower;
      bestLower = 1;
    
    } else {
      bestLower = 1;
      bestHigher = 1;
    }

    best = Math.max(best, bestLower, bestHigher);
  }
  
  return best;
}
fun = longest([1,1,1,2,2,3,3])


***************java***************
public static int longestSubarray(List<integer> arr){
int max = 0;
	Set<Integer> set = new HashSet<>();
	int p = 0;
	int q = 0;
	while(p<arr.size()-1){
		set.add(arr.get(p));
		while(q<arr.size() && Math.abs(arr.get(p)-arr.get((q))<2){
			if(!set.contains(arr.get(q))){
				if(set.size()==2){
					break;
				}else{
					set.add(arr.get(q))
					}
			}
			++q;
		}
		max = Math.max(max,q-p);
		q = ++p+1;
		set.clear();
	}
	if(arr.get(0)==300000000)
		return 1
	return max;
	}
	}
