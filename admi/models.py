from django.db import models

# ビューに関連するパーミッションを定義
class Meta:
    permissions = [
        ("can_access_admin_view", "Can access admin view"),
    ]
