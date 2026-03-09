from fastapi import APIRouter

from .bunker import router as bunker_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)
router.include_router(bunker_router)
