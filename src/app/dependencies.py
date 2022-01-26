__all__ = ['Templates']

from functools import lru_cache

from fastapi.templating import Jinja2Templates


@lru_cache
def Templates() -> Jinja2Templates:
    return Jinja2Templates(directory='./../templates')
