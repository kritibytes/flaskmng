from click.testing import CliRunner
from .__main__ import main

def test_start_project():
    runner = CliRunner()
    result = runner.invoke(main,["startproject"])
    assert "STARTING PROJECT" in result.output
    assert result.exit_code == 0

def test_new_app():
    runner = CliRunner()
    result = runner.invoke(main,["newapp"])
    assert "NEW APP" in result.output
    assert result.exit_code == 0
