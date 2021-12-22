from git_portfolio import __all__
from git_portfolio import __version__

def test_all():
	assert __all__ is not None

def test_version():
    assert __version__ == '0.1.0'
