#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-25 00:50:56 (CST)
# Last Update:星期日 2016-11-13 0:13:55 (CST)
#          By:
# Description:
# **************************************************************************
from flask import (url_for, redirect, flash, send_from_directory, current_app)
from flask.views import MethodView
from flask_maple.forms import flash_errors
from flask_login import login_required
from .forms import AvatarForm
from .controls import UploadModel
import os


class AvatarView(MethodView):
    decorators = [login_required]

    def post(self):
        form = AvatarForm()
        if form.validate_on_submit():
            UploadModel.avatar(form)
            flash('上传成功', 'success')
            return redirect(url_for('setting.setting'))
        else:
            if form.errors:
                flash_errors(form)
            return redirect(url_for('setting.setting'))


class AvatarFileView(MethodView):
    def get(self, filename):
        avatar_path = os.path.join(current_app.static_folder,
                                   current_app.config.get('AVATAR_FOLDER',
                                                          'avatars/'))
        if not os.path.exists(os.path.join(avatar_path, filename)):
            avatar_path = os.path.join(current_app.static_folder, 'images/')
            filename = 'Moo.png'
        return send_from_directory(avatar_path, filename)
