# utils/theme.py

# 🎨 Màu mặc định cho toàn bộ ứng dụng
THEME = {
    "bg_color": "#f3e5ab",      # màu nền chính
    "text_color": "#4b3832",    # màu chữ chính
    "button_color": "#8b5e3c",  # màu nút
    "button_text": "#ffffff",   # chữ trên nút
    "entry_bg": "white",        # nền ô nhập
    "entry_fg": "#333333",      # chữ trong ô nhập
    "highlight": "#d4a373",     # màu nổi bật
    "error_color": "red",       # báo lỗi
    "success_color": "green",   # báo thành công
}

# Font mặc định
FONTS = {
    "title": ("Arial", 16, "bold"),
    "subtitle": ("Arial", 14, "italic"),
    "label": ("Arial", 12),
    "entry": ("Arial", 12),
    "button": ("Arial", 12, "bold"),
    "message": ("Arial", 10),
}


LIGHT_THEME = {
    "bg_color": "#f3e5ab",
    "text_color": "#4b3832",
    "button_color": "#8b5e3c",
    "button_text": "#ffffff",
    "entry_bg": "white",
    "entry_fg": "#333333",
    "highlight": "#d4a373",
    "error_color": "red",
    "success_color": "green",
}

DARK_THEME = {
    "bg_color": "#2e2e2e",
    "text_color": "#f5f5f5",
    "button_color": "#444444",
    "button_text": "#ffffff",
    "entry_bg": "#3c3c3c",
    "entry_fg": "#ffffff",
    "highlight": "#6f4e37",
    "error_color": "red",
    "success_color": "lightgreen",
}

CURRENT_THEME = LIGHT_THEME   # mặc định


