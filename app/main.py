from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi

from app.config.database import Base, engine
from app.models import *
from app.controller.user_controller import router as user_router
from app.controller.blog_controller import router as blog_router
from app.controller.auth_controller import router as auth_router
from app.middlewares.auth_middlewares import get_current_user


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    version="1.0.0"
)

app.include_router(user_router, prefix="/api/v1/user", tags=["User"])
app.include_router(blog_router, prefix ="/api/v1/blog", tags = ["Blog"])
app.include_router(auth_router, prefix = "/api/v1/auth", tags=["auth"])




@app.get("/")
def root():
    return {"message": "Welcome to Blog API"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )

    # Define Bearer token auth scheme
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    # Apply BearerAuth only to /blog routes (paths startswith "/blog")
    for path in openapi_schema["paths"]:
        # Apply only to /blog and not to /auth or /user
        if path.startswith("/blog"):
            for method in openapi_schema["paths"][path]:
                openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
        else:
            # Remove any existing security requirement for non-blog routes (optional)
            for method in openapi_schema["paths"][path]:
                if "security" in openapi_schema["paths"][path][method]:
                    del openapi_schema["paths"][path][method]["security"]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi



