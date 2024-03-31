from core.application import Application
from core.config_manager import ConfigManager

if __name__ == "__main__":
    ConfigManager()
    app = Application()
    app.mainloop()