from flask import Blueprint, render_template, url_for
from ..models import DeviceInfo

bp = Blueprint('info', __name__, url_prefix='/info')

@bp.route('/list/')
def lists():
    info_list = DeviceInfo.query.order_by(DeviceInfo.index.desc())
    return render_template('info/devinfo_list.html', info_list=info_list)
