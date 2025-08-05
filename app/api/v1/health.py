from fastapi import APIRouter   


router = APIRouter()


@router.get("/", tags=["Root"])
def root():
    return {"status": "ok"}

@router.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
