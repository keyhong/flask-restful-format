"""TODO"""

from db import db

class BasicModel(db.Model):
    """TODO"""

    __tablename__ = "TODO: tablename"

    prj_id = db.Column(db.String(80), primary_key=True)
    stan_yy = db.Column(db.String(80), nullable=False)
    bz_cd = db.Column(db.String(80), nullable=False)
