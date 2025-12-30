class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: float,
                 coords = [0,0]) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
    
    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step
    
    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def go_up(self, step: int = 1) -> None:
        if len(self.coords) == 2:
            self.coords.append(step)
        else:
            self.coords[2] += step
    
    def go_down(self, step: int = 1) -> None:
        if len(self.coords) == 2:
            self.coords.append(-step)
        else:
            self.coords[2] -= step

class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: float,
                 coords: list = [0,0],
                 max_load_weight = 20,
                 current_load = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
    
    def hook_load(self, cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        
    def unhook_load(self):
        self.current_load = None

class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight