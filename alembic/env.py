# alembic/env.py
from __future__ import annotations

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

import os
import sys
from pathlib import Path

# --- Cho phép import "app.*" khi chạy từ thư mục alembic ---
ROOT = Path(__file__).resolve().parents[1]  # project root (thư mục chứa "app/")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# --- Import metadata của models ---
from app.models.base_model import Base
# Import các model để Alembic "thấy" schema (đừng xoá, dù không dùng trực tiếp)
from app.models import chat_logs_model  # noqa: F401

# Alembic config / logging
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Đây là metadata Alembic sẽ autogenerate
target_metadata = Base.metadata


def _get_sync_url() -> str:
    """
    Lấy URL cho Alembic (driver sync). Ưu tiên:
    1) ALEMBIC_DATABASE_URL (sync)
    2) DATABASE_URL (có thể async; nếu bạn dùng 2 biến thì biến này nên sync luôn)
    3) fallback: sqlite sync local
    """
    return (
        os.getenv("ALEMBIC_DATABASE_URL")
        or os.getenv("DATABASE_URL")
        or "sqlite:///./repairmen_local.db"
    )


def run_migrations_offline() -> None:
    """Chạy migration ở 'offline mode' (không tạo Engine)."""
    url = _get_sync_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=url.startswith("sqlite"),  # hỗ trợ ALTER TABLE trên SQLite
        compare_type=True,  # phát hiện đổi kiểu cột
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Chạy migration ở 'online mode' (tạo Engine & connect)."""
    cfg = config.get_section(config.config_ini_section) or {}
    url = _get_sync_url()
    cfg["sqlalchemy.url"] = url

    connectable = engine_from_config(
        cfg,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=url.startswith("sqlite"),
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()