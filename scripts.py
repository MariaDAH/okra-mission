#ORM SYNTAX  - SQLAlchemy 
from okra.models import Category
from okra import db
from flask_sqlalchemy import SQLAlchemy
import datetime

retail = Category(name="Retail")
financial = Category(name="Financial Services")
toys = Category(name="Toys")
electronics = Category(name="Consumer electronics")
apparel = Category(name="Apparel")
homeapply = Category(name="Home appliances")
beauty = Category(name="Beauty & personal care")
household = Category(name="Household products")
furniture = Category(name="Furniture")
automobiles = Category(name="Automobiles")
groceries = Category(name="Groceries")
restaurant = Category(name="Restaurant")

db.session.add_all([retail, financial, toys, electronics, apparel, homeapply, beauty, household, furniture, automobiles, groceries, restaurant])
db.session.commit()

from okra.models import User
daredevil=User(email='daredevil@hotmail.com',plaintext_password="daredevil",role="user")
jesiccajones=User(email='jesiccajones@hotmail.com',plaintext_password="jesiccajones",role="admin")
ironman=User(email='ironman@hotmail.com',plaintext_password="ironman",role="associate")
wonderwoman=User(email='wonderwoman@hotmail.com',plaintext_password="wonderwoman",role="admin")
thor=User(email='thor@hotmail.com',plaintext_password="thor",role="associate")
db.session.add_all([daredevil, jesiccajones, ironman, wonderwoman, thor])
db.session.commit()

from okra.models import Ecobusiness
ecoasda = Ecobusiness(name='Ecoasda', user_id=1, website='www.ecoasda.com', location='M643E', phonenumber='076542189', comment='', subscriptionplan='Yearly', email='ecoasda1@hotmail.com', registered_on=None, updated_on=None, category_id=12)
agasallo = Ecobusiness(name='Agasallo', user_id=2, website='www.agasallo.online', location='M4643', phonenumber='12434', comment='Testing', subscriptionplan='Monthly', email='agasallo@gmail.com', registered_on=datetime.datetime.now(), updated_on=datetime.datetime.now(), category_id=11)
carballo = Ecobusiness(name='CarballoMoble', user_id=1, website='www.carballo.com', location='M643E', phonenumber='076542189', comment='', subscriptionplan='Monthly', email='carballo@hotmail.com', registered_on=datetime.datetime.now(), updated_on=None, category_id=9)
toxo = Ecobusiness(name='Toxo', user_id=3, website='www.toxo.com', location='ST14DA', phonenumber='076542189', comment='', subscriptionplan='Montly', email='toxo@hotmail.com', registered_on=datetime.datetime.strptime('06/21/17', "%m/%d/%y")+ datetime.timedelta(days=-10), updated_on=datetime.datetime.now(), category_id=7)
volvoreta = Ecobusiness(name='Volvoreta', user_id=5, website='www.volvoreta.online', location='STA5AG', phonenumber='12434', comment='Testing', subscriptionplan='Monthly', email='volvoreta@gmail.com', registered_on=datetime.datetime.strptime('06/21/18', "%m/%d/%y")+ datetime.timedelta(days=-20), updated_on=datetime.datetime.now(), category_id=2)
sapoconcho = Ecobusiness(name='Sapoconcho', user_id=1, website='www.sapoconcho.com', location='M643E', phonenumber='076542189', comment='', subscriptionplan='Yearly', email='sapoconcho@hotmail.com', registered_on=datetime.datetime.strptime('06/21/18', "%m/%d/%y")+ datetime.timedelta(hours=-20), updated_on=datetime.datetime.now(), category_id=4)
db.session.add_all([ecoasda, agasallo, carballo, toxo, volvoreta, sapoconcho])
db.session.commit()

