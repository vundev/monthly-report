from functools import lru_cache
from .settings_model import Settings

# --- Define here dependency resolvers. ---

@lru_cache
def get_settings():
    """
    Want to read the .env file only once after multiple injections.
    """
    return Settings()
