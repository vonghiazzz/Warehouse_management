from tkinter import *
from tkinter import ttk
from utils import theme
# from controllers.nhapkho_controller import NhapKhoController
# from models.database import SessionLocal
# from controllers.major_controller import MajorController
from tkinter import messagebox
from datetime import datetime


class NhapKhoWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Quản Lý Kho")
        self.master.resizable(True, True)

        # Lấy danh sách mat hang
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

        form = Frame(self.frame, bg=self.theme["bg_color"])
        form.pack(fill=X, pady=5)

        Label(
            form,
            text="Mã hàng:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=0, column=0, pady=2)
        self.mahang_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.mahang_entry.grid(row=0, column=1, pady=2)

        # Thay Entry bằng Combobox cho ID Major
        # Label(
        #     form,
        #     text="ID Major:",
        #     width=15,
        #     anchor="w",
        #     bg=self.theme["bg_color"],
        #     fg=self.theme["text_color"],
        # ).grid(row=1, column=0, pady=2)
        # self.major_var = StringVar()
        # self.major_combobox = ttk.Combobox(
        #     form, textvariable=self.major_var, width=28, state="readonly"
        # )
        # self.major_combobox["values"] = list(self.major_map.keys())
        # self.major_combobox.grid(row=1, column=1, pady=2)
        # if majors:
        #     self.major_combobox.current(0)

        Label(
            form,
            text="Số lượng:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=1, column=0, pady=2)
        self.amount_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.amount_entry.grid(row=1, column=1, pady=2)

        Label(
            form,
            text="Giá nhập:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=2, column=0, pady=2)
        self.price_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.price_entry.grid(row=2, column=1, pady=2)

        Label(
            form,
            text="Nhà cung cấp:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=3, column=0, pady=2)
        self.suplier_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.suplier_entry.grid(row=3, column=1, pady=2)

        Label(
            form,
            text="Note:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=4, column=0, pady=2)
        self.suplier_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.suplier_entry.grid(row=4, column=1, pady=2)
        
        Label(
            form,
            text="Nhân viên nhập:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=0, column=4, pady=2, padx=(40, 0))
        self.staff_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.staff_entry.grid(row=0, column=5, pady=2)

        Label(
            form,
            text="Hạn sử dụng:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=1, column=4, pady=2, padx=(40, 0))
        self.expiry_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.expiry_entry.grid(row=1, column=5, pady=2)


        Label(
            form,
            text="Số hóa đơn:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=2, column=4, pady=2, padx=(40, 0))
        self.bill_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.bill_entry.grid(row=2, column=5, pady=2)


        Label(
            form,
            text="Ghi chú:",
            width=15,
            anchor="w",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
        ).grid(row=3, column=4, pady=2, padx=(40, 0))
        self.note_entry = Entry(
            form, width=30, bg=self.theme["entry_bg"], fg=self.theme["entry_fg"]
        )
        self.note_entry.grid(row=3, column=5, pady=2)

      # Tạo frame chứa nút
        button_frame = Frame(form, bg=self.theme["bg_color"])
        button_frame.grid(row=4, column=6, pady=10, sticky="e")

        Button(
            button_frame,
            text="Delete",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=5,
            command='',
            ).pack(side=RIGHT, padx=2)

        Button(
            button_frame,
            text="Update",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=5,
            command='',
            ).pack(side=RIGHT, padx=2)

        Button(
            button_frame,
            text="Save",
            bg=self.theme["button_color"],
            fg=self.theme["button_text"],
            width=5,
            command='',
            ).pack(side=RIGHT, padx=2)

        # Thêm bảng hiển thị danh sách sinh viên
        columns = (
            "ID",
            "Mã Hàng",
            "Ngày",
            "Số lượng",
            "Giá Nhập",
            "Cung cấp",
            "Nhân Viên",
            "Hạn Sử Dụng",
            "Số Hóa Đơn",
            "Ghi Chú",
        )
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=75, anchor="center")
        self.tree.pack(fill=BOTH, expand=True, pady=10)
        # self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.load_students()

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

    def open_mat_hang(self):
        self.frame.destroy()
        from views.mathang_window import MatHangWindow

        MatHangWindow(self.master)

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