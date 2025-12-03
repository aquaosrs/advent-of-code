def load_input():
    # get current file path
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().strip().split("\n")
    return lines

def get_lists():
    input_lines = load_input()
    list1 = []
    list2 = []
    for line in input_lines:
        parts = line.split()
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
    return list1, list2


if __name__ == "__main__":
    list1, list2 = get_lists()
    
    #list1.sort()
    list2.sort()

    print("List 1:", list1)
    print("List 2:", list2)

    result = 0

    for i in range(len(list1)):
        countInList2 = list2.count(list1[i])
        result += (countInList2 * list1[i])
    
    print ("Final Result:", result)