from typing import Optional, Union
from pydantic import BaseModel


class ApiResponse(BaseModel):
    message: Optional[str]
    data: Union[list, dict] = []
    status_code: int = 200
    success: bool = True

    class Config:
        from_attributes = True
