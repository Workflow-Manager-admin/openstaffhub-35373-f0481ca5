from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import get_db

router = APIRouter()


# Department Endpoints


@router.post(
    "/departments/",
    response_model=schemas.DepartmentRead,
    summary="Create Department"
)
def create_department(
    department: schemas.DepartmentCreate, db: Session = Depends(get_db)
):
    db_dept = db.query(models.Department).filter(
        models.Department.name == department.name
    ).first()
    if db_dept:
        raise HTTPException(
            status_code=400, detail="Department with this name already exists."
        )
    new_dept = models.Department(**department.dict())
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept


@router.get(
    "/departments/",
    response_model=List[schemas.DepartmentRead],
    summary="List Departments"
)
def list_departments(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(models.Department).offset(skip).limit(limit).all()


@router.get(
    "/departments/{dept_id}",
    response_model=schemas.DepartmentRead,
    summary="Get Department"
)
def get_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.query(models.Department).filter(
        models.Department.id == dept_id
    ).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept


@router.put(
    "/departments/{dept_id}",
    response_model=schemas.DepartmentRead,
    summary="Update Department"
)
def update_department(
    dept_id: int, department: schemas.DepartmentCreate, db: Session = Depends(get_db)
):
    dept = db.query(models.Department).filter(
        models.Department.id == dept_id
    ).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    dept.name = department.name
    db.commit()
    db.refresh(dept)
    return dept


@router.delete(
    "/departments/{dept_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Department"
)
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.query(models.Department).filter(
        models.Department.id == dept_id
    ).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(dept)
    db.commit()
    return


# Job Position Endpoints


@router.post(
    "/positions/",
    response_model=schemas.JobPositionRead,
    summary="Create Job Position"
)
def create_position(
    position: schemas.JobPositionCreate, db: Session = Depends(get_db)
):
    db_pos = db.query(models.JobPosition).filter(
        models.JobPosition.title == position.title
    ).first()
    if db_pos:
        raise HTTPException(
            status_code=400, detail="Job position with this title already exists."
        )
    new_pos = models.JobPosition(**position.dict())
    db.add(new_pos)
    db.commit()
    db.refresh(new_pos)
    return new_pos


@router.get(
    "/positions/",
    response_model=List[schemas.JobPositionRead],
    summary="List Job Positions"
)
def list_positions(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(models.JobPosition).offset(skip).limit(limit).all()


@router.get(
    "/positions/{pos_id}",
    response_model=schemas.JobPositionRead,
    summary="Get Job Position"
)
def get_position(pos_id: int, db: Session = Depends(get_db)):
    position = db.query(models.JobPosition).filter(
        models.JobPosition.id == pos_id
    ).first()
    if not position:
        raise HTTPException(status_code=404, detail="Job position not found")
    return position


@router.put(
    "/positions/{pos_id}",
    response_model=schemas.JobPositionRead,
    summary="Update Job Position"
)
def update_position(
    pos_id: int, position: schemas.JobPositionCreate, db: Session = Depends(get_db)
):
    pos = db.query(models.JobPosition).filter(
        models.JobPosition.id == pos_id
    ).first()
    if not pos:
        raise HTTPException(status_code=404, detail="Job position not found")
    pos.title = position.title
    pos.department_id = position.department_id
    db.commit()
    db.refresh(pos)
    return pos


@router.delete(
    "/positions/{pos_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Job Position"
)
def delete_position(pos_id: int, db: Session = Depends(get_db)):
    pos = db.query(models.JobPosition).filter(
        models.JobPosition.id == pos_id
    ).first()
    if not pos:
        raise HTTPException(status_code=404, detail="Job position not found")
    db.delete(pos)
    db.commit()
    return


# Employee Endpoints


@router.post(
    "/employees/",
    response_model=schemas.EmployeeRead,
    summary="Create Employee"
)
def create_employee(
    employee: schemas.EmployeeCreate, db: Session = Depends(get_db)
):
    db_emp = db.query(models.Employee).filter(
        models.Employee.email == employee.email
    ).first()
    if db_emp:
        raise HTTPException(
            status_code=400, detail="Employee with this email already exists."
        )
    new_emp = models.Employee(**employee.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


@router.get(
    "/employees/",
    response_model=List[schemas.EmployeeRead],
    summary="List Employees"
)
def list_employees(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(models.Employee).offset(skip).limit(limit).all()


@router.get(
    "/employees/{emp_id}",
    response_model=schemas.EmployeeRead,
    summary="Get Employee"
)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(
        models.Employee.id == emp_id
    ).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@router.put(
    "/employees/{emp_id}",
    response_model=schemas.EmployeeRead,
    summary="Update Employee"
)
def update_employee(
    emp_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)
):
    emp = db.query(models.Employee).filter(
        models.Employee.id == emp_id
    ).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.name = employee.name
    emp.email = employee.email
    emp.department_id = employee.department_id
    emp.job_position_id = employee.job_position_id
    db.commit()
    db.refresh(emp)
    return emp


@router.delete(
    "/employees/{emp_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Employee"
)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(
        models.Employee.id == emp_id
    ).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return
