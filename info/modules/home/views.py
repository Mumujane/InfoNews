from info import sr
from info.constants import HOME_PAGE_MAX_NEWS
from info.models import User, News
from info.modules.home import home_blue

import logging # python内置的日志模块 将日志信息在控制台中输出, 并且可以将日志保存到文件中
from flask import current_app, render_template, session, jsonify, request

# 2. 使用蓝图注册路由
from info.utils.response_code import error_map, RET


@home_blue.route("/")
def index():
    # 判断用户是否登录
    user_id = session.get("user_id")

    user = None # type: User
    if user_id:
        try:
            user = User.query.get(user_id)
        except BaseException as e:
            current_app.logger.error(e)

    user = user.to_dict() if user else None


    # 首页 按照`点击量`查询`前10条`新闻数据
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(10).all()
    except BaseException as e:
        current_app.logger.error(e)

    news_list = [news.to_dict() for news in news_list]

    return render_template("index.html", user= user, news_list=news_list)


@home_blue.route("/favicon.ico")
def favicon():
    return current_app.send_static_file("news/favicon.ico")


@home_blue.route('/get_news_list')
def get_news_list():
    """
    首页新闻列表
    cid: 分类id
    cur_page: 当面页面
    per_count: 每页显示数量
    :return:
    """
    # 获取参数
    cid = request.args.get("cid")
    cur_page = request.args.get("cur_page")
    per_count = request.args.get("per_count", HOME_PAGE_MAX_NEWS)

    # 参数校验
    if not all([cid, cur_page, per_count]):
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])

    # 根据参数查询目标新闻 按照发布时间和分类和页码查询新闻数据
    try:
        cid = int(cid)
        cur_page = int(cur_page)
        per_count = int(per_count)
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg=error_map[RET.PARAMERR])
    filter_list = []
    if cid != 1:
        filter_list.append(News.category_id == cid)

    try:
        pn = News.query.filter(*filter_list).order_by(News.create_time.desc()).paginate(cur_page, per_count)
        news_list = [news.to_dict() for news in pn.items]

        total_page = pn.pages
    except BaseException as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg=error_map[RET.DBERR])

    data = {
        "news_list": news_list,
        "total_page": total_page
    }
    return jsonify(errno=RET.OK, errmsg=error_map[RET.OK], data = data)
