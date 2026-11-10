# Author: Ilaria Teberneac
# File name: bucketsort.py
# This program defines a Bucket Sort function
# and compares the time needed to sort a list with Bucket Sort and Quick Sort

import random
import copy
from sorts import quickSort
import time

def bucketSort(lyst):
    
    max_num = max(lyst)
    total_buckets = max_num + 1
    simple_lyst = []
    for simple in range(total_buckets):
        simple_lyst.append([])
    
    for number in lyst:
        test = simple_lyst[number].append(number)

    single_lyst = []
    
    for simple2 in simple_lyst:
        single_lyst += simple2

    #return single_lyst

    lyst[:] = single_lyst
    
             
def randints(other):

    rand_lyst = []
    for numbers in range(other):
        rand_lyst.append(random.randint(0, other))
    return rand_lyst
    

if __name__== '__main__':

     testlyst = [4, 2, 1, 3, 3, 11, 25, 26, 26, 27, 17, 17, 49, 50]
     bucketSort(testlyst)
     print("Expected [1, 2, 3, 3, 4, 11, 17, 17, 25, 26, 26, 27, 49, 50]: ", testlyst)

     print()
     testlyst = [0,0, 10, 1, 1]
     bucketSort(testlyst)
     print("Expected [0, 0, 1, 1, 10]: ", testlyst)

     print()
     testlyst = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
     bucketSort(testlyst)
     print("Expected [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: ", testlyst)

     print()
     print("Expect 10 randomn numbers:", randints(10))

     print()
     testlyst = randints(20)
     bucketSort(testlyst)
     print("Expected bucket-sorted 20 randomn numbers:", testlyst)

     print()
     testlyst = randints(35)
     bucketSort(testlyst)
     print("Expected bucket-sorted 35 randomn numbers:", testlyst)

     print("\n\n")


     for number in range(1000, 10000, 500):
         values = randints(number)
         compare_list = copy.copy(values)

         start = time.time()
         bucketSort(compare_list)
         finish = time.time()
         final_time = finish - start

         print("Total time for bucket sort for:", number, "is", final_time)
         
         start = time.time()
         quickSort(values)
         finish = time.time()
         final_time = finish - start
         print("Total time for qs for:", number, "is", final_time)
         print()

     
     
     

     

