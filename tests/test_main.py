from service.core import combine_data
from service.renderer import JsonRenderer, XmlRenderer


students = [
    {"id": 1, "name": "Alice", "room": 101},
    {"id": 2, "name": "Bob", "room": 102},
    {"id": 3, "name": "Charlie", "room": 101},
]


rooms = [
    {"id": 101, "name": "Blue Room"},
    {"id": 102, "name": "Green Room"},
]


class TestDataProcessing:
    def test_combine_data(self):
        combined = combine_data(students, rooms)
        assert len(combined) == 2

        blue = next(r for r in combined if r["id"] == 101)
        green = next(r for r in combined if r["id"] == 102)

        assert blue["name"] == "Blue Room"
        assert len(blue["students"]) == 2
        assert blue["students"][0]["name"] == "Alice"

        assert green["name"] == "Green Room"
        assert len(green["students"]) == 1
        assert green["students"][0]["name"] == "Bob"

    def test_render_json(self):
        combined = combine_data(students, rooms)
        renderer = JsonRenderer()
        output = renderer.render(combined)

        assert isinstance(output, str)
        assert '"students": [' in output
        assert '"name": "Blue Room"' in output

    def test_render_xml(self):
        combined = combine_data(students, rooms)
        renderer = XmlRenderer()
        output = renderer.render(combined)

        assert output.startswith("<rooms>")
        assert '<room id="101" name="Blue Room">' in output
        assert '<student id="1" name="Alice" />' in output
