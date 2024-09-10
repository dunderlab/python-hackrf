from hackrf.scan import ScanHackRF
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def main():
    scanhackrf = ScanHackRF(0)
    await scanhackrf.scan(
        freqs=[
            # List of frequency tuples (start_freq, end_freq) in MHz
            (80, 160),
        ],
        sample_rate=20e6,  # Sample rate in samples per second (20 million samples per second)
        step_width=10e6,  # Frequency step width in Hz (10 MHz)
        step_offset=5e6,  # Step offset in Hz (5 MHz from the target frequency)
        read_num_blocks=1,  # Number of blocks to read in each step
        buffer_num_blocks=1,  # Number of blocks to buffer
        callback=None,  # Optional callback function to process the data
    )


asyncio.run(main())
