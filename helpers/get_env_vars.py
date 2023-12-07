from functools import lru_cache

from configurations import settings


@lru_cache()
def get_settings():
    return settings.Settings()
