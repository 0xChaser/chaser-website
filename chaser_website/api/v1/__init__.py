from fastapi import APIrouter

from chaser_website.api.v1.project import router as ProjectRouter

router = APIrouter(prefix="/v1")

router.include_router(ProjectRouter)