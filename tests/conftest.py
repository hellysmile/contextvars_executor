import asyncio
import gc
import os

import pytest

from contextvars_executor import ContextVarExecutor

asyncio.set_event_loop(None)  # type: ignore


@pytest.fixture
def event_loop(request):
    loop = asyncio.new_event_loop()
    loop.set_debug(bool(os.environ.get('PYTHONASYNCIODEBUG')))

    yield loop

    loop.run_until_complete(loop.shutdown_asyncgens())

    loop.call_soon(loop.stop)
    loop.run_forever()
    loop.close()

    gc.collect()
    gc.collect()  # for pypy


@pytest.fixture
def loop(event_loop, request):
    asyncio.set_event_loop(None)
    event_loop.set_default_executor(None)
    request.addfinalizer(lambda: asyncio.set_event_loop(None))  # type: ignore
    request.addfinalizer(lambda: event_loop.set_default_executor(None))  # type: ignore # noqa

    return event_loop


@pytest.fixture
def executor(request):
    e = ContextVarExecutor()

    yield e

    e.shutdown(wait=True)
