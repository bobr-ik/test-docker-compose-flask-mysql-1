from typing import Optional
from sqlalchemy import Table, Column, Integer, String, MetaData, Numeric, ForeignKey, text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.database import Base


metadata_obj = MetaData()


class FirstORM(Base):
    __tablename__ = "first"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))