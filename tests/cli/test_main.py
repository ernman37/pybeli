from click.testing import CliRunner

from pybeli.cli.main import main


def test_main_outputs_welcome() -> None:
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Welcome to PyBeli!" in result.output
