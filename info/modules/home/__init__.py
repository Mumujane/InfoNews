from flask import Blueprint

# 创建蓝图
home_blue = Blueprint("home", __name__)

# 4. 关联视图函数
from .view import *