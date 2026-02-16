# Independent-LLM-Project

**Independent-LLM-Project** is an open-source research initiative aiming to democratize Large Language Model (LLM) training. It provides a lightweight, modular framework for pre-training and fine-tuning transformer-based models on consumer-grade hardware (e.g., single NVIDIA RTX 3090/4090).

Unlike mainstream frameworks tailored for massive clusters, this project focuses on **memory efficiency**, **local privacy**, and **independent alignment**.

## Core Features

- **Optimized Attention:** Implementation of Flash Attention v2 integration for 3x faster training.
- **Consumer Hardware Focus:** Native support for 4-bit and 8-bit quantization using `bitsandbytes`.
- **Modular Tokenizer:** Custom BPE (Byte-Pair Encoding) implementation supporting multi-lingual datasets.
- **RLHF Pipeline:** Experimental Reinforcement Learning from Human Feedback loop for local alignment.

## Installation

```bash
git clone [https://github.com/KULLANICI_ADIN/Independent-LLM-Project.git](https://github.com/KULLANICI_ADIN/Independent-LLM-Project.git)
cd Independent-LLM-Project
pip install -r requirements.txt (ANL)
