from .settings_model import Settings
from typing import Annotated
from fastapi import Depends
from .settings import get_settings


SettingsDep = Annotated[Settings, Depends(get_settings)]
