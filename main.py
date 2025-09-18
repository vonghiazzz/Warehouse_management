from tkinter import Tk
from views.login_window import LoginWindow
from PIL import Image, ImageTk
# from models.database import Base, engine
# from models import major, student

def main():
    root=Tk()
    root.title("Warehouse management")

    print("📦 Creating database tables...")
    # Base.metadata.create_all(bind=engine)


    #Setup width and height
    window_width = 800
    window_height = 600

    # Get width and height of screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to place the window
    x = (screen_width - window_width)//2
    y = (screen_height - window_height)//2-40

    # Setup window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    #Run login page
    LoginWindow(root)

    # Load icon by Pillow to resize
    icon_img = Image.open("assets/banner.png").resize((40,40), Image.Resampling.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_img)


    # Set icon into title bar
    root.iconphoto(False, icon_photo)

    root.mainloop()

if __name__ == "__main__":
    main()