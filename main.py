import argparse
from service.loader import JsonDataLoader
from service.core import StudentRoomApp
from service.render_factory import RendererFactory


def parse_args():
    parser = argparse.ArgumentParser(
        description="Merge students into rooms and export as JSON or XML."
    )
    parser.add_argument(
        "students_file", type=str, help="Path to students.json"
    )
    parser.add_argument("rooms_file", type=str, help="Path to rooms.json")
    parser.add_argument(
        "--format",
        choices=["json", "xml"],
        default="json",
        help="Output format",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    data_loader = JsonDataLoader()
    renderer = RendererFactory.create_renderer(args.format)

    app = StudentRoomApp(data_loader, renderer)
    app.run(args.students_file, args.rooms_file)


if __name__ == "__main__":
    main()
