from core.application import Application

from core.serialization import Serializer

if __name__ == "__main__":
    ser = Serializer()
    ser.create_default_config()
    ser.create_user_config()
    
    app = Application()
    app.mainloop()