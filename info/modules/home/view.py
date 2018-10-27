from info import sr
from info.modules.home import home_blue

import logging # python内置的日志模块 将日志信息在控制台中输出, 并且可以将日志保存到文件中
from flask import current_app, render_template


# 2. 使用蓝图注册路由
@home_blue.route("/view")
def index():
    sr.set("name", "lisi")
    # logging.error("出现了一个错误") # logging默认的输出不包含错误位置, 显示效果不好, 可以使用flask内置的日志输出语法来代替

    # current_app.logger.error("出现了一个错误")

    return render_template("index.html")


@home_blue.route("/favicon.ico")
def favicon():
    return current_app.send_static_file("news/favicon.ico")