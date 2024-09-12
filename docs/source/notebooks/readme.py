# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] editable=true slideshow={"slide_type": ""}
# # Python HackRF

# %% [markdown]
# ## Installation Instructions
#
# To install the required dependencies for this project, you can use the following command:
#
# ```bash
# pip install libhackrf
# ```

# %% [markdown]
# ## Why this package?
#
# The HackRF device is designed for software-defined radio applications, providing a versatile platform for experimentation and development. This package facilitates easy access to its functionality, allowing users to quickly implement and test their ideas.
#
# - Supports a wide range of frequencies
# - Compatible with various software frameworks
# - Ideal for educational purposes and research
# %% [markdown] editable=true slideshow={"slide_type": ""}
# ## Sweep Scanning
#
# This package implements sweep scanning effectively, allowing users to specify frequency bands, sample rates, and step widths for scanning radio frequencies. The asynchronous scanning process captures filtered data, enabling real-time analysis and visualization of signals across the specified frequency ranges.
#
# Users can define custom callback functions to process the scanned data, providing flexibility for different applications, whether for educational purposes, signal detection, or research.

# %% [markdown] editable=true slideshow={"slide_type": ""}
# ![Sweep Scanning](_images/sweep.png "Sweep Scanning")

# %% [markdown] editable=true slideshow={"slide_type": ""}
# For example, to configure FM scanning, you can use the following setup:

# %% [markdown] editable=true slideshow={"slide_type": ""}
# ![Sweep Scanning](_images/sweepFM.png "Sweep Scanning")

# %% [markdown] editable=true slideshow={"slide_type": ""}
# This configuration allows you to scan the FM broadcast band from 88 MHz to 108 MHz, with a sample rate of 8 MHz, stepping 2 MHz at a time. The `step_offset` can be adjusted as needed for specific scenarios.
