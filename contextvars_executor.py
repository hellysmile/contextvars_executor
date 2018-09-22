import contextvars
import typing
from concurrent.futures import Future, ThreadPoolExecutor
from functools import partial

__version__ = '0.0.1'


class ContextVarExecutor(ThreadPoolExecutor):

    def submit(self, fn: typing.Callable, *args, **kwargs) -> Future:
        ctx = contextvars.copy_context()  # type: contextvars.Context

        return super().submit(partial(ctx.run, partial(fn, *args, **kwargs)))
