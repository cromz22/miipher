import argparse
from miipher.dataset.preprocess_for_infer import PreprocessForInfer
from miipher.lightning_module import MiipherLightningModule
from lightning_vocoders.models.hifigan.xvector_lightning_module import (
    HiFiGANXvectorLightningModule,
)
import torch
import torchaudio
import hydra


@torch.inference_mode()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-wav-path', type=str, required=True, help='path to input wav file')
    parser.add_argument('--transcript', type=str, default="", help='transcript of the audio, if available')
    parser.add_argument('--lang-code', type=str, default="eng-us", help='language code of the transcript, when you use transcript')  # TODO: check if lang_code is necessary
    parser.add_argument("--output-wav-path", type=str, default="output.wav", help="path to output wav file")
    args = parser.parse_args()

    assert args.lang_code in {"eng-us", "jpn"}, "lang_code must be either eng-us or jpn"

    miipher_path = "https://huggingface.co/spaces/Wataru/Miipher/resolve/main/miipher.ckpt"
    miipher = MiipherLightningModule.load_from_checkpoint(miipher_path, map_location="cpu")
    vocoder = HiFiGANXvectorLightningModule.load_from_checkpoint(
            "https://huggingface.co/spaces/Wataru/Miipher/resolve/main/vocoder_finetuned.ckpt",
            map_location="cpu",
            )
    xvector_model = hydra.utils.instantiate(vocoder.cfg.data.xvector.model)
    xvector_model = xvector_model.to("cpu")
    preprocessor = PreprocessForInfer(miipher.cfg)

    wav, sr = torchaudio.load(args.input_wav_path)
    batch = preprocessor.process(
        basename="test",
        degraded_audio_tuple=(wav, sr),
        word_segmented_text=args.transcript,
        lang_code=args.lang_code,
    )
    (
        phone_feature,
        speaker_feature,
        degraded_ssl_feature,
        _,
    ) = miipher.feature_extractor(batch)
    cleaned_ssl_feature, _ = miipher(
        phone_feature, speaker_feature, degraded_ssl_feature
    )
    vocoder_xvector = xvector_model.encode_batch(
        batch["degraded_wav_16k"].cpu()
    ).squeeze(1)
    cleaned_wav = vocoder.generator_forward(
        {"input_feature": cleaned_ssl_feature, "xvector": vocoder_xvector}
    )[0]

    with open(args.output_wav_path, "wb") as fp:
        torchaudio.save(fp, cleaned_wav, sample_rate=22050, format="wav")


if __name__ == '__main__':
    main()
