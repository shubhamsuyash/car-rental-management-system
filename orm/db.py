from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy import Column, String, Integer, Float, Boolean
    
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String)
    phone = Column(String)
    username = Column(String)
    password = Column(String)
    role = Column(String)

    def __str__(self):
        return self.fname

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    reg_no = Column(String)
    year = Column(String)
    color = Column(String)
    rent = Column(Float)
    available = Column(Boolean)
    details = Column(String)

    def __str__(self):
        return f'{self.brand}-{self.model}({self.year})'

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    address = Column(String)
    details = Column(String)

    def __str__(self):
        return self.fname

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    car_id = Column(Integer, ForeignKey('cars.id'))
    rental_start_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    rental_end_datetime = Column(DateTime)
    total_cost = Column(Float)
    booking_status = Column(String)  # Use this column to store 'active' or 'completed'
    # Define relationships
    customer = relationship("Customer", back_populates="bookings")
    car = relationship("Car", back_populates="bookings")

class Payment(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    payment_amount = Column(Float)
    payment_status = Column(String)  # Use this column to store 'paid' or 'pending'
    payment_method = Column(String)

    # Define relationship
    booking = relationship("Booking", back_populates="payments")

if __name__ == "__main__":
    engine = create_engine('sqlite:///cardb.sqlite3', echo=True)
    Base.metadata.create_all(engine)