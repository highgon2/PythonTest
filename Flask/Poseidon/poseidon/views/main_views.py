import json
import traceback

from flask import Blueprint, request, redirect, url_for

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('info.lists'))

@bp.route('/input')
def input():
    jstring = request.args.get('jstring')
    try:
        jdata = json.loads(jstring)
        check_device(jdata['imei'])
        add_device_info(jdata)
    except Exception as e:
        traceback.print_exc()
        return "{}".format(e)
        # return redirect(url_for('main.index'))

    return redirect(url_for('info.lists'))

def check_device(sn):
    from .. import db
    from ..models import Device

    dev = Device.query.filter(Device.imei.like(sn)).all()
    if not dev:
        dev = Device(imei=sn)
        db.session.add(dev)
        db.session.commit()

def add_device_info(jdata):
    from .. import db
    from ..models import DeviceInfo

    dev_info = DeviceInfo(
                        device_imei     = jdata['imei'],
                        datetime        = jdata['datetime'],
                        rpm             = jdata['rpm'],
                        coolant         = jdata['coolant'],
                        oil_pressure    = jdata['oil_pressure'],
                        oil_temperature = jdata['oil_temperature'],
                        voltage         = jdata['voltage'],
                        fuel            = jdata['fuel'])

    if 'fault_code' in jdata:
        fault_list = ""
        for i, error_code in enumerate(jdata['fault_code']):
            if i != (len(jdata['fault_code']) - 1):
                fault_list += error_code + ","
            else:
                fault_list += error_code

        dev_info.fault_code = fault_list;

    if 'gps_date' in jdata:
        latitude  = (int)(jdata['gps_latitude'] / 100)
        latitude  = latitude + ((jdata['gps_latitude'] - (latitude * 100)) / 60)

        longitude = (int)(jdata['gps_longitude'] / 100)
        longitude = longitude + ((jdata['gps_longitude'] - (longitude * 100)) / 60)
        print("latitude = {}, longitude = {}".format(latitude, longitude))

        dev_info.gps_latitude  = latitude
        dev_info.gps_longitude = longitude
        dev_info.gps_knots     = jdata['gps_knots']
        dev_info.gps_direction = jdata['gps_direction']
        dev_info.gps_date      = jdata['gps_date']
        dev_info.gps_utc       = jdata['gps_utc']

    db.session.add(dev_info)
    db.session.commit()