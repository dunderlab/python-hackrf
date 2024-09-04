from hackrf.scan import ScanHackRF
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def main():
    scanhackrf = ScanHackRF(0)
    await scanhackrf.scan(
        freqs=[
            (80, 160),
        ],
        sample_rate=20e6,
        step_width=10e6,
        step_offset=5e6,
        read_num_blocks=1,
        buffer_num_blocks=1,
        callback=None,
    )


asyncio.run(main())
