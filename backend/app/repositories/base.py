"""
Base repository with common database operations.
"""

from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy.orm import Session

from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Base repository with common database operations."""

    def __init__(self, model: Type[ModelType], db: Session):
        """
        Initialize repository with model and database session.

        Args:
            model: SQLAlchemy model class.
            db: Database session.
        """
        self.model = model
        self.db = db

    def get(self, id: int) -> Optional[ModelType]:
        """
        Get a record by ID.

        Args:
            id: Record ID.

        Returns:
            Record if found, None otherwise.
        """
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Get all records with pagination.

        Args:
            skip: Number of records to skip.
            limit: Maximum number of records to return.

        Returns:
            List of records.
        """
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, obj_in) -> ModelType:
        """
        Create a new record.

        Args:
            obj_in: Data to create record with.

        Returns:
            Created record.
        """
        obj_data = obj_in if isinstance(obj_in, dict) else obj_in.model_dump()
        db_obj = self.model(**obj_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, id: int, obj_in) -> Optional[ModelType]:
        """
        Update a record.

        Args:
            id: Record ID.
            obj_in: Data to update record with.

        Returns:
            Updated record if found, None otherwise.
        """
        db_obj = self.get(id)
        if not db_obj:
            return None

        obj_data = (
            obj_in
            if isinstance(obj_in, dict)
            else obj_in.model_dump(exclude_unset=True)
        )
        for key, value in obj_data.items():
            setattr(db_obj, key, value)

        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> bool:
        """
        Delete a record.

        Args:
            id: Record ID.

        Returns:
            True if record was deleted, False if not found.
        """
        db_obj = self.get(id)
        if not db_obj:
            return False

        self.db.delete(db_obj)
        self.db.commit()
        return True
