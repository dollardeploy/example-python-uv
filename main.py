from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Html(
        Head(
            Style("""
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }
                .container {
                    max-width: 800px;
                    padding: 2rem;
                    text-align: center;
                }
                a {
                    color: #0366d6;
                    text-decoration: none;
                    font-size: 1.2rem;
                    font-weight: bold;
                }
                a:hover {
                    text-decoration: underline;
                }
            """)
        ),
        Body(
            Div(
                H1("Welcome to the Python Example App!"),
                P("This is a simple web server written in Python, with FastHTML and uv. It serves this static HTML page. You can use this as a starting point for building more complex web applications."),
                H2("Run with DollarDeploy"),
                P("Deploying and managing this application is easy with DollarDeploy. Connect your server, point DollarDeploy to your code repository, and it handles the build, deployment, and monitoring automatically – no SSH required!"),
                P(A("View on GitHub", href="https://github.com/dollardeploy/example-python-uv/")),
                cls="container"
            )
        )
    )

serve()
