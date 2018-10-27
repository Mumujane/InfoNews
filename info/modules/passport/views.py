from flask import request, abort, current_app, make_response, Response
from info import sr
from info.lib.captcha.pic_captcha import captcha
from info.modules.passport import passport_blue
import random
import re
from flask import request, abort, current_app, make_response, Response, jsonify
from info.lib.yuntongxun.sms import CCP
from info.utils.response_code import RET, error_map

@passport_blue.route("/get_img_code")
def get_img_code():
    """
    获取图片验证码
    :return: response
    """
    # 获取参数
    img_code_id = request.args.get("img_code_id")

    # 校验参数
    if not img_code_id:
        return abort(403)

    # 生成图片验证码
    img_name, img_text, img_bytes = captcha.generate_captcha()

    # 保存验证码文字和图片key redis 设置过期时间

    try:
        sr.set("img_code_id_" + img_code_id, img_text, ex=300)

    except BaseException as e:
        current_app.logger.error(e)  # 记录错误信息
        return abort(500)

    # 自定义响应对象  设置响应头的content-type为image/jpeg
    response = make_response(img_bytes)

    response.content_type = "image/jpeg"
    return response

@passport_blue.route("/get_sms_code", methods=['POST'])
def get_sms_code():
    """
    获取短信验证码
    :return: json结果
    """
    # 获取参数


    # 校验参数

    # 校验手机格式

    # 校验图片验证码 根据图片key取出真实的验证码文字

    # 生成随机短信验证码

    # 打印验证码

    # 发送短信

    # 保存短信验证码 设置过期时间

    # 返回json结果
