-- Tạo bảng Nhập Kho
CREATE TABLE IF NOT EXISTS NhapKho (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MaHang INTEGER,
    NgayNhap TEXT,
    SoLuong INTEGER,
    GiaNhap REAL,
    FOREIGN KEY (MaHang) REFERENCES MatHang(MaHang)
);

ALTER TABLE NhapKho ADD COLUMN NhaCungCap TEXT;      -- Nhà cung cấp nào giao hàng
ALTER TABLE NhapKho ADD COLUMN NhanVienNhap TEXT;    -- Ai thực hiện nhập kho
ALTER TABLE NhapKho ADD COLUMN HanSuDung TEXT;       -- Hạn sử dụng (nếu là thực phẩm, thuốc)
ALTER TABLE NhapKho ADD COLUMN SoHoaDon TEXT;        -- Số hóa đơn/phiếu nhập
ALTER TABLE NhapKho ADD COLUMN GhiChu TEXT;          -- Ghi chú thêm (hàng lỗi, khuyến mãi)

-- Insert nhập kho
INSERT INTO NhapKho (MaHang, NgayNhap, SoLuong, GiaNhap)
VALUES (?, ?, ?, ?);

-- Lấy danh sách nhập kho theo mã hàng
SELECT * FROM NhapKho WHERE MaHang = ?;

-- Tìm theo giá nhập
SELECT * FROM NhapKho WHERE GiaNhap = ?;
