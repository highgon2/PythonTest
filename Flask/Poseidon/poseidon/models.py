from . import db

class Device(db.Model):
    imei       = db.Column(db.String(16), nullable=False, primary_key=True)

class DeviceInfo(db.Model):
    index           = db.Column(db.Integer, primary_key=True)
    device_imei     = db.Column(db.String(16), db.ForeignKey('device.imei', ondelete='CASCADE'))
    imei            = db.relationship('Device', backref=db.backref('info_set', cascade='all, delete-orphan'));
    datetime        = db.Column(db.String(32), nullable=False)
    rpm             = db.Column(db.Integer, nullable=False)
    coolant         = db.Column(db.Integer, nullable=False)
    oil_pressure    = db.Column(db.Integer, nullable=False)
    oil_temperature = db.Column(db.Integer, nullable=False)
    voltage         = db.Column(db.Integer, nullable=False)
    fuel            = db.Column(db.Integer, nullable=False)
    fault_code      = db.Column(db.String(256))
    gps_latitude    = db.Column(db.Float)
    gps_longitude   = db.Column(db.Float)
    gps_knots       = db.Column(db.Float)
    gps_direction   = db.Column(db.Float)
    gps_date        = db.Column(db.String(6))
    gps_utc         = db.Column(db.String(10))
    