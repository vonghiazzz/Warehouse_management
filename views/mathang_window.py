from tkinter import *
from tkinter import ttk
from entities.mathang import MatHang
from utils import theme
from tkinter import messagebox
from datetime import datetime
from controllers.mathang_controller import MatHangController
from controllers.nhapkho_controller import NhapKhoController


class MatHangWindow:
    def __init__(self, master):
        self.controller = MatHangController()
        self.nhap_kho_controller = NhapKhoController()

        self.master = master
        self.master.title("Quản Lý Mặt Hàng")
        self.master.resizable(True, True)

        self.theme = theme.CURRENT_THEME

        self.frame = Frame(self.master, bg=self.theme["bg_color"])
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Tạo frame chứa tiêu đề và nút chuyển trang
        header_frame = Frame(self.frame, bg=self.theme["bg_color"])
        header_frame.pack(fill=X, pady=5)

        header_frame.columnconfigure(0, weight=1)
        header_frame.columnconfigure(1, weight=0)

        Label(
            header_frame,
            text="Quản lý mặt hàng",
            font=("Arial", 14, "bold"),
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=0, column=0, sticky="ew", padx=(0, 10))

        Button(
            header_frame,
            text="Quản lý kho",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=20,
            command=self.open_nhap_kho,
        ).grid(row=0, column=1, padx=(10, 0))

        form = Frame(self.frame, bg=self.theme["bg_color"])
        form.pack(fill=X, pady=5)

        Label(
            form,
            text="Tên hàng:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=0, column=0, pady=2)
        self.name_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.name_entry.grid(row=0, column=1, pady=2)

        Label(
            form,
            text="Đơn vị tính:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=1, column=0, pady=2)

        # Combobox cho trạng thái
        self.unit_var = StringVar()
        self.unit_combobox = ttk.Combobox(
            form,
            textvariable=self.unit_var,
            values=["Cái", "Hộp", "Kg", "Tờ"],  
            state="readonly",  
            width=27
        )
        self.unit_combobox.grid(row=1, column=1, pady=2)
        self.unit_combobox.current(0)  # Mặc định chọn "Hoạt động"

        Label(
            form,
            text="Loại hàng: ",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=2, column=0, pady=2)
        self.type_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.type_entry.grid(row=2, column=1, pady=2)


        Label(
            form,
            text="Mô tả:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=0, column=4, pady=2,  padx=(40, 0))
        self.description_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.description_entry.grid(row=0, column=5, pady=2)

        Label(
            form,
            text="Tồn tối thiểu:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=1, column=4, pady=2, padx=(40, 0))
        self.minimum_amount_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.minimum_amount_entry.grid(row=1, column=5, pady=2)

        Label(
            form,
            text="Trạng thái:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=2, column=4, pady=2, padx=(40, 0))

        # Combobox cho trạng thái
        self.status_var = StringVar()
        self.status_combobox = ttk.Combobox(
            form,
            textvariable=self.status_var,
            values=["Hoạt động", "Ngưng", "Chờ xử lý"],  # Danh sách lựa chọn
            state="readonly",  # Chỉ cho chọn, không cho gõ lung tung
            width=27
        )
        self.status_combobox.grid(row=2, column=5, pady=2)
        self.status_combobox.current(0)  # Mặc định chọn "Hoạt động"


      # Tạo frame chứa nút
        button_frame = Frame(form, bg=self.theme["bg_color"])
        button_frame.grid(row=3, column=6, pady=10, sticky="e")

        Button(
            button_frame,
            text="Delete",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=5,
            command=self.delete_item,
            ).pack(side=RIGHT, padx=2)

        Button(
            button_frame,
            text="Update",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=5,
            command=self.update_item,
            ).pack(side=RIGHT, padx=2)

        Button(
            button_frame,
            text="Create",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=5,
            command=self.save_item,
            ).pack(side=RIGHT, padx=2)

        # Thêm bảng hiển thị danh sách sinh viên
        columns = (
            "Mã Hàng",
            "Tên Hàng",
            "Đơn Vị Tính",
            "Loại Hàng",
            "Mô Tả",
            "Tồn Tối Thiểu",
            "Trạng Thái",
            "Ngày Tạo",
        )
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.pack(fill=BOTH, expand=True, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.show_history_dialog)
        self.load_data()
    
    # def load_data(self):
    #     for item in self.tree.get_children():
    #         self.tree.delete(item)

    #     items = self.controller.get_all_mat_hang()
    #     for mh in items:
    #         # Định dạng ngày tạo nếu có
    #         if hasattr(mh, "ngay_tao") and mh.ngay_tao:
    #             try:
    #                 if isinstance(mh.ngay_tao, str):
    #                     dt = datetime.strptime(mh.ngay_tao, "%m/%d/%Y %H:%M:%S")
    #                 else:
    #                     dt = mh.ngay_tao
    #                 ngay_tao_str = dt.strftime("%m/%d/%Y")
    #             except Exception:
    #                 ngay_tao_str = str(mh.ngay_tao)
    #         else:
    #             ngay_tao_str = ""
    #         self.tree.insert("", "end", values=(
    #             mh.ma_hang,
    #             mh.ten_hang,
    #             mh.don_vi,
    #             mh.loai,
    #             mh.mo_ta,
    #             mh.ton_toi_thieu,
    #             mh.trang_thai,
    #             ngay_tao_str
    #         ))
    def load_data(self):
        # Xóa dữ liệu cũ trên TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Lấy tất cả mặt hàng
        items = self.controller.get_all_mat_hang()
        for mh in items:
            # Xử lý ngày tạo
            ngay_tao_str = ""
            if hasattr(mh, "ngay_tao") and mh.ngay_tao:
                dt = None
                if isinstance(mh.ngay_tao, str):
                    # Thử parse theo ISO format (SQLite thường lưu thế này)
                    try:
                        dt = datetime.strptime(mh.ngay_tao, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        try:
                            # Nếu bạn có lưu theo dạng Mỹ
                            dt = datetime.strptime(mh.ngay_tao, "%m/%d/%Y %H:%M:%S")
                        except ValueError:
                            dt = None
                else:
                    # Nếu DB trả về datetime object thì gán thẳng
                    dt = mh.ngay_tao

                # Nếu parse được thì format lại
                if dt:
                    ngay_tao_str = dt.strftime("%m/%d/%Y %H:%M:%S")
                else:
                    ngay_tao_str = str(mh.ngay_tao)

            # Insert vào TreeView
            self.tree.insert("", "end", values=(
                mh.ma_hang,
                mh.ten_hang,
                mh.don_vi,
                mh.loai,
                mh.mo_ta,
                mh.ton_toi_thieu,
                mh.trang_thai,
                ngay_tao_str
            ))

    def clear_form(self):
        self.name_entry.delete(0, END)
        self.type_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.minimum_amount_entry.delete(0, END)
        self.unit_combobox.current(0)
        self.status_combobox.current(0)

    def save_item(self):
        try:
            # Tạo object MatHang
            data = MatHang(
                ten_hang=self.name_entry.get(),
                don_vi=self.unit_var.get(),
                loai=self.type_entry.get(),
                mo_ta=self.description_entry.get(),
                ton_toi_thieu=self.minimum_amount_entry.get(),
                trang_thai=self.status_var.get(),
                ngay_tao = datetime.now()
            )
            errors = self.controller.validate_mat_hang(data)
            if errors:
                messagebox.showwarning("Lỗi dữ liệu", "\n".join(errors))
                return
            if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn tạo bản ghi mới?"):
                return

            # Gọi controller để thêm mặt hàng mới
            ma_hang = self.controller.add_mat_hang(data)
            if not ma_hang:
                messagebox.showwarning("Cảnh báo", "Tên hàng đã tồn tại!")
                return

            print(">>> Thêm mặt hàng thành công:", vars(data))

            # Thêm vào TreeView
            self.tree.insert("", "end", values=(
                data.ma_hang,
                data.ten_hang,
                data.don_vi,
                data.loai,
                data.mo_ta,
                data.ton_toi_thieu,
                data.trang_thai,
                data.ngay_tao.strftime("%m/%d/%Y %H:%M:%S")
            ))

            messagebox.showinfo("Thành công", "Thêm mặt hàng thành công.")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu mặt hàng: {e}")



    def open_nhap_kho(self):
        self.frame.destroy()
        from views.nhapkho_window import NhapKhoWindow

        NhapKhoWindow(self.master)

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn mặt hàng để cập nhật.")
            return

        item_id = selected[0]
        values = self.tree.item(item_id, "values")
        ma_hang = values[0]  # cột Mã Hàng

        try:
            # Lấy dữ liệu mới từ form
            data = MatHang(
                ten_hang=self.name_entry.get(),
                don_vi=self.unit_var.get(),
                loai=self.type_entry.get(),
                mo_ta=self.description_entry.get(),
                ton_toi_thieu=self.minimum_amount_entry.get(),
                trang_thai=self.status_var.get(),
                ngay_tao=datetime.now()
            )
            errors = self.controller.validate_mat_hang(data)
            if errors:
                messagebox.showerror("Lỗi dữ liệu", "\n".join(errors))
                return
            if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn cập nhật bản ghi này?"):
                return

            # Gọi controller/service để update DB
            self.controller.update_mat_hang(ma_hang, data)

            # Cập nhật lại dòng trong TreeView
            self.tree.item(item_id, values=(
                ma_hang,
                data.ten_hang,
                data.don_vi,
                data.loai,
                data.mo_ta,
                data.ton_toi_thieu,
                data.trang_thai,
                values[7]  # giữ nguyên Ngày Tạo cũ
            ))

            messagebox.showinfo("Thành công", "Cập nhật mặt hàng thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cập nhật mặt hàng: {e}")

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        # Đổ dữ liệu lên form
        self.name_entry.delete(0, END)
        self.name_entry.insert(0, values[1])

        self.unit_var.set(values[2])
        self.type_entry.delete(0, END)
        self.type_entry.insert(0, values[3])
        self.description_entry.delete(0, END)
        self.description_entry.insert(0, values[4])
        self.minimum_amount_entry.delete(0, END)
        self.minimum_amount_entry.insert(0, values[5])
        self.status_var.set(values[6])

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn mặt hàng để xóa.")
            return
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa mặt hàng đã chọn?"):
            return

        for item in selected:
            values = self.tree.item(item, "values")
            ma_hang = values[0]  # lấy MaHang từ cột đầu tiên
            try:
                # Gọi service để xóa mềm (soft delete)
                self.controller.delete_mat_hang(ma_hang)
                # Xóa khỏi TreeView
                self.tree.delete(item)
                self.clear_form()
                messagebox.showinfo("Thành công", "Xóa mặt hàng thành công.")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể xóa mặt hàng: {e}")

    def show_history_dialog(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        ma_hang = values[0]

        history = self.nhap_kho_controller.get_history_by_mat_hang(int(ma_hang))

        if not history:
            messagebox.showinfo("Lịch sử nhập kho", "Không có lịch sử nhập kho cho mặt hàng này.")
            return

        top = Toplevel(self.master)
        top.title(f"Lịch sử nhập kho - Mã hàng {ma_hang}")

        columns = [
            "ID", "Tên hàng", "Số lượng", "Giá nhập", "Nhà cung cấp",
            "Nhân viên nhập", "Hạn sử dụng", "Số hóa đơn", "Ghi chú", "Ngày tạo"
        ]
        tree = ttk.Treeview(top, columns=columns, show="headings", height=10)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        # Thêm scrollbar dọc
        scrollbar = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Đổ dữ liệu vào treeview
        for item in history:
            # Format hạn sử dụng
            han_su_dung = item.han_su_dung
            if han_su_dung:
                try:
                    if isinstance(han_su_dung, str):
                        dt = datetime.strptime(han_su_dung, "%m/%d/%Y")
                    else:
                        dt = han_su_dung
                    han_su_dung = dt.strftime("%m/%d/%Y")
                except Exception:
                    han_su_dung = str(item.han_su_dung)
            # Format ngày tạo
            ngay_tao = item.ngay_tao
            if ngay_tao:
                try:
                    if isinstance(ngay_tao, str):
                        dt = datetime.strptime(ngay_tao, "%m/%d%Y %H:%M:%S")
                    else:
                        dt = ngay_tao
                    ngay_tao = dt.strftime("%m/%d/%Y")
                except Exception:
                    ngay_tao = str(item.ngay_tao)

            tree.insert(
                "",
                "end",
                values=(
                    item.id,
                    item.ten_hang,
                    item.so_luong,
                    item.gia_nhap,
                    item.nha_cung_cap,
                    item.nhan_vien_nhap,
                    han_su_dung,
                    item.so_hoa_don,
                    item.ghi_chu,
                    ngay_tao,
                ),
            )



