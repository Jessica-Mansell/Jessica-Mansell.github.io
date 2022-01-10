#creating for loop to return numbers 1-10
for num in range(1,11):
    print(num)

#creating for loop to return numbers 1-10 in reverse
for num in range(11, 0, -1):
  print(num)

#repeat 1-3 3x
for num in range(1, 4):
    for num in range(1, 4):
        print(num)

for x in range(1,4):
    for y in range(1,4):
        print("Iteration is", x, "and y is", y)

def bubbleSort(input):
    for i in range(len(input)):
        for j in range(len(input)-1):
            if input[j] > input[j + 1]:
                #swap (input, j, j+1)
                tmp = input[j]
                input[j] = input[j + 1]
                input[j + 1] = tmp
    return input

print(bubbleSort([6,4,8,4,6,4,1,1,6,5,1,6,5,4]))

def selectionSort(input):
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i] < input[j]:
                #swap (input, j, j+1)
                tmp = input[i]
                input[i] = input[j]
                input[j] = tmp
    return input

print(selectionSort([6,4,8,4,6,4,1,1,6,5,1,6,5,4]))
#return min element
class Solution:
    def __init__(self, input):
        self.input = input

    def find_min_element(self):
        smallest = None

        for elem in self.input:
            if(smallest == None or elem < smallest):
                smallest = elem
        return smallest

    def find_max_element(self):
        biggest = None

        for elem in self.input:
            if(biggest == None or elem > biggest):
                biggest = elem
        return biggest

my_solution = Solution(input = [3, 1, 2, 7, -1, 0])
smallest_item = my_solution.find_min_element()
biggest_item = my_solution.find_max_element()
print(smallest_item)
print(biggest_item)
