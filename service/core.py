from typing import List, Dict
from service.loader import DataLoader
from service.renderer import Renderer


def combine_data(students: List[Dict], rooms: List[Dict]) -> List[Dict]:
    room_map = {room["id"]: {**room, "students": []} for room in rooms}
    for student in students:
        room_id = student.get("room")
        if room_id in room_map:
            room_map[room_id]["students"].append(student)
    return list(room_map.values())


class App:
    def __init__(self, data_loader: DataLoader, renderer: Renderer):
        self.data_loader = data_loader
        self.renderer = renderer

    def run(self, students_path: str, rooms_path: str) -> None:
        students = self.data_loader.load(students_path)
        rooms = self.data_loader.load(rooms_path)
        combined = combine_data(students, rooms)
        output = self.renderer.render(combined)
        print(output)
