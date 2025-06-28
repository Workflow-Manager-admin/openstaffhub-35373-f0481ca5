from pydantic import BaseModel, Field, EmailStr


# PUBLIC_INTERFACE
class DepartmentBase(BaseModel):
    name: str = Field(..., description="Department name")


# PUBLIC_INTERFACE
class DepartmentCreate(DepartmentBase):
    pass


# PUBLIC_INTERFACE
class DepartmentRead(DepartmentBase):
    id: int

    class Config:
        orm_mode = True


# PUBLIC_INTERFACE
class JobPositionBase(BaseModel):
    title: str = Field(..., description="Job position title")
    department_id: int = Field(..., description="ID of department")


# PUBLIC_INTERFACE
class JobPositionCreate(JobPositionBase):
    pass


# PUBLIC_INTERFACE
class JobPositionRead(JobPositionBase):
    id: int

    class Config:
        orm_mode = True


# PUBLIC_INTERFACE
class EmployeeBase(BaseModel):
    name: str = Field(..., description="Employee name")
    email: EmailStr = Field(..., description="Employee's email")
    department_id: int = Field(..., description="Department ID")
    job_position_id: int = Field(..., description="JobPosition ID")


# PUBLIC_INTERFACE
class EmployeeCreate(EmployeeBase):
    pass


# PUBLIC_INTERFACE
class EmployeeRead(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
