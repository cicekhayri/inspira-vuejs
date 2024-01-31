from database import db_session
from inspira.logging import log
from sqlalchemy.exc import SQLAlchemyError

from src.model.user import User


class UserRepository:

    def get_all_users(self):
        return db_session.query(User).all()

    def get_user_by_email(self, email: str) -> User:
        return db_session.query(User).filter_by(email=email).first()

    def create_user(self, user: User) -> bool:
        try:
            db_session.add(user)
            db_session.commit()
            return True
        except SQLAlchemyError as e:
            db_session.rollback()
            log.error(f"Error creating user: {e}")
            return False
