from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# PUBLIC_INTERFACE
class Department(Base):
    """Department entity stores department details."""

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    employees = relationship("Employee", back_populates="department")
    job_positions = relationship("JobPosition", back_populates="department")


# PUBLIC_INTERFACE
class JobPosition(Base):
    """JobPosition entity stores job position details."""

    __tablename__ = "job_positions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    department = relationship("Department", back_populates="job_positions")
    employees = relationship("Employee", back_populates="job_position")


# PUBLIC_INTERFACE
class Employee(Base):
    """Employee entity stores employee information."""

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    job_position_id = Column(Integer, ForeignKey("job_positions.id"), nullable=False)

    department = relationship("Department", back_populates="employees")
    job_position = relationship("JobPosition", back_populates="employees")
