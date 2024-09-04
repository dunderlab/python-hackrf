from hackrf.core import HackRF
import asyncio
import logging


########################################################################
class ScanHackRF(HackRF):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        self.scan_event = asyncio.Event()

    # ----------------------------------------------------------------------
    async def scan(
        self,
        freqs,
        sample_rate=20e6,
        step_width=10e6,
        step_offset=5e6,
        read_num_blocks=1,
        buffer_num_blocks=1,
        callback=None,
    ):
        """"""
        block_size = 16384
        self.sample_rate = sample_rate

        self.start_sweep(
            freqs,
            pipe_function=(self._callback if callback is None else callback),
            step_width=step_width,
            num_bytes=block_size * read_num_blocks,
            step_offset=step_offset,
            interleaved=False,
            buffer_size=block_size * buffer_num_blocks,
        )
        await self.scan_event.wait()

    # ----------------------------------------------------------------------
    def _callback(self, data_freqs):
        """"""
        for freq in data_freqs:
            data = data_freqs[freq]
            logging.debug(
                f"{int(freq / 1e6)} MHz queue has {len(data)} values."
            )
        return self.scan_event.is_set()
