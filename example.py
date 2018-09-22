import asyncio
import contextvars

from contextvars_executor import ContextVarExecutor

ctx = contextvars.ContextVar('42')


def thread():
    ret = ctx.get()

    assert ret == 42

    return ret


async def main(*, loop):
    ctx.set(42)

    ret = await loop.run_in_executor(None, thread)

    assert ret == 42


loop = asyncio.get_event_loop()
loop.set_default_executor(ContextVarExecutor())
loop.run_until_complete(main(loop=loop))
