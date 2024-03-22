from core.application import Application
from core.configmanager import ConfigManager

if __name__ == "__main__":
    ConfigManager()
    app = Application()
    app.mainloop()