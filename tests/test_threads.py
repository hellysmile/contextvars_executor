import contextvars

ctx = contextvars.ContextVar('asyncio')  # type: contextvars.ContextVar


def test_basic(executor):
    ctx.set(42)

    def sync():
        return ctx.get()

    fut = executor.submit(sync)

    assert fut.result() == 42


def test_kwargs(executor):
    ctx.set(42)

    def sync(*, foo):
        assert ctx.get() == 42

        return foo

    fut = executor.submit(sync, foo=42)

    assert fut.result() == 42
