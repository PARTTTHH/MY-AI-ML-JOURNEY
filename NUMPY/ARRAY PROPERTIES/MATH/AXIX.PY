# AXIX IS A ATRIBUTES IT IS USED TO MANULPATE OPERATION IN 2D OR 
# MORE DIAMENTIONAL ARRAY TO CONTROL DRECTION OF OPERATION LETS SEE WITH EXAMPLE
        # USE IT LIKE  np.operation(arr_here, axis=1 / 0)
# WE HAVE TWO VALUES OF AxiS 1 OR 0
        # IF WE DOES axis=0 ITS MEANS OPERATION DIRECTION IS VERTICLE - COLUMN WISE
        # AND IF WE DOES axis=1 ITS MEANS OPERATION DIRECTION IS HORIZONTAL - ROW-WISE
        
import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8]])
col_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)
print(col_sum)
print(row_sum)