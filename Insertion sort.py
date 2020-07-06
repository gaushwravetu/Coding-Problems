def InsertionSort(seq):
    for sliceEnd in range(len(l)):
        pos = sliceEnd
        while(pos > 0 and seq[pos] < seq[pos-1]):
            (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
            pos = pos-1
        
