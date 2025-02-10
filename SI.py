#matplotlib selection and insertion
import matplotlib.pyplot as plt
input_sizes = [10,20,50,100,200,500,1000]
quadratic_times = [n**2 for n in input_sizes]
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, quadratic_times, marker = 'o', label = '0(n*n)_ quadratic time complexity')
plt.title("Asymptotic Notations for Selection and Insertion", fontsize=18)
plt.xlabel("Input Size (n)", fontsize=12)  # Corrected syntax
plt.ylabel('Number of operations (n*n)', fontsize=12)  # Corrected syntax
plt.grid (True)
plt.show()
