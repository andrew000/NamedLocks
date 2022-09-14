import asyncio
import logging
from random import randint, uniform

import pytest

from named_locks import AsyncNamedLock

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

NAMED_LOCK = AsyncNamedLock()


async def _some_task(uid: int):
    async with NAMED_LOCK.lock(uid):
        logger.debug("Task <%s> started" % uid)
        await asyncio.sleep(uniform(0, 3))
        logger.debug("Task <%s> finished" % uid)


@pytest.mark.asyncio
async def test_async_named_lock():
    tasks = []

    for _ in range(100):
        uid = randint(0, 10)
        tasks.append(asyncio.create_task(_some_task(uid)))
        await asyncio.sleep(0.01)

    await asyncio.gather(*[task for task in tasks if not task.done()])
    assert len(NAMED_LOCK._locks) == 0
