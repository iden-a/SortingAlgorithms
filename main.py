from algorithms import Algorithm
from visuals import Visuals

def main():
    print("\nSorting Algorithms Visualizer & Time Complexity Analyzer")
    print("\nAlgorithms To Choose From")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Heap Sort")
    print("4. Bubble Sort")
    print("5. Selection Sort")
    print("6. Insertion Sort")

    algorithms_to_num = {
        1 : "merge_sort",
        2 : "quick_sort",
        3 : "heap_sort",
        4 : "bubble_sort",
        5 : "selection_sort",
        6 : "insertion_sort"
    }

    size = int(input("\nEnter The Data Size (1-10): "))

    while size > 10:
        print("Number Must Be In The Range 1 - 10!")
        size = int(input("Enter A Number (1-10): "))
    else:
        user_choice = int(input("Select An Algorithm To Visualize: "))
        if user_choice == 1:
            print("\nYou've Selected The Merge Sorting Algorithm!")
            algorithm = Algorithm(size)
            visuals = Visuals(algorithm)
            # visuals.merge_sort_visual(algorithm.data) #Show sorting visualization
        elif user_choice == 2:
            algorithm = Algorithm(size)
            visuals = Visuals(algorithm)
            visuals.quick_sort_visual(algorithm.data) #Show sorting visualization
        elif user_choice == 3:
            algorithm = Algorithm(size)
            visuals = Visuals(algorithm)
            # visuals.heap_sort_visual(algorithm.data) #Show sorting visualization
        elif user_choice == 4:
            print("\nYou've Selected The Bubble Sorting Algorithm!")
            print()
            algorithm = Algorithm(size)
            visuals = Visuals(algorithm)
            visuals.bubble_sort_visual(algorithm.data) #Show sorting visualization
        elif user_choice == 5:
            print("\nYou've Selected The Selection Sorting Algorithm!")
            algorithm = Algorithm(size)
            visuals = Visuals(algorithm)
            # visuals.selection_sort_visual(algorithm.data) #Show sorting visualization
        elif user_choice == 6:
            algorithm = Algorithm(size)
            visuals = Visuals(algorithm)
            # visuals.insertion_sort_visual(algorithm.data) #Show sorting visualization
        else:
            print("Could Not Find, Try Again!")

        calc_complexity = input("\nWould you like to calculate the time complexity of the algorithm? (y/n): ").lower()
        if calc_complexity == 'y':
            algorithm = Algorithm(size)
            algorithm_name = algorithms_to_num[user_choice]
            algorithm.time_algorithm(algorithm_name, algorithm.data)
            time_taken = algorithm.time_algorithm(algorithm_name, algorithm.data)
            print(f"Time Taken By The `{algorithm_name}` Algorithm: {time_taken:.6f} seconds")
            print()
        else:
            print("Exiting Program!")

if __name__ == "__main__":
    main()