from fastapi import APIRouter

from chaser_website.api.v1 import router as Router

__all__ = (Router)

router = APIRouter(prefix="/api")

for api_router in __all__:
    router.include_router(api_router)
