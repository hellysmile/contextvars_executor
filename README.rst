contextvars_executor
====================

:info: contextvars friendly ThreadPoolExecutor

.. image:: https://travis-ci.org/hellysmile/contextvars_executor.svg?branch=master
    :target: https://travis-ci.org/hellysmile/contextvars_executor

.. image:: https://img.shields.io/pypi/v/contextvars_executor.svg
    :target: https://pypi.python.org/pypi/contextvars_executor

.. image:: https://codecov.io/gh/hellysmile/contextvars_executor/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/hellysmile/contextvars_executor

Installation
------------

.. code-block:: shell

    pip install contextvars_executor

Why???
------

* `related Python issue <https://bugs.python.org/issue34014>`_

Usage
-----

.. code-block:: python

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

Python 3.7+ is required, there is no need to support older python versions!!!
