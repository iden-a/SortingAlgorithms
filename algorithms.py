import time
import random 

class Algorithm:
    def __init__(self, size):
        self.data = [random.randint(1, 100) for _ in range(size)]
        self.size = size

    def merge_sort_helper(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
    
        mid = len(data) // 2
    
        left = self.merge_sort(data[mid:])
        right = self.merge_sort(data[:mid])
        return self.merge_sort_helper(left, right)


    def quick_sort(self, data):
        if len(data) <= 1:
            return data
        
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1

            while j >= 0 and key < data[i]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key

        return data

    def bubble_sort(self, data):
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:  
                break
        return data
    
    def heap_sort(self, data): #TODO
        pass

    def selection_sort(self, data): #TODO
        pass

    def time_algorithm(self, algorithm, data):
        # dynamically get the sorting method by its name
        sort_method = getattr(self, algorithm, None)
        if not callable(sort_method):
            raise ValueError(f"The algorithm '{algorithm}' is not implemented.")
        
        start_time = time.time()
        sort_method(data.copy())
        end_time = time.time()
        return end_time - start_time


