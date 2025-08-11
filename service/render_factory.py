from service.renderer import JsonRenderer, XmlRenderer
from service.renderer import Renderer


class RendererFactory:
    _renderers = {
        "json": JsonRenderer,
        "xml": XmlRenderer,
    }

    @classmethod
    def create_renderer(cls, format_type: str) -> Renderer:
        try:
            return cls._renderers[format_type]()
        except KeyError:
            raise ValueError(f"Unknown renderer format: {format_type}")
