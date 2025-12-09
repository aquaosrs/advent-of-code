from utils import load_input

class Circuit: 
    def __init__(self, junction_boxes):
        self.junction_boxes = junction_boxes

    def add_junction_box(self, junction_box):
        if junction_box not in self.junction_boxes:
            self.junction_boxes.append(junction_box)

    def contains(self, junction_box):
        return junction_box in self.junction_boxes
    
    def length(self):
        return len(self.junction_boxes)
    
    def combine(self, other_circuit):
        for box in other_circuit.junction_boxes:
            self.add_junction_box(box)

    def __str__(self):
        return f"Circuit with {len(self.junction_boxes)} junction boxes"

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Junction Box at x:{self.x}, y:{self.y}, z:{self.z}"
    

    def distance_to(self, other_box):
        return ((self.x - other_box.x) ** 2 + 
                (self.y - other_box.y) ** 2 + 
                (self.z - other_box.z) ** 2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

def parse_input():
    input_data = load_input()
    junction_boxes = []
    for line in input_data:
        x, y, z = map(int, line.split(","))
        junction_boxes.append(JunctionBox(x, y, z))
    return junction_boxes

def find2ClosestBoxes(junction_boxes: list[JunctionBox], min_acceptable_distance: float):
    closest_pair = None
    min_distance = float('inf')
        
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            box1 = junction_boxes[i]
            box2 = junction_boxes[j]
            distance = box1.distance_to(box2)
            
            if distance < min_distance and distance > min_acceptable_distance:
                min_distance = distance
                closest_pair = (box1, box2)
    
    return closest_pair

def find_closest_boxes_between_circuits(circuits: list[Circuit]):
    """Find the closest pair of boxes where each box is in a different circuit."""
    closest_pair = None
    min_distance = float('inf')
    
    for i in range(len(circuits)):
        for j in range(i + 1, len(circuits)):
            circuit1 = circuits[i]
            circuit2 = circuits[j]
            
            for box1 in circuit1.junction_boxes:
                for box2 in circuit2.junction_boxes:
                    distance = box1.distance_to(box2)
                    if distance < min_distance:
                        min_distance = distance
                        closest_pair = (box1, box2)
    
    return closest_pair
    
def totalConnections(circuits: list[Circuit]) -> int:
    total = 0
    for circuit in circuits:
        n = len(circuit.junction_boxes)
        print (f"Circuit with {n} boxes contributes {n - 1} connections")
        total += (n - 1)
    return total

if __name__ == "__main__":
    min_distance = 0.0
    junction_boxes = parse_input()
    print(f"Total junction boxes to process: {len(junction_boxes)}")
    circuits: list[Circuit] = []

    # Start by putting each box in its own circuit
    for box in junction_boxes:
        new_circuit = Circuit([box])
        circuits.append(new_circuit)

    index = 0

    while len(circuits) > 1:
        print (f"Starting iteration {index}, current number of circuits: {len(circuits)}")
        index += 1
        if index % 100 == 0:
            print(f"Iteration {index}, current number of circuits: {len(circuits)}")
        
        try:
            closest_boxes = find2ClosestBoxes(junction_boxes, min_distance)
            
            if closest_boxes is None:
                # No more pairs found with current min_distance
                # Need to connect separate circuits - find closest boxes between different circuits
                print(f"No more pairs found, connecting circuits... Current circuits: {len(circuits)}")
                closest_boxes = find_closest_boxes_between_circuits(circuits)
                if closest_boxes is None:
                    # This shouldn't happen, but if it does, break
                    print("ERROR: No pairs found between circuits")
                    break
                min_distance = 0.0  # Reset min_distance for next iteration
            else:
                min_distance = closest_boxes[0].distance_to(closest_boxes[1])

            closest_boxes_circuits = [circuit for circuit in circuits if circuit.contains(closest_boxes[0]) or circuit.contains(closest_boxes[1])]
            if len(closest_boxes_circuits) == 2:
                closest_boxes_circuits[0].combine(closest_boxes_circuits[1])
                circuits.remove(closest_boxes_circuits[1])
            elif len(closest_boxes_circuits) == 1:
                closest_boxes_circuits[0].add_junction_box(closest_boxes[0] if closest_boxes_circuits[0].contains(closest_boxes[1]) else closest_boxes[1])
            else:
                new_circuit = Circuit([closest_boxes[0], closest_boxes[1]])
                circuits.append(new_circuit)
        except Exception as e:
            print(f"Exception in iteration {index}: {e}")
            import traceback
            traceback.print_exc()
            break


    print(f"Loop ended at iteration {index} with {len(circuits)} circuits")
    
    # Count how many boxes are in circuits
    boxes_in_circuits = sum(len(c.junction_boxes) for c in circuits)
    print(f"Boxes in circuits: {boxes_in_circuits} out of {len(junction_boxes)}")
    
    circuits.sort(key=lambda c: len(c.junction_boxes), reverse=True)

    print(f"Total circuits: {len(circuits)}")

    largest_circuits = circuits[:3]
    product_of_sizes = 1
    for circuit in largest_circuits:
        product_of_sizes *= len(circuit.junction_boxes)
    print(f"Product of sizes of the 3 largest circuits: {product_of_sizes}")