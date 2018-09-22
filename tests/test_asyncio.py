import asyncio
import contextvars

import pytest

pytestmark = pytest.mark.asyncio

ctx = contextvars.ContextVar('asyncio')  # type: contextvars.ContextVar


async def test_basic(loop, executor):

    ctx.set(42)

    def sync():
        return ctx.get()

    ret = await loop.run_in_executor(executor, sync)

    assert ret == 42


async def test_default_executor(loop, executor):

    loop.set_default_executor(executor)

    ctx.set(42)

    def sync():
        return ctx.get()

    ret = await loop.run_in_executor(None, sync)

    assert ret == 42


async def test_future(loop, executor):

    ctx.set(42)

    def sync():
        return ctx.get()

    ret = await asyncio.ensure_future(loop.run_in_executor(executor, sync))

    assert ret == 42


async def test_args(loop, executor):

    ctx.set(42)

    def sync(foo):
        assert ctx.get() == 42

        return foo

    ret = await loop.run_in_executor(executor, sync, 42)

    assert ret == 42
