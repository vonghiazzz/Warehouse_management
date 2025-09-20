from tkinter import *
from tkinter import ttk
from utils import theme
from tkinter import messagebox
from datetime import datetime
from controllers.mathang_controller import MatHangController


class MatHangWindow:
    def __init__(self, master):
        self.controller = MatHangController()
        self.master = master
        self.master.title("Quản Lý Mặt Hàng")
        self.master.resizable(True, True)
        # self.load_data()  # <-- XÓA DÒNG NÀY
        # Lấy danh sách ngành học
        # db = SessionLocal()
        # majors = MajorController(db).get_majors()
        # db.close()
        # self.major_map = {major.name: major.id for major in majors}  # name: id

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
            text="Save",
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
        # self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.load_students()
        self.load_data()
    # def load_students(self):
    #     # Delete old data
    #     for item in self.tree.get_children():
    #         self.tree.delete(item)
    #     # Load new data
    #     db = SessionLocal()
    #     students = StudentController(db).get_students()
    #     for student in students:
    #         self.tree.insert(
    #             "",
    #             "end",
    #             values=(
    #                 student.id,
    #                 student.major_id,
    #                 student.name,
    #                 student.birthday,
    #                 (
    #                     "Male" if student.gender else "Female"
    #                 ),  # chuyển True/False thành chuỗi
    #                 student.phone,
    #                 student.email,
    #             ),
    #         )
    #         print(">>> Loaded student:", student.name)
    #     db.close()

    # def save_student(self):
    #     from datetime import datetime

    #     major_name = self.major_var.get()
    #     major_id = self.major_map.get(major_name, "")
    #     try:
    #         birthday = datetime.strptime(self.birthday_entry.get(), "%Y-%m-%d").date()
    #     except Exception:
    #         messagebox.showwarning("Fail format", "Birthday must be format yyyy-mm-dd!")
    #         return

    #     gender = True if self.gender_var.get() == "Male" else False

    #     data = {
    #         "ID Student": self.mssv_entry.get(),
    #         "ID Major": major_id,
    #         "Full Name": self.name_entry.get(),
    #         "Gender": "Male" if gender else "Female",
    #         "Birthday": self.birthday_entry.get(),
    #         "Phone": self.phone_entry.get(),
    #         "Email": self.email_entry.get(),
    #     }
    #     if (
    #         not data["ID Student"]
    #         or not data["ID Major"]
    #         or not data["Full Name"]
    #         or not data["Birthday"]
    #     ):
    #         messagebox.showwarning("Notification!", "Please fill out completely!")
    #         return
    #     if not StudentController.check_valid_information(
    #         self, data["Full Name"], data["Email"], data["Phone"]
    #     ):
    #         messagebox.showwarning(
    #             "Notification!", "Please enter valid information!\n"
    #             "- Name should not contain numbers\n"
    #             "- Email must be valid\n"
    #             "- Phone must be 10 numbers"
    #         )
    #         return
    #     try:
    #         db = SessionLocal()
    #         controller = StudentController(db)
    #         controller.add_student(
    #             student_id=data["ID Student"],
    #             name=data["Full Name"],
    #             birthday=birthday,
    #             gender=gender,
    #             email=data["Email"],
    #             phone=data["Phone"],
    #             major_id=data["ID Major"],
    #         )
    #         db.close()
    #         messagebox.showinfo("Success!", "Add a student successfully!")
    #         print(">>> Thêm sinh viên thành công:", data)
    #         self.load_students()  # Refresh
    #         self.delete_form()
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error when adding a student:\n{e}")
    #         print("Error when adding a student:", e)
    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        items = self.controller.get_all_mat_hang()
        for mh in items:
            self.tree.insert("", "end", values=(
                mh.ma_hang,
                mh.ten_hang,
                mh.don_vi,
                mh.loai,
                mh.mo_ta,
                mh.ton_toi_thieu,
                mh.trang_thai,
                mh.ngay_tao if hasattr(mh, "ngay_tao") else ""
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
            # Lấy dữ liệu từ form
            data = {
                "ten_hang": self.name_entry.get(),
                "don_vi": self.unit_var.get(),
                "loai": self.type_entry.get(),
                "mo_ta": self.description_entry.get(),
                "ton_toi_thieu": self.minimum_amount_entry.get(),
                "trang_thai": self.status_var.get(),
                "ngay_tao": datetime.now(),
            }

            # Validate input
            if not data["ten_hang"]:
                messagebox.showwarning("Cảnh báo", "Tên hàng không được để trống!")
                return

            # Gọi controller để thêm mặt hàng mới
            ma_hang = self.controller.add_mat_hang(data)
            print(">>> Thêm mặt hàng thành công:", data)
            # Thêm vào TreeView
            self.tree.insert("", "end", values=(
                ma_hang,
                data["ten_hang"],
                data["don_vi_tinh"],
                data["loai_hang"],
                data["mo_ta"],
                data["ton_toi_thieu"],
                data["trang_thai"],
                data["ngay_tao"].strftime("%Y-%m-%d %H:%M:%S")
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
            data = {
                "ten_hang": self.name_entry.get(),
                "don_vi": self.unit_var.get(),
                "loai": self.type_entry.get(),
                "mo_ta": self.description_entry.get(),
                "ton_toi_thieu": self.minimum_amount_entry.get(),
                "trang_thai": self.status_var.get()
            }

            # Gọi controller/service để update DB
            self.controller.update_mat_hang(ma_hang, data)

            # Cập nhật lại dòng trong TreeView
            self.tree.item(item_id, values=(
                ma_hang,
                data["ten_hang"],
                data["don_vi"],
                data["loai"],
                data["mo_ta"],
                data["ton_toi_thieu"],
                data["trang_thai"],
                values[7]  # giữ nguyên Ngày Tạo cũ
            ))

            messagebox.showinfo("Thành công", "Cập nhật mặt hàng thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cập nhật mặt hàng: {e}")


    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn mặt hàng để xóa.")
            return

        for item in selected:
            values = self.tree.item(item, "values")
            ma_hang = values[0]  # lấy MaHang từ cột đầu tiên
            try:
                # Gọi service để xóa mềm (soft delete)
                self.controller.delete_mat_hang(ma_hang)
                # Xóa khỏi TreeView
                self.tree.delete(item)
                messagebox.showinfo("Thành công", "Xóa mặt hàng thành công.")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể xóa mặt hàng: {e}")

    # def delete_form(self):
    #     self.mssv_entry.delete(0, END)
    #     # Reset combobox major
    #     if self.major_combobox["values"]:
    #         self.major_var.set(self.major_combobox["values"][0])
    #     else:
    #         self.major_var.set("")
    #     self.name_entry.delete(0, END)
    #     self.birthday_entry.delete(0, END)
    #     self.phone_entry.delete(0, END)
    #     self.email_entry.delete(0, END)

    # def update_student(self):
    #   major_name = self.major_var.get()
    #   major_id = self.major_map.get(major_name, "")
    #   try:
    #         birthday = datetime.strptime(self.birthday_entry.get(), "%Y-%m-%d").date()
    #   except Exception:
    #         messagebox.showwarning("Fail format", "Birthday must be format yyyy-mm-dd!")
    #         return

    #   gender = True if self.gender_var.get() == "Male" else False

    #   student_id = self.mssv_entry.get()
    #   if not student_id:
    #         messagebox.showwarning("Notification!", "Please select a student to update!")
    #         return
    #   try:
    #     db = SessionLocal()
    #     controller = StudentController(db)
    #     controller.update_student(
    #         student_id=student_id,
    #         name=self.name_entry.get(),
    #         birthday=birthday,
    #         gender=gender,
    #         email=self.email_entry.get(),
    #         phone=self.phone_entry.get(),
    #         major_id=major_id
    #     )
    #     db.close()
    #     messagebox.showinfo("Success!", "Update student successfully!")
    #     self.load_students()
    #     self.delete_form()
    #   except Exception as e:
    #     messagebox.showerror("Error", f"Error when updating a student:\n{e}")

    # def delete_student(self):
    #   student_id = self.mssv_entry.get()
    #   if not student_id:
    #          messagebox.showwarning("Warning!", "Please select a student to delete!")
    #          return
    #   try:
    #      db = SessionLocal()
    #      controller = StudentController(db)
    #      success = controller.delete_student(student_id)
    #      db.close()
    #      if success:
    #           messagebox.showinfo("Success!", "Delete student successfully!")
    #           self.load_students()
    #           self.delete_form()
    #      else:
    #           messagebox.showwarning("Fail!", f"Student ID {student_id} does not exist!")
    #   except Exception as e:
    #      messagebox.showerror("Error", f"Error when deleting a student:\n{e}")

    # def on_tree_select(self, event):
    #   selected = self.tree.focus()
    #   if not selected:
    #         return
    #   values = self.tree.item(selected, "values")
    #   # Đổ dữ liệu lên form
    #   self.mssv_entry.delete(0, END)
    #   self.mssv_entry.insert(0, values[0])

    #   # Major: tìm tên ngành từ id
    #   major_id = values[1]
    #   major_name = ""
    #   for name, id_ in self.major_map.items():
    #         if id_ == major_id:
    #               major_name = name
    #               break
    #   self.major_var.set(major_name)

    #   self.name_entry.delete(0, END)
    #   self.name_entry.insert(0, values[2])

    #   self.birthday_entry.delete(0, END)
    #   self.birthday_entry.insert(0, values[3])

    #   self.gender_var.set(values[4])

    #   self.phone_entry.delete(0, END)
    #   self.phone_entry.insert(0, values[5])

    #   self.email_entry.delete(0, END)
    #   self.email_entry.insert(0, values[6])