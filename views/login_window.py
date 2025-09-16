from tkinter import *
from controllers.login_controller import LoginController
from utils import theme   # import nguyên module để dễ cập nhật
from PIL import Image, ImageTk

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Manage Student - Login")
        self.master.resizable(False, False)

        self.theme = theme.CURRENT_THEME

        # Main Frame
        self.frame = Frame(self.master, bg = self.theme["bg_color"])
        self.frame.pack(fill=BOTH, expand= True)

        #Load icon
        sun_img = Image.open("assets/sun.png").resize((24, 24), Image.Resampling.LANCZOS)
        moon_img = Image.open("assets/moon.png").resize((24, 24), Image.Resampling.LANCZOS)
        banner_img = Image.open("assets/banner.png").resize((300, 200), Image.Resampling.LANCZOS)

        self.banner = ImageTk.PhotoImage(banner_img)
        self.sun_icon = ImageTk.PhotoImage(sun_img)
        self.moon_icon = ImageTk.PhotoImage(moon_img)

        # Button to change theme (icon 🌞 / 🌙)
        self.toggle_button = Button(
            self.frame, image=self.moon_icon,  # mặc định LIGHT -> hiện icon moon
            bg=self.theme["button_color"], fg=self.theme["button_text"],
            command=self.toggle_theme, borderwidth=0, highlightthickness=0,
            activebackground=self.theme["button_color"]
        )
        self.toggle_button.pack(anchor="ne", padx=10, pady=10)

        # Title
        self.title_lable = Label(
            self.frame,
            text= "Manage Student Login",
            font =("Arial", 16, "bold"),
            bg = self.theme["bg_color"], fg = self.theme["text_color"]
        )
        self.title_lable.pack(pady=20)

        #Banner
        self.banner_lable = Label(
            self.frame,
            image=self.banner,
            bg=self.theme["bg_color"],
            fg = self.theme["entry_fg"]

        )
        self.banner_lable.pack(fill="x")

        #Error infor
        self.message_label = Label(self.frame, text="", bg=self.theme["bg_color"],
                                   fg=self.theme["error_color"], font=("Arial", 10))
        self.message_label.pack(pady=5)

        #Username
        self.user_label = Label(
            self.frame,
            text="Username: ",
            bg=self.theme["bg_color"],
            fg=self.theme["text_color"],
            font=("Arial", 12)
        )
        self.user_label.pack(pady=(5))

        self.username = Entry(
            self.frame,
            font=("Arial", 12),
            width= 25,
            bd=2,
            relief="solid",
            bg=self.theme["entry_bg"], 
            fg = self.theme["entry_fg"]
        )
        self.username.pack()

        #Password
        self.pass_label = Label(
            self.frame, 
            text="Password:", 
            bg=self.theme["bg_color"], 
            fg=self.theme["text_color"], 
            font=("Arial", 12))
        self.pass_label.pack(pady=(15, 5))

        self.password = Entry(
            self.frame, 
            font=("Arial", 12), 
            width=25, bd=2, 
            relief="solid",
            show="*", 
            bg=self.theme["entry_bg"], 
            fg=self.theme["entry_fg"])
        self.password.pack()

        #Login Button
        self.login_button = Button(
            self.frame,
            text="Login",
            font=("Arial", 12, "bold"),
            bg=self.theme["button_color"], fg=self.theme["button_text"],
            activebackground=self.theme["highlight"],
            activeforeground="white",
            width=15, height=1,
            command=self.login
        )
        self.login_button.pack(pady=20)

      

    def toggle_theme(self):
        """Change theme LIGHT <-> DARK"""
        if theme.CURRENT_THEME == theme.LIGHT_THEME:
            theme.CURRENT_THEME = theme.DARK_THEME
            self.toggle_button.config(image=self.sun_icon)  # nếu đang dark thì hiện mặt trời
        else:
            theme.CURRENT_THEME = theme.LIGHT_THEME
            self.toggle_button.config(image= self.moon_icon)  # nếu đang light thì hiện mặt trăng

        self.theme = theme.CURRENT_THEME
        self.apply_theme()
    
    def apply_theme(self):        
        #Update again all colors above on new theme
        self.frame.config(bg=self.theme["bg_color"])
        self.title_lable.config(bg=self.theme["bg_color"], fg=self.theme["text_color"])
        self.user_label.config(bg=self.theme["bg_color"], fg=self.theme["text_color"])
        self.pass_label.config(bg=self.theme["bg_color"], fg=self.theme["text_color"])
        self.username.config(bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.password.config(bg=self.theme["entry_bg"], fg=self.theme["entry_fg"])
        self.login_button.config(bg=self.theme["button_color"], fg=self.theme["button_text"],
                                 activebackground=self.theme["highlight"])
        self.message_label.config(bg=self.theme["bg_color"], fg=self.theme["error_color"])

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if LoginController.authenticate(username, password):
            self.frame.destroy()
            # from views.main_window import MainWindow
            # MainWindow(self.master)            
            # from views.student_window import StudentWindow
            # StudentWindow(self.master)
        else:
            self.message_label.config(text="❌ Login failed! Please try again.")
