from click.testing import CliRunner
from flaskmng.__main__ import main
import os
runner = CliRunner()

def test_start_project():
    os.chdir('test')
    open('hello.txt','w')
    result = runner.invoke(main,["startproject"],input="hello-world\n\n\n\n\n")
    assert result.exit_code == 0
