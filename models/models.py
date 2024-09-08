from sqlalchemy import MetaData, Integer, String, JSON
from sqlalchemy import TIMESTAMP, ForeignKey, Table, Column, Boolean
from datetime import datetime
metadata = MetaData()

roles = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

users = Table(
    'user',
    metadata,
    Column('username', String, nullable=False),
    Column('id', Integer, primary_key=True),
    Column('registred_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(roles.c.id)),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)

