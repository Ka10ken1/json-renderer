import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import List, Dict


class Renderer(ABC):
    @abstractmethod
    def render(self, data: List[Dict]) -> str:
        pass


class JsonRenderer(Renderer):
    def render(self, data: List[Dict]) -> str:
        return json.dumps(data, indent=2, ensure_ascii=False)


class XmlRenderer(Renderer):
    def render(self, data: List[Dict]) -> str:
        root = ET.Element("rooms")
        for room in data:
            room_elem = ET.SubElement(
                root, "room", id=str(room["id"]), name=room["name"]
            )
            students_elem = ET.SubElement(room_elem, "students")
            for student in room.get("students", []):
                ET.SubElement(
                    students_elem,
                    "student",
                    id=str(student["id"]),
                    name=student["name"],
                )
        return ET.tostring(root, encoding="unicode", method="xml")
