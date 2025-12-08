from utils import load_input

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

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
    
def loadCircuits():
    result = load_input()
    junction_boxes = []
    for line in result:
        x, y, z = map(int, line.split(','))
        junction_boxes.append(JunctionBox(x, y, z))

    circuits = [Circuit(box) for box in junction_boxes]
    return circuits
    
class Circuit:
    def __init__(self, junction_box):
        self.junction_boxes = [junction_box]

    def get_junction_boxes(self) -> list[JunctionBox]:
        return self.junction_boxes

    def combine_circuits(self, other_circuit):
        self.junction_boxes.extend(other_circuit.junction_boxes)
        del other_circuit

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
    circuits = loadCircuits()
    for circuit in circuits:
        closest_circuit, distance = circuit.find_closest_circuit(circuits)
        circuit.combine_circuits(closest_circuit)

    circuits.sort(key=lambda c: len(c.junction_boxes), reverse=True)

    for circuit in circuits:
        print(f"{circuit}")