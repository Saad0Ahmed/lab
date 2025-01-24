#bubble sort
def bubblesort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range (n-i-1):
            if arr [j] > arr [j+i]:
                arr [j], arr[j+i] = arr [j+i], arr[j]

#example usage
arr = [5,3,8,6,7,2]
print("original array: ", arr)
bubblesort(arr)
print("sorted array: ", arr)

#selection sort
def selection(arr1):
    n = len(arr1)
    for i in range (n-1):
        mini = i
        for j in range (n-i-1):
            if arr1 [j] < arr1 [mini]:
                arr1 [i], arr[mini] = arr1 [mini], arr[i]

#example usage
arr1 = [5,3,8,6,7,2]
print("original array: ", arr1)
selection(arr1)
print("sorted array: ", arr1)

#matplotlib
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(start=1, stop=50, num=50)
bestcase = n
averagecase = n**2  # Use ** for exponentiation
worstcase = n**2    # Use ** for exponentiation
plt.figure(figsize=(10, 6))
plt.plot(n, bestcase, label="Best Case: O(n)", color="green", linewidth=2)
plt.plot(n, averagecase, label="Average Case: O(n^2)", color="blue", linewidth=2)
plt.plot(n, worstcase, label="Worst Case: O(n^2)", color="red", linewidth=2, linestyle=":")
plt.title("Asymptotic Notations for BubbleSort", fontsize=18)
plt.xlabel("Input Size (n)", fontsize=12)  # Corrected syntax
plt.ylabel("Time Complexity", fontsize=12)  # Corrected syntax
plt.legend()
plt.show()