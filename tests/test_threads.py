import contextvars

ctx = contextvars.ContextVar('asyncio')  # type: contextvars.ContextVar


def test_basic(executor):
    ctx.set(42)

    def sync():
        return ctx.get()

    fut = executor.submit(sync)

    assert fut.result() == 42
