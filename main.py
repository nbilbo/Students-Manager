from app.view.application import Application
from app.controller.application_controller import ApplicationController


if __name__ == '__main__':
    application = Application()
    controller = ApplicationController(application)
    application.mainloop()
    controller.close()
