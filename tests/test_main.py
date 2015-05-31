"""Example test."""

from replace_me import main


def test(capsys):
    """Example test."""
    main()
    stdout, stderr = capsys.readouterr()
    assert 'Hello World!\n' == stdout
    assert not stderr
