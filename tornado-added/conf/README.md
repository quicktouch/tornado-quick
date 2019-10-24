存放配置文件



如数据的相关配置: 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:123@localhost:3306/demo?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()



