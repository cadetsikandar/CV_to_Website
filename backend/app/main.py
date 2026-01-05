from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text
from app.core.database import engine, Base
from app.users import routes as user_routes
from app.users import models as user_models
from app.cvs import models as cv_models
from app.cvs.routes import router as cv_router
import os

# Create necessary directories for portfolio generation
os.makedirs("uploads", exist_ok=True)
os.makedirs("generated_portfolios", exist_ok=True)
os.makedirs("hosted_portfolios", exist_ok=True)

# Create all tables in the DB
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Resume2Site API",
    description="API for generating portfolio websites from resumes",
    version="1.0.0"
)

# CORS middleware - Allow frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers WITHOUT prefix for cv_router
app.include_router(user_routes.router, prefix="/api", tags=["Users"])
app.include_router(cv_router, tags=["Portfolio"])  # Removed prefix="/api"

# Mount static files for generated portfolios
try:
    app.mount("/static", StaticFiles(directory="generated_portfolios"), name="static")
except Exception as e:
    print(f"Warning: Could not mount static files: {e}")


@app.get("/")
def health_check():
    return {
        "status": "ok", 
        "message": "Resume2Site backend running",
        "version": "1.0.0",
        "endpoints": {
            "health": "/",
            "db_test": "/db-test",
            "generate_portfolio": "/generate-portfolio",  # Updated
            "preview_portfolio": "/portfolio/preview/{portfolio_id}",  # Updated
            "download_portfolio": "/portfolio/download/{portfolio_id}",  # Updated
            "publish_portfolio": "/portfolio/publish/{portfolio_id}",  # Updated
            "view_hosted": "/portfolio/{portfolio_id}",
            "list_portfolios": "/portfolio/list",  # Updated
            "delete_portfolio": "/portfolio/{portfolio_id}"
        }
    }


@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {
                "db": "connected",
                "status": "healthy",
                "message": "Database connection successful"
            }
    except Exception as e:
        return {
            "db": "error",
            "status": "unhealthy",
            "message": str(e)
        }


@app.get("/info")
def api_info():
    """Get API information and available endpoints"""
    return {
        "api_name": "Resume2Site API",
        "version": "1.0.0",
        "description": "Generate beautiful portfolio websites from PDF/DOCX resumes",
        "features": [
            "Upload CV (PDF/DOCX)",
            "AI-powered portfolio generation",
            "Preview generated portfolios",
            "Download portfolio HTML files",
            "Publish and host portfolios",
            "Get shareable URLs"
        ],
        "supported_formats": ["PDF", "DOCX"],
        "max_file_size": "10MB"
    }


# Error handlers - Return JSONResponse instead of dict
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Not Found",
            "message": "The requested resource was not found",
            "path": str(request.url)
        }
    )


@app.exception_handler(500)
async def internal_error_handler(request: Request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred",
            "details": str(exc)
        }
    )