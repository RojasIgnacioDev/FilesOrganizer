from core.application import Application

from core.serialization import Serializer

if __name__ == "__main__":
    serializer = Serializer()
    if not serializer.user_config_exists():
        serializer.create_user_config()
        serializer.reset_user_config()
    
    app = Application()
    app.mainloop()