from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import RedirectResponse
from app.core.init_db import init_db
from app.api.router import api_router
from app.core.deps import get_db, get_current_user

app = FastAPI(
    title="Mentor-Mentee Matching API",
    description="API for matching mentors and mentees in a mentoring platform",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url=None,  # Swagger UI 커스텀 경로 사용
    redoc_url=None
)

# CORS 설정 (프론트엔드 연동용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/swagger-ui")

@app.get("/swagger-ui", include_in_schema=False)
def swagger_ui():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Mentor-Mentee Matching API")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(api_router, prefix="/api")
