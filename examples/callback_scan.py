from hackrf.scan import ScanHackRF
import asyncio
import time


t0 = time.time()


# ----------------------------------------------------------------------
def custom_callback(data_freqs):
    """"""
    global t0
    print(f"{(time.time() - t0) * 1000} ms")
    t0 = time.time()

    print(data_freqs.keys())


async def main():
    scanhackrf = ScanHackRF(0)
    await scanhackrf.scan(
        freqs=[
            # List of frequency tuples (start_freq, end_freq) in MHz
            (100, 140),
        ],
        sample_rate=20e6,  # Sample rate in samples per second (20 million samples per second)
        step_width=20e6,  # Frequency step width in Hz (10 MHz)
        step_offset=None,  # Step offset in Hz (5 MHz from the target frequency)
        read_num_blocks=1,  # Number of blocks to read in each step
        buffer_num_blocks=1,  # Number of blocks to buffer
        callback=custom_callback,  # Optional callback function to process the data
        interleaved=False,
    )


asyncio.run(main())
