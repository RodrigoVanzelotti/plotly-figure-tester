import pytest
from plotly_figure_tester import PlotlyFigureTester

def test_run_server():
    tester = PlotlyFigureTester(debug=False)
    # You can use mocking or subprocesses to test the server without actually running it
    assert tester.host == "127.0.0.1"
    assert tester.port == 8050