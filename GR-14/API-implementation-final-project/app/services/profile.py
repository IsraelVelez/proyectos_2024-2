from sqlalchemy.orm import Session
from app.models.profile import ProfileRecord
from app.schemas.profile import ProfileCreate

class ProfileService:
    @staticmethod
    def create_profile_record(db: Session, record: ProfileCreate, parameters: str, result: str):
        """
        Guarda un registro de perfilado en la base de datos.
        - parameters: Parámetros usados en la función perfilada.
        - result: Resultado o datos filtrados del perfilado.
        """
        db_record = ProfileRecord(
            function_name=record.function_name,
            module_name=record.module_name,
            parameters=parameters,
            result=result,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    @staticmethod
    def get_all_profile_records(db: Session):
        """Obtiene todos los registros de perfilado."""
        return db.query(ProfileRecord).all()
