from utils import load_input

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = None 

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"JunctionBox(x={self.x}, y={self.y}, z={self.z})"
    
    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
    
    def find_closest(self, junction_boxes: list['JunctionBox']):
        closest_box = None
        closest_distance = float('inf')
        for box in junction_boxes:
            if box == self:
                continue
            distance = self.distance_to(box)
            if distance < closest_distance:
                closest_distance = distance
                closest_box = box
        return closest_box, closest_distance
    
def loadBoxes():
    result = load_input()
    junction_boxes = []
    for line in result:
        x, y, z = map(int, line.split(','))
        junction_boxes.append(JunctionBox(x, y, z))
    return junction_boxes
    
class Circuit:
    def __init__(self):
        self.junction_boxes = []

    def __init__(self, junction_box):
        self.junction_boxes = [junction_box]
        junction_box.circuit = self 

    def get_junction_boxes(self) -> list[JunctionBox]:
        return self.junction_boxes

    def combine_circuits(self, other_circuit):
        self.junction_boxes.extend(other_circuit.junction_boxes)
        for box in other_circuit.junction_boxes:
            box.circuit = self
        del other_circuit

    def add_junction_box(self, junction_box: JunctionBox):
        self.junction_boxes.append(junction_box)
        junction_box.circuit = self 

    def find_closest_circuit(self, circuits: list['Circuit']):
        closest_circuit = None
        closest_distance = float('inf')
        for circuit in circuits:
            if circuit == self:
                continue
            for box in self.get_junction_boxes():
                other_box, distance = box.find_closest(circuit.get_junction_boxes())
                if distance < closest_distance:
                    closest_distance = distance
                    closest_circuit = circuit
        return closest_circuit, closest_distance
    
    def __str__(self):
        return f'Circuit with {len(self.junction_boxes)} junction boxes'

if __name__ == "__main__":
    circuits = []
    boxes: list[JunctionBox] = loadBoxes()
    for box in boxes:
        if box.circuit is None:
            circuit = Circuit(box)
            circuits.append(circuit)
        else:
            circuit = box.circuit
        
        # find nearest box to box
        closest_box, distance = box.find_closest(boxes)
        if closest_box.circuit is None:
            circuit.add_junction_box(closest_box)
        elif closest_box.circuit != circuit:
            other_circuit = closest_box.circuit
            circuit.combine_circuits(other_circuit)
            circuits.remove(other_circuit)

    # sort circuits by box count
    circuits.sort(key=lambda c: len(c.get_junction_boxes()), reverse=True)

    for circuit in circuits:
        print(f"{circuit}")