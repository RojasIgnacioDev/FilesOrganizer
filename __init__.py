from core.application import Application

from core.serialization import Serializer

if __name__ == "__main__":
    Serializer().create_default_config()
    app = Application()
    app.mainloop()