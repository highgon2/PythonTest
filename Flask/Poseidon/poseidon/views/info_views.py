from flask import Blueprint, render_template, request
from ..models import DeviceInfo

bp = Blueprint('info', __name__, url_prefix='/info')

@bp.route('/list/')
def lists():
    page = request.args.get('page', type=int, default=1)
    info_list = DeviceInfo.query.order_by(DeviceInfo.index.desc())
    info_list = info_list.paginate(page, per_page=10)
    return render_template('info/devinfo_list.html', info_list=info_list)

@bp.route('/list/<int:index>')
def detail(index):
    dev_info = DeviceInfo.query.get_or_404(index)
    return render_template('info/devinfo_detail.html', dev_info=dev_info)