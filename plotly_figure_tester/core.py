import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc

import plotly.express as px
import plotly.graph_objects as go

import os

class PlotlyFigureTester:
    """
    A class to test Plotly figures and run a server for visualization.

    Attributes:
        debug (bool): Whether to run the server in debug mode. Defaults to True.
        figures (list): A list of tuples containing figures and their labels.
    """

    def __init__(self):
        """
        Initialize the PlotlyFigureTester with default settings.
        """
        self.debug = True  # Default debug mode is True
        self.figures = []  # Store figures and their labels
        self.stylesheets = []  # Store CSS stylesheets

    #     self._add_default_styles()

    # def _add_default_styles(self):
    #     """
    #     Add the default CSS file from the assets folder.
    #     """
    #     # Path to the default CSS file
    #     assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    #     default_css = os.path.join(assets_dir, "default.css")

    #     if os.path.exists(default_css):
    #         self.stylesheets.append(default_css)
    #     else:
    #         raise FileNotFoundError(f"Default CSS file not found: {default_css}")

    def add_chart(self, figure, label: str):
        """
        Add a Plotly figure to the layout with a label.

        Args:
            figure: A Plotly figure object.
            label (str): The label for the figure.
        """
        self.figures.append((figure, label))

    def add_stylesheet(self, stylesheet: str):
        """
        Add a CSS stylesheet to the server.

        Args:
            stylesheet (str): The path or URL to the CSS file.
        """
        self.stylesheets.append(stylesheet)

    def run_server(self, host: str = "127.0.0.1", port: int = 2802):
        """
        Run a server to visualize Plotly figures.

        Args:
            host (str): The host address to run the server on. Defaults to "127.0.0.1".
            port (int): The port to run the server on. Defaults to 2802.

        Raises:
            ValueError: If the host is not a valid IP address or the port is out of range.
        """
        # Validate host
        if not self._is_valid_host(host):
            raise ValueError(f"Invalid host: {host}. Must be a valid IP address or 'localhost'.")

        # Validate port
        if not self._is_valid_port(port):
            raise ValueError(f"Invalid port: {port}. Must be between 1024 and 65535.")

        # If valid, run the server
        self._start_server(host, port)

    def _is_valid_host(self, host: str) -> bool:
        """
        Check if the host is a valid IP address or 'localhost'.

        Args:
            host (str): The host address to validate.

        Returns:
            bool: True if the host is valid, False otherwise.
        """
        if host == "localhost":
            return True
        try:
            import ipaddress
            ipaddress.ip_address(host)
            return True
        except ValueError:
            return False

    def _is_valid_port(self, port: int) -> bool:
        """
        Check if the port is within the valid range (1024-65535).

        Args:
            port (int): The port number to validate.

        Returns:
            bool: True if the port is valid, False otherwise.
        """
        return 1024 <= port <= 65535

    def _start_server(self, host: str, port: int):
        """
        Start the Dash server with the given host and port.

        Args:
            host (str): The host address to run the server on.
            port (int): The port to run the server on.
        """

        # Initialize the Dash app
        app = dash.Dash(
            'FigureTester'
        )

        app.layout = dmc.MantineProvider(
            dmc.Container([
                dmc.Title('Figure Tester', size="h1", mb=20),
                dmc.Grid(id='figure-container', children=[]),  # Placeholder for dynamic content
            ], fluid=True)
        )


        # Callback to dynamically update the layout
        @app.callback(
            Output('figure-container', 'children'),
            [Input('figure-container', 'id')]
        )
        def update_layout(_):
            children = []
            for figure, label in self.figures:
                children.append(
                    dmc.Col(
                        self._wrap_figure(figure, label),
                        span=12
                    )
                )
            return children

        # Run the server
        app.run_server(host=host, port=port, debug=self.debug)

    def _wrap_figure(self, figure: go.Figure, label: str) -> dmc.Paper:
        button_section = dmc.Stack(
            [
                dmc.Button("Button 1", fullWidth=True, size="md", style={"marginBottom": 10}),
                dmc.Button("Button 2", fullWidth=True, size="md", style={"marginBottom": 10}),
                dmc.Button("Button 3", fullWidth=True, size="md"),
            ],
            align="stretch",  # Ensures buttons stretch to fill the width
            spacing="md",     # Adds spacing between buttons
        )

        layout = dmc.Paper(
            [
                dmc.Grid([
                    dmc.Col(
                        dmc.Text(label, size="xl", mb=10),
                        span=12
                    ),
                    dmc.Col(
                        dcc.Graph(figure=figure),
                        span=9
                    ),
                    dmc.Col(
                        button_section,
                        span=3
                    )
                ])
            ],
            withBorder=True,
            shadow="sm",
            p="md",
            radius="md",
        )

        return layout
