import asyncio
from asyncio import get_running_loop, AbstractEventLoop, Task

class Monitor:
    # lag: float = 0
    num_active_tasks: float = 0

    def __init__(self, interval: float = 0.25):
        self._interval = interval
        self._lag = 0

    @property
    def interval(self):
        return self._interval
    
    @interval.setter
    def interval(self, new_value: float):
        self._interval = new_value

    @property
    def lag(self):
        return self._lag
    
    @lag.setter
    def lag(self, new_value: float):
        self._lag = new_value

    def start(self):
        loop = get_running_loop()
        loop.create_task(self._monitor_loop(loop))
    
    async def _monitor_loop(self, loop: AbstractEventLoop):
        while loop.is_running():
            start = loop.time()
            # sideffect, self._interval might be changed while this is running
            # maybe that's good
            await asyncio.sleep(self._interval)
            time_slept = loop.time() - start
            # TODO: push this lag into a monitoring system
            self._lag = time_slept - self._interval

            # monitor the number of active tasks
            tasks = [t for t in Task.all_tasks(loop) if not t.done()]
            self.num_active_tasks = len(tasks)