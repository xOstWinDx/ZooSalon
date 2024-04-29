import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, DateTime
from app.database import Base


class User(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(index=True, unique=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[bytes] = mapped_column(nullable=False)
    is_admin: Mapped[bool] = mapped_column(
        default=False, server_default="false", nullable=False
    )
    registration_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=func.now(),
        default=datetime.datetime.now(),
    )
