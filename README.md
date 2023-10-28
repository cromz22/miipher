# Miipher

This repository proviedes unofficial implementation of the speech restoration model Miipher ([Koizumi et al., 2023](https://arxiv.org/abs/2303.01664)).
Please note that the model provided in this repository doesn't represent the performance of the original model proposed by Koizumi et al. as this implementation differs in many ways from the paper.

## Installation

This repository uses [rye](https://github.com/mitsuhiko/rye) as the Python package manager.
Run the following commands to install the dependencies:

```
rye pin 3.10
rye sync
```

## Pretrained model

The pretrained model is trained on [LibriTTS-R](http://www.openslr.org/141/) and [JVS corpus](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus), and provided in **CC-BY-NC-2.0 license**.

The models are hosted on [huggingface](https://huggingface.co/spaces/Wataru/Miipher/)

To use pretrained model, please refere to `examples/demo.py`

## Differences from the original paper

| | [original paper](https://arxiv.org/abs/2303.01664) | This repo |
|---|---|---|
| Clean speech dataset | proprietary | [LibriTTS-R](http://www.openslr.org/141/) and [JVS corpus](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus) |
| Noise dataset |  TAU Urban Audio-Visual Scenes 2021 dataset | TAU Urban Audio-Visual Scenes 2021 dataset and Slakh2100 |
| Speech SSL model | [W2v-BERT XL](https://arxiv.org/abs/2108.06209) | [WavLM-large](https://arxiv.org/abs/2110.13900) |
| Language SSL model | [PnG BERT](https://arxiv.org/abs/2103.15060) | [XPhoneBERT](https://github.com/VinAIResearch/XPhoneBERT) |
| Feature cleaner building block | [DF-Conformer](https://arxiv.org/abs/2106.15813) | [Conformer](https://arxiv.org/abs/2005.08100) |
| Vocoder | [WaveFit](https://arxiv.org/abs/2210.01029) | [HiFi-GAN](https://arxiv.org/abs/2010.05646) |
| X-Vector model | Streaming Conformer-based speaker encoding model | [speechbrain/spkrec-xvect-voxceleb](https://huggingface.co/speechbrain/spkrec-xvect-voxceleb) |

## LICENSE

Code in this repo: MIT License

Weights on huggingface: CC-BY-NC-2.0 license

