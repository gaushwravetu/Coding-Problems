def calculate_no_ways(receiving_data,temp):
       
    if receiving_data<temp:
        return 0
    elif matrix_list[receiving_data][temp]!=-1:
        return matrix_list[receiving_data][temp] 
    elif temp==receiving_data:
        return 1
    else:
        matrix_list[receiving_data][temp] = calculate_no_ways(receiving_data,temp+1)
        matrix_list[receiving_data][temp]+=calculate_no_ways(receiving_data,temp+2)
        matrix_list[receiving_data][temp]+=calculate_no_ways(receiving_data,temp+3)
        return matrix_list[receiving_data][temp]

matrix_list = []
j = 0
while j<250:
    matrix_list.append([-1]*250)
    j+=1

    
i = 0
t = int(input())
# def my_matrix(N):
#     matrix_list = []
#     matrix_list[[-1]*N]*N
#     return 
# matrix_list = my_matrix(250)
while i<t:
    my_input = int(input())
    sending_data = my_input+2
    result = calculate_no_ways(sending_data,1)
    print(result)
    i+=1