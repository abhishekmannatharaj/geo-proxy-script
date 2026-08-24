from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, HttpUrl


class RequestConfig(BaseModel):
    url: HttpUrl

    method: str = Field(
        default="GET",
        description="HTTP method"
    )

    headers: Optional[Dict[str, str]] = None

    params: Optional[Dict[str, Any]] = None

    body: Optional[Dict[str, Any]] = None

    timeout: int = Field(
        default=15,
        ge=1,
        le=120
    )

    use_proxy: bool = True

    max_retries: int = Field(
        default=3,
        ge=1,
        le=10
    )


class TaskResponse(BaseModel):
    task_id: str
    status: str