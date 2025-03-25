from pydantic import BaseModel, EmailStr, field_validator


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")