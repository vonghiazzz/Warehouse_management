class NhapKhoHistoryDTO:
    def __init__(
        self,
        id,
        ten_hang,
        so_luong,
        gia_nhap,
        nha_cung_cap,
        nhan_vien_nhap,
        han_su_dung,
        so_hoa_don,
        ghi_chu,
        ngay_tao,
        is_delete
    ):
        self.id = id
        self.ten_hang = ten_hang
        self.so_luong = so_luong
        self.gia_nhap = gia_nhap
        self.nha_cung_cap = nha_cung_cap
        self.nhan_vien_nhap = nhan_vien_nhap
        self.han_su_dung = han_su_dung
        self.so_hoa_don = so_hoa_don
        self.ghi_chu = ghi_chu
        self.ngay_tao = ngay_tao
        self.is_delete = is_delete