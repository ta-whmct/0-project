from enum import Enum, unique
from pathlib import Path

from app.config.types import EndpointParams, BunkerNameConstrType

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
ENVS_DIR = CONFIG_DIR / "envs"
LOG_DIR = BASE_DIR / "logs"
LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)

BUNKER_NAME_CONSTR: BunkerNameConstrType = {"min": 3, "max": 32}


@unique
class ApiV1Endpoints(Enum):
    bunker = EndpointParams(name="/bunkers", tags=["bunker"])
