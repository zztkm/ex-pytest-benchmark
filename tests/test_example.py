import pytest

from something import dosomething


def test_dosomething():
    ret = dosomething()
    assert ret


def test_dosomething_benchmark_quick(benchmark):
    ret = benchmark(dosomething, duration=0.01)
    assert ret


def test_dosomething_benchmark_slow(benchmark):
    ret = benchmark(dosomething, duration=1.0)
    assert ret


if __name__ == "__main__":
    pytest.main(["-v", __file__])
