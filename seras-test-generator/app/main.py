"""FastAPI application entry point."""

from fastapi import FastAPI

from app.routers.test_generator import router

app = FastAPI(title="seras-test-generator")
app.include_router(router)
