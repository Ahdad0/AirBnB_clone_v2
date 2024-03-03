#!/usr/bin/python3
"""Database Storage"""
import os
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine


class DBStorage:
    """manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes SQL Database Storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        host = os.getenv('HBNB_MYSQL_HOST')
        env = os.getenv('HBNB_ENV')
        db_name = os.getenv('HBNB_MYSQL_DB')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        DB = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, pwd, host, db_name)
        self.__engine = create_engine(DB, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dictio = dict()
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for ele in query:
                key = "{}.{}".format(type(ele).__name__, ele.id)
                dictio[key] = ele
        else:
            li = [State, City, User, Place, Review, Amenity]
            for clas in li:
                query = self.__session.query(clas)
                for ele in query:
                    key = "{}.{}".format(type(ele).__name__, ele.id)
                    dictio[key] = ele
        return (dictio)

    def new(self, obj):
        """add the object"""
        self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration the database"""
        Base.metadata.create_all(self.__engine)

        s = sessionmaker(bind=self.__engine, expire_on_commit=False)

        Sess = scoped_session(s)

        self.__session = Sess()
