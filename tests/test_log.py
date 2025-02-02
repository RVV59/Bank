import pytest

from src.decorators import log


def test_my_function_success(capsys):
    '''тестирует, что корректно выводит сообщение "OK" в случае успеха'''

    @log()
    def my_function_test(x, y):
        return x / y

    my_function_test(4, 2)
    captured = capsys.readouterr().out.strip()
    assert "my_function_test OK" in captured


def test_my_function_error(capsys):
    '''проверяет, как декоратор обрабатывает исключения'''

    @log()
    def my_function_test(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function_test(10, 0)

    captured = capsys.readouterr().out.strip()
    assert "my_function_test error:" in captured
    assert "Inputs: (10, 0), {}" in captured


def test_logging_to_file(tmp_path):
    '''проверяет, что декоратор корректно записывает сообщения в файл при наличии аргумента'''
    log_filename = tmp_path / "test.log"

    @log(filename=str(log_filename))
    def my_function_test(x, y):
        return x / y

    my_function_test(20, 5)
    with open(str(log_filename)) as f:
        content = f.read().strip()
    assert "my_function_test OK" in content


def test_logging_to_console(capsys):
    '''проверяет, что декоратор корректно выводит сообщения в консоль, если аргумент filename не передан'''

    @log()
    def my_function_test(x, y):
        return x / y

    my_function_test(30, 15)
    captured = capsys.readouterr().out.strip()
    assert "my_function_test OK" in captured
