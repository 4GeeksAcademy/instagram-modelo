from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean  # (starter)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {"id": self.id, "email": self.email}


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    caption: Mapped[str | None] = mapped_column(String(255))

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, "caption": self.caption}


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)

    def serialize(self):
        return {"id": self.id, "post_id": self.post_id, "url": self.url}


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    text: Mapped[str] = mapped_column(String(255), nullable=False)

    def serialize(self):
        return {"id": self.id, "post_id": self.post_id, "user_id": self.user_id, "text": self.text}


class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    followed_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    def serialize(self):
        return {"id": self.id, "follower_id": self.follower_id, "followed_id": self.followed_id}


if __name__ == "__main__":
    try:
        from eralchemy2 import render_er
        render_er(db.Model, "diagram.png")
        print("diagram.png generado")
    except Exception as e:
        print("Error generando diagrama:", e)
