from typing import List, Dict
from enum import Enum
from service.loader import DataLoader
from service.renderer import Renderer


class Keys(Enum):
    ROOM_ID = "id"
    ROOM_NAME = "name"
    STUDENTS = "students"
    STUDENT_ID = "id"
    STUDENT_NAME = "name"
    STUDENT_ROOM = "room"


class DataCombiner:

    @staticmethod
    def combine(students: List[Dict], rooms: List[Dict]) -> List[Dict]:
        room_map = {
            room[Keys.ROOM_ID.value]: {**room, Keys.STUDENTS.value: []}
            for room in rooms
        }
        for student in students:
            room_id = student.get(Keys.STUDENT_ROOM.value)
            if room_id in room_map:
                room_map[room_id][Keys.STUDENTS.value].append(student)
        return list(room_map.values())


class StudentRoomApp:

    def __init__(self, data_loader: DataLoader, renderer: Renderer):
        self.data_loader = data_loader
        self.renderer = renderer
        self.combiner = DataCombiner()

    def run(self, students_path: str, rooms_path: str) -> None:
        students = self.data_loader.load(students_path)
        rooms = self.data_loader.load(rooms_path)
        combined = self.combiner.combine(students, rooms)
        output = self.renderer.render(combined)
        print(output)
