import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import MagicMock
from controllers.mathang_controller import MatHangController
from entities.mathang import MatHang
from datetime import datetime

@pytest.fixture
def controller():
    ctrl = MatHangController()
    # Mock repository methods
    ctrl.repo.get_all = MagicMock(return_value=[])
    ctrl.repo.add = MagicMock(return_value=1)
    ctrl.repo.update = MagicMock(return_value=None)
    ctrl.repo.get_by_id = MagicMock(return_value=MatHang(
        ma_hang=1,
        ten_hang="Test hàng",
        don_vi="Cái",
        loai="Loại A",
        mo_ta="Mô tả test",
        ton_toi_thieu=5,
        trang_thai="Hoạt động",
        ngay_tao=datetime.now(),
        is_deleted=0
    ))
    ctrl.repo.soft_delete = MagicMock(return_value=None)
    return ctrl

def test_add_mat_hang_success(controller):
    mh = MatHang(
        ten_hang="Test hàng",
        don_vi="Cái",
        loai="Loại A",
        mo_ta="Mô tả test",
        ton_toi_thieu=5,
        trang_thai="Hoạt động",
        ngay_tao=datetime.now(),
        is_deleted=0
    )
    result = controller.add_mat_hang(mh)
    assert result == 1

def test_add_mat_hang_duplicate(controller):
    controller.repo.get_all.return_value = [MatHang(ten_hang="Trùng tên", ma_hang=1)]
    mh2 = MatHang(
        ten_hang="Trùng tên",
        don_vi="Hộp",
        loai="Loại C",
        mo_ta="Mô tả khác",
        ton_toi_thieu=2,
        trang_thai="Ngưng",
        ngay_tao=datetime.now(),
        is_deleted=0
    )
    result = controller.add_mat_hang(mh2)
    assert result == -1

def test_update_mat_hang_success(controller):
    controller.repo.get_all.return_value = []
    mh = MatHang(
        ten_hang="Update hàng",
        don_vi="Kg",
        loai="Loại D",
        mo_ta="Mô tả update",
        ton_toi_thieu=3,
        trang_thai="Hoạt động",
        ngay_tao=datetime.now(),
        is_deleted=0,
        ma_hang=1
    )
    result = controller.update_mat_hang(1, mh)
    assert result is True

def test_update_mat_hang_duplicate_name(controller):
    controller.repo.get_all.return_value = [
        MatHang(ten_hang="Tên A", ma_hang=1),
        MatHang(ten_hang="Tên B", ma_hang=2)
    ]
    mh2 = MatHang(
        ten_hang="Tên A",  # Trùng tên với mh1
        don_vi="Hộp",
        loai="Loại F",
        mo_ta="Mô tả khác",
        ton_toi_thieu=2,
        trang_thai="Ngưng",
        ngay_tao=datetime.now(),
        is_deleted=0,
        ma_hang=2
    )
    result = controller.update_mat_hang(2, mh2)
    assert result is False

def test_delete_mat_hang_success(controller):
    controller.repo.get_by_id.return_value = MatHang(ma_hang=1, ten_hang="Xóa hàng")
    result = controller.delete_mat_hang(1)
    assert result is True

def test_delete_mat_hang_not_exist(controller):
    controller.repo.get_by_id.return_value = None
    result = controller.delete_mat_hang(999999)
    assert result is False