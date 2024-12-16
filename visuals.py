import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import time

class Visuals:
    def __init__(self, algorithm):
        self.algorithm = algorithm  # Associate an Algorithm instance

    def clear_console(self):
        """Clears the console for the next frame."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_array(self, data, highlight=None):
        """Prints the array with optional highlighting."""
        for i, val in enumerate(data):
            if highlight and i in highlight:
                print(f"\033[91m{val:3}\033[0m", end="  ")  # red color for highlighting
            else:
                print(f"{val:3}", end="  ")  # aligning the numbers neatly
        print("\n")

    def bubble_sort_visual(self, data):
        """Console visualizer for Bubble Sort."""
        n = len(data)
        for i in range(n):
            for j in range(n - 1 - i):
                # self.clear_console()
                self.print_array(data)
                self.print_array(data, highlight=(j, j + 1))  # Highlight compared elements
                if data[j] > data[j + 1]:
                    # Swap if needed
                    data[j], data[j + 1] = data[j + 1], data[j]
                time.sleep(1.5)  # Add delay for animation
        # self.clear_console()
        self.print_array(data)  # Final sorted array

    def quick_sort_visual(self, data, level=0):
        """
        Console visualizer for Quick Sort with detailed left and right halves.
        """
        if len(data) <= 1:
            return data  # Base case for recursion

        indent = "   " * level  # Indentation for visualization at different recursion levels

        # Highlight the pivot element
        pivot_index = len(data) // 2
        pivot = data[pivot_index]

        # self.clear_console()
        print()
        print(f"{indent}Current Array: {data}")
        print(f"{indent}Pivot: \033[91m{pivot}\033[0m")  # Highlight pivot in red
        time.sleep(5)  # Pause to highlight the pivot

        # Partition into left, middle, and right
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        # Display the partitioned arrays
        # self.clear_console()
        # print(f"{indent}Current Array: {data}")
        # print(f"{indent}Pivot: \033[91m{pivot}\033[0m")
        print()
        print(f"{indent}Left: {left}")
        print(f"{indent}Middle: {middle}")
        print(f"{indent}Right: {right}")
        time.sleep(5)  # Pause to highlight the partitioning

        # Recursively sort the left and right halves
        sorted_left = self.quick_sort_visual(left, level + 1)
        sorted_right = self.quick_sort_visual(right, level + 1)

        # Combine the sorted parts
        sorted_data = sorted_left + middle + sorted_right

        # Display the merged sorted array
        # self.clear_console()
        print()
        print(f"{indent}Merged: {sorted_data}")
        time.sleep(5)  # Pause to show the merged state

        return sorted_data
    
    def merge_sort_visual(self, data): #TODO
        pass


    def heap_sort_visual(self, data): #TODO
        pass

    def selection_sort_visual(self, data): #TODO
        pass

    def insertion_sort_visual(self, data): #TODO
        pass
    

    






    