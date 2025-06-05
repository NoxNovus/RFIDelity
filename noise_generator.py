import numpy as np
from tqdm import tqdm

duration = 60  # seconds
sample_rate = 10_000_000  # 10 Msps
chunk_size = 10_000  # number of complex samples per chunk
num_chunks = (duration * sample_rate) // chunk_size

with open("noise.iq", "wb") as f:
    for _ in tqdm(range(num_chunks), desc="Generating IQ noise"):
        # Generate white noise (complex IQ)
        iq = (np.random.randn(chunk_size) + 1j * np.random.randn(chunk_size)) * 0.1

        # Interleave and convert to int8
        iq_interleaved = np.empty(2 * chunk_size, dtype=np.int8)
        iq_interleaved[0::2] = (np.real(iq) * 127).astype(np.int8)
        iq_interleaved[1::2] = (np.imag(iq) * 127).astype(np.int8)

        # Write to file
        iq_interleaved.tofile(f)
