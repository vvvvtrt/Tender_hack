from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast
import torch


def spell_text(raw_text):
    MODEL_NAME = 'UrukHan/t5-russian-spell'
    MAX_INPUT = 256

    tokenizer = T5TokenizerFast.from_pretrained("UrukHan/t5-russian-spell")
    model = AutoModelForSeq2SeqLM.from_pretrained("UrukHan/t5-russian-spell")

    input_sequences = raw_text

    task_prefix = "Spell correct: "
    if type(input_sequences) != list: input_sequences = [input_sequences]

    encoded = tokenizer(
        [task_prefix + sequence for sequence in input_sequences],
        padding="longest",
        max_length=MAX_INPUT,
        truncation=True,
        return_tensors="pt",
    )

    device = torch.device('cpu')
    predicts = model.generate(**encoded.to(device))

    return tokenizer.batch_decode(predicts, skip_special_tokens=True)[0]