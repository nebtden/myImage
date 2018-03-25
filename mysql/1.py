# 数据库表是一个二维表, 包含多行多列. 把一个表的内容用pyton的数据接口表示的话, 可以用list表示多行
# list的每一个元素是tuple, 表示一个记录.比如id 和name的user表
# [
#     ('1', 'Michael'),
#     ('2', 'Bob'),
#     ('3', 'Adam')
# ]

# Python的DB-API返回的数据接口就是像上面这样.
# 但是用tuple表示一行很难看出表的结构.如果把一个tuple用class实例表示, 就可以更容易看出表的结构

# class User(object):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# 这就是传说中的ORM技术: Object-Relational Mapping, 把关系数据库的表结构映射到对象上.
# 但是由谁来做这个转换呢, 所以ORM框架应运而生.
# 在Python中, 最有名的ORM框架是SQLAlchemy. 我们来看看SQLAlchemy的用法.

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:password@localhost:3306/test')
# 创建DBSession类型pi
DBSession = sessionmaker(bind=engine)
# create_engine用来初始化数据库连接.
# SQLAlchemy用一个字符串表示连接信息'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# # 创建session对象:
# session = DBSession()
# # 创建新User对象
# new_user = User(id='5', name='Bob')
# # 添加到session
# session.add(new_user)
# # 提交保存到数据库
# session.commit()
# # 关闭session
# session.close()

# 可见将关键是获取session, 然后把对象添加到session, 最后提交并关闭.(DBSession对象, 可以看做是当前数据库的连接)

# 查询
session = DBSession()
# 创建Query查询, filter是where条件, 最后调用one()返回唯一行, 如果调用all()则返回所有行.
user = session.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)
session.close()

# ORM就是把数据库表的行与相应的对象简历关联, 互相转换.
# 由于关系数据库的多个表还可以用外键实现一对多, 多对多的关联, 相应地, ORM框架也可以提供两个对象之间的一对多, 多对多功能.
# 例如, 如果一个User拥有多个Book, 就可以定义一对多关系如下
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     books = relationship('BOOK')
#
# class BOOK(Base):
#     __tablename__ = 'book'
#     id = Column(String(20), primary_key=True)
#     nam = Column(String(20))
#     user_id = Column(String(20), ForeignKey('user.id'))
