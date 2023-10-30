# Miipher

This repository proviedes unofficial implementation of the speech restoration model Miipher ([Koizumi et al., 2023](https://arxiv.org/abs/2303.01664)).
Please note that the model provided in this repository doesn't represent the performance of the original model proposed by Koizumi et al. as this implementation differs in many ways from the paper.

## Installation

To use `miipher` as a package, install the directory with pip.

```
pip install git+https://github.com/cromz22/miipher
```

Alternatively, if you would like to make some changes to the code, clone the repository and use [rye](https://github.com/mitsuhiko/rye) to install the dependencies.

```
git clone git@github.com:cromz22/miipher.git
cd miipher
rye sync
```

By default, this should create `miipher/.venv` and install packages there.
Type `. .venv/bin/activate` to activate the environment.

## Pretrained model

The pretrained model is trained on [LibriTTS-R](http://www.openslr.org/141/) and [JVS](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus) corpora, and provided in **CC-BY-NC-2.0 license**.

The model is hosted on [huggingface](https://huggingface.co/spaces/Wataru/Miipher/).

### Using the pretrained model

If you would like to run the web app:

```
python3 examples/demo.py
```

If you would like to use the model from command line:

```
python3 examples/predict.py --input-wav-path /path/to/input.wav --output-wav-path /path/to/output.wav --transcript "your transcript" --lang-code "eng-us"
```

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

