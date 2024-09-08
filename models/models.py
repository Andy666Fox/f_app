from sqlalchemy import MetaData, Integer, String, JSON
from sqlalchemy import TIMESTAMP, ForeignKey, Table, Column
from datetime import datetime
metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registred_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

