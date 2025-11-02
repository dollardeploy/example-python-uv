from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        H1("Welcome to the Python Example App!"),
        P("This is a simple web server written in Python. It serves this static HTML page. You can use this as a starting point for building more complex web applications."),
        H2("Run with DollarDeploy"),
        P("Deploying and managing this application is easy with DollarDeploy. Connect your server, point DollarDeploy to your code repository, and it handles the build, deployment, and monitoring automatically – no SSH required!")
    )

serve()
