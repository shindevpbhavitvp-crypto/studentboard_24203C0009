from config.db import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    notice_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)