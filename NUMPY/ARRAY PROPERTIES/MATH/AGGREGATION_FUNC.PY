# AGGREGATION FUNCTION MEAN DATA SUMMERISE MEANS FOR EXAMPLE 
# WE CALCULATE SUM OF ARRAY, AVRAGE OF ARRAGE WE CAN CALCULATE THIS 
# DIRECLTY EVEN WITHOUT A LOOP LETS SEE SOME FUCTIONS BELOW
            # FUNCTIONS                WHAT IT DOES
        # np.sum(arr_here)          ADDS ALL ELEMENTS
        # np.mean(arr_here)         CALCULATES AVARAGE OF DATA OR ARRAY 
        # np.min(arr_here)          RETURNS SMALLEST VALUE 
        # np.max(arr_here)           RETURNS LARGETS VALUE 
        #  np.std(arr_here)         CALCULATES STANDARD DEVIATION
        #  np.var(arr_here)         CALCULATES VARIENCE
        
import numpy as np

arr = np.array([10, 20, 30, 40])

sum = np.sum(arr)
print(sum)

mean = np.mean(arr)
print(mean)

min = np.min(arr)
print(min)

max = np.max(arr)
print(max)

standard_deviation = np.std(arr)
print(standard_deviation)

variance = np.var(arr)
print(variance)