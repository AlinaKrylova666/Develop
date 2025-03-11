import pytest
from src.decorators import log

@log()
def successful_function(x, y):
    return x + y

@log()
def failing_function(x, y):
    return x / y

def test_successful_function(capsys):
    result = successful_function(3, 4)
    assert result == 7
    captured = capsys.readouterr()
    assert "successful_function ok" in captured.err  # Изменено на captured.err

def test_failing_function(capsys):
    with pytest.raises(ZeroDivisionError):
        failing_function(3, 0)
    captured = capsys.readouterr()
    assert "failing_function error: division by zero" in captured.err  # Изменено на captured.err

def test_logging_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file)
    def test_func(a, b):
        return a * b

    test_func(2, 3)

    with open(log_file) as f:
        log_contents = f.read()
        assert "test_func ok" in log_contents

# Запуск тестов через командную строку
if __name__ == "__main__":
    pytest.main()
