from sqlalchemy import select
from data.database import sync_engine, session_factory, Base
from data.models import FirstORM


class SyncORM:
    @staticmethod
    def create_table():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
    
        
    @staticmethod
    def insert_data():
        with session_factory() as session:
            create = []
            create += [FirstORM(id=1, name="first"), FirstORM(id=2, name="second")]

            session.add_all(create)
            session.commit()
    

    @staticmethod
    def select_data(id):
        with session_factory() as session:
            query = select(FirstORM).where(FirstORM.id == id)
            res = session.execute(query)
            conditers = res.scalars().all() 
            return f"{conditers[0].name = }"