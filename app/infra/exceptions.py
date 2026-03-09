from string import Template

from starlette.exceptions import HTTPException


class ApplicationHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        self._message_tmpl: Template
        super().__init__(status_code, detail)


class BunkerException(ApplicationHTTPException): ...


class InvalidMaxVolume(BunkerException):
    def __init__(self, max_volume: int, new_volume: int, current_volume: int):
        self._message_tmpl = Template(
            "Invalid value for bunker volume. max: $max, new: $new, current: $current"
        )
        detail = self._message_tmpl.safe_substitute(
            max=max_volume, new=new_volume, current=current_volume
        )
        super().__init__(status_code=400, detail=detail)
