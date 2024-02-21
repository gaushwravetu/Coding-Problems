package leetCodeInterview150;
import java.util.*;
import java.io.*;
public class RemoveElements {
	
	public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int index = 0;
        for(int i=0;i<n;i++){
            if(nums[i]!=val){
                nums[index]=nums[i];
                index++;
            }
        }
        return index;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.printf("Enter size of array : ");
		int n = sc.nextInt();
		int[] nums = new int[n];
		for(int i=0; i<n; i++)  
		{  
	   
			nums[i]=sc.nextInt();  
		}
		System.out.printf("Enter value to be removed : ");
		int val = sc.nextInt();
		 
		
		RemoveElements RE = new RemoveElements();
		int k = RE.removeElement(nums,val);
		System.out.printf("Your Unique array have : " + k +  " elements");

	}

}
