from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Date


MYSQL_HOST = "172.17.0.2"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "secret"
MYSQL_DB = "curstomer"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(
                                MYSQL_USER,
                                MYSQL_PWD,
                                MYSQL_HOST,
                                MYSQL_PORT,
                                MYSQL_DB
)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()




class Customer(Base):

    __tablename__ = "customer"
    
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    first_name = Column(String(80), nullable=False)
    lasst_name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    created_at = Column(created_at, nullable=False) 


def add_customer(id, first_name, lasst_name, email, created_at):
    try:
        customer = Customer(id=id, first_name=first_name, lasst_name=lasst_name, email=email, created_at=created_at)
        session.add(customer)
        session.commit()

        return True

    except Exception as e:
        print(e)

        return False

def get_customer_by_id(id):
    try:
        result = session.query(Customer).filter_by(id=id).first()
        return result
    except Exception as e:
        print(e)
        return False

def get_all_customers():
    try:
        result = session.query(Customer).filter_by()

        return result
    except Exception as e:
        print(e)
        return False

def delete_customer_by_id(id):
    try:
        customer_to_delete = get_customer_by_id(id)
        if customer_to_delete :
            session.delete(customer_to_delete)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
