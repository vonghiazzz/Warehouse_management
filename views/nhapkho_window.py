from tkinter import *
from tkinter import ttk, messagebox
from utils import theme
from controllers.nhapkho_controller import NhapKhoController
from controllers.mathang_controller import MatHangController
from entities.nhapkho import NhapKho
from datetime import datetime


class NhapKhoWindow:
    def __init__(self, master):
        self.controller = NhapKhoController()
        self.master = master
        self.master.title("Quản Lý Kho")
        self.master.resizable(True, True)

        # Lấy danh sách mặt hàng để map vào combobox
        mathangs = MatHangController().get_all_mat_hang()
        self.mathang_map = {f"{mh.ma_hang} - {mh.ten_hang}": mh.ma_hang for mh in mathangs}

        self.theme = theme.CURRENT_THEME

        self.frame = Frame(self.master, bg=self.theme["bg_color"])
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = Frame(self.frame, bg=self.theme["bg_color"])
        header_frame.pack(fill=X, pady=5)
        header_frame.columnconfigure(0, weight=1)
        header_frame.columnconfigure(1, weight=0)



        Label(
            header_frame,
            text="Quản lý kho",
            font=("Arial", 14, "bold"),
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=0, column=0, sticky="ew", padx=(0, 10))

        Button(
            header_frame,
            text="Quản lý mặt hàng",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=20,
            command=self.open_mat_hang,
        ).grid(row=0, column=1, padx=(10, 0))

        # Form nhập liệu
        form = Frame(self.frame, bg=self.theme["bg_color"])
        form.pack(fill=X, pady=5)

        # Combobox chọn mã hàng
        Label(form, text="Mã mặt hàng:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=0, column=0, pady=2)
        self.mathang_var = StringVar()
        self.mathang_combobox = ttk.Combobox(form, textvariable=self.mathang_var, width=28, state="readonly")
        self.mathang_combobox["values"] = list(self.mathang_map.keys())
        self.mathang_combobox.grid(row=0, column=1, pady=2)
        if mathangs:
            self.mathang_combobox.current(0)

        # Số lượng
        Label(form, text="Số lượng:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=1, column=0, pady=2)
        self.amount_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.amount_entry.grid(row=1, column=1, pady=2)

        # Giá nhập
        Label(form, text="Giá nhập:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=2, column=0, pady=2)
        self.price_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.price_entry.grid(row=2, column=1, pady=2)

        # Nhà cung cấp
        Label(form, text="Nhà cung cấp:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=3, column=0, pady=2)
        self.supplier_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.supplier_entry.grid(row=3, column=1, pady=2)

        # Nhân viên nhập
        Label(form, text="Nhân viên nhập:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=0, column=4, pady=2, padx=(40, 0))
        self.staff_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.staff_entry.grid(row=0, column=5, pady=2)

        # Hạn sử dụng
        Label(form, text="Hạn sử dụng:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=1, column=4, pady=2, padx=(40, 0))
        self.expiry_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.expiry_entry.grid(row=1, column=5, pady=2)

        # Số hóa đơn
        Label(form, text="Số hóa đơn:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=2, column=4, pady=2, padx=(40, 0))
        self.bill_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.bill_entry.grid(row=2, column=5, pady=2)

        # Ghi chú
        Label(form, text="Ghi chú:", width=15, anchor="w",
              bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=3, column=4, pady=2, padx=(40, 0))
        self.note_entry = Entry(form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.note_entry.grid(row=3, column=5, pady=2)

        # Hàng tìm kiếm + CRUD
        Label(form, text="Tìm kiếm:", width=15, anchor="w",
            bg=self.theme["bg_color"], fg=self.theme["text_color"]).grid(row=4, column=0, pady=2)

        self.search_var = StringVar()
        self.search_entry = Entry(form, textvariable=self.search_var, width=30,
                                bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.search_entry.grid(row=4, column=1, pady=2)
        self.search_entry.bind("<KeyRelease>", self.filter_data)

        # Combobox chọn trường tìm kiếm
        self.search_field = StringVar()
        self.field_combobox = ttk.Combobox(form, textvariable=self.search_field, width=20, state="readonly")
        self.field_combobox["values"] = ("Tất cả", "Mặt hàng", "Nhà cung cấp", "Nhân viên nhập", "Số hóa đơn","Giá nhập", "Ghi chú")
        self.field_combobox.current(0)  # mặc định chọn "Tất cả"
        self.field_combobox.grid(row=4, column=2, pady=2)

        # Các nút CRUD (vẫn ở bên phải, cột 6)
        button_frame = Frame(form, bg=self.theme["bg_color"])
        button_frame.grid(row=4, column=6, pady=10, sticky="e")

        Button(button_frame, text="Delete", bg=self.theme["button_color"], fg=self.theme["button_text"],
            width=6, command=self.delete_item).pack(side=RIGHT, padx=2)

        Button(button_frame, text="Update", bg=self.theme["button_color"], fg=self.theme["button_text"],
            width=6, command=self.update_item).pack(side=RIGHT, padx=2)

        Button(button_frame, text="Create", bg=self.theme["button_color"], fg=self.theme["button_text"],
            width=6, command=self.save_item).pack(side=RIGHT, padx=2)



        # TreeView hiển thị dữ liệu
        columns = ("ID", "Mặt hàng", "Số lượng", "Giá nhập", "Nhà cung cấp",
                   "Nhân viên nhập", "Hạn sử dụng", "Số hóa đơn", "Ghi chú", "Ngày tạo")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.pack(fill=BOTH, expand=True, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Load dữ liệu ban đầu
        self.load_data()

    def open_mat_hang(self):
        self.frame.destroy()
        from views.mathang_window import MatHangWindow
        MatHangWindow(self.master)

    def clear_form(self):
        self.amount_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.supplier_entry.delete(0, END)
        self.staff_entry.delete(0, END)
        self.expiry_entry.delete(0, END)
        self.bill_entry.delete(0, END)
        self.note_entry.delete(0, END)
        if self.mathang_combobox["values"]:
            self.mathang_combobox.current(0)

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        items = self.controller.get_all_nhap_kho()

        for nk in items:
            ma_ten = next((k for k, v in self.mathang_map.items() if v == nk.ma_hang), str(nk.ma_hang))
            self.tree.insert("", "end", values=(
                nk.id, ma_ten, nk.so_luong, nk.gia_nhap, nk.nha_cung_cap,
                nk.nhan_vien_nhap, nk.han_su_dung, nk.so_hoa_don, nk.ghi_chu,
                nk.ngay_tao if nk.ngay_tao else ""
            ))

    def save_item(self):
        try:
            data = NhapKho(
                ma_hang=self.mathang_map[self.mathang_var.get()],
                so_luong=self.amount_entry.get(),
                gia_nhap=self.price_entry.get(),
                nha_cung_cap=self.supplier_entry.get(),
                nhan_vien_nhap=self.staff_entry.get(),
                han_su_dung=self.expiry_entry.get(),
                so_hoa_don=self.bill_entry.get(),
                ghi_chu=self.note_entry.get(),
                ngay_tao=datetime.now(),
                is_delete=0
            )
            errors = self.controller.validate_nhap_kho(data)
            if errors:
                messagebox.showerror("Lỗi dữ liệu", "\n".join(errors))
                return
            if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn tạo bản ghi mới?"):
                return
            new_id = self.controller.add_nhap_kho(data)    
            self.load_data()
            self.clear_form()
            messagebox.showinfo("Thành công", "Thêm nhập kho thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu nhập kho: {e}")

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn bản ghi để cập nhật.")
            return
        
        values = self.tree.item(selected[0], "values")
        id = values[0]
        try:
            data = NhapKho(
                id=id,
                ma_hang=self.mathang_map[self.mathang_var.get()],
                so_luong=self.amount_entry.get(),
                gia_nhap=self.price_entry.get(),
                nha_cung_cap=self.supplier_entry.get(),
                nhan_vien_nhap=self.staff_entry.get(),
                han_su_dung=self.expiry_entry.get(),
                so_hoa_don=self.bill_entry.get(),
                ghi_chu=self.note_entry.get(),
                ngay_tao=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                is_delete=0
            )

            errors = self.controller.validate_nhap_kho(data)
            if errors:
                messagebox.showerror("Lỗi dữ liệu", "\n".join(errors))
                return

            if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn cập nhật bản ghi này?"):
                return

            if self.controller.update_nhap_kho(id, data):
                self.load_data()
                self.clear_form()
                messagebox.showinfo("Thành công", "Cập nhật thành công.")
            else:
                messagebox.showerror("Lỗi", "Không thể cập nhật nhập kho.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cập nhật nhập kho: {e}")

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn bản ghi để xóa.")
            return
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa bản ghi này?"):
            return
        values = self.tree.item(selected[0], "values")
        id = values[0]
        try:
            if self.controller.delete_nhap_kho(id):
                self.load_data()
                self.clear_form()
                messagebox.showinfo("Thành công", "Xóa thành công.")
            else:
                messagebox.showerror("Lỗi", "Không thể xóa bản ghi.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa nhập kho: {e}")

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self.amount_entry.delete(0, END)
        self.amount_entry.insert(0, values[2])
        self.price_entry.delete(0, END)
        self.price_entry.insert(0, values[3])
        self.supplier_entry.delete(0, END)
        self.supplier_entry.insert(0, values[4])
        self.staff_entry.delete(0, END)
        self.staff_entry.insert(0, values[5])
        self.expiry_entry.delete(0, END)
        self.expiry_entry.insert(0, values[6])
        self.bill_entry.delete(0, END)
        self.bill_entry.insert(0, values[7])
        self.note_entry.delete(0, END)
        self.note_entry.insert(0, values[8])

    
    def filter_data(self, event=None):
        keyword = self.search_var.get().lower().strip()
        field = self.search_field.get()

        # gọi validate ở service qua controller
        error = self.controller.validate_search(field, keyword)
        if error:
            messagebox.showerror("Lỗi tìm kiếm", error)
            return

        # Xóa dữ liệu cũ
        for row in self.tree.get_children():
            self.tree.delete(row)

        items = self.controller.get_all_nhap_kho()

        for nk in items:
            # Lấy "mã - tên" để hiển thị
            ma_ten = next((k for k, v in self.mathang_map.items() if v == nk.ma_hang), str(nk.ma_hang))

            values = (
                nk.id, ma_ten, nk.so_luong, nk.gia_nhap, nk.nha_cung_cap,
                nk.nhan_vien_nhap, nk.han_su_dung, nk.so_hoa_don, nk.ghi_chu,
                nk.ngay_tao if nk.ngay_tao else ""
            )

            # logic lọc
            match = False
            if not keyword:
                match = True
            elif field == "Tất cả":
                match = any(keyword in str(v).lower() for v in values)
            elif field == "Mặt hàng":
                match = keyword in ma_ten.lower()
            elif field == "Nhà cung cấp":
                match = keyword in str(nk.nha_cung_cap).lower()
            elif field == "Nhân viên nhập":
                match = keyword in str(nk.nhan_vien_nhap).lower()
            elif field == "Số hóa đơn":
                match = keyword in str(nk.so_hoa_don).lower()
            elif field == "Giá nhập":
                match = keyword in str(nk.gia_nhap).lower()
            elif field == "Ghi chú":
                match = keyword in str(nk.ghi_chu).lower()

            if match:
                self.tree.insert("", "end", values=values)



