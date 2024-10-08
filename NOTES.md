### Resources
#### Axolotl
- https://github.com/axolotl-ai-cloud/axolotl/blob/main/docs/config.qmd
- https://www.youtube.com/watch?v=mmsa4wDsiy0

#### Modal
- https://modal.com/docs/examples/llm-finetuning

### Issues
#### Empty Inference
Model result is empty when using
``` bash
modal run -q src.inference --prompt "<INSERT PROMPT>"
```
##### Track down request id
The log references a request id. How to access it? May contain the model response

##### Rule out tokenization errors
- https://github.com/axolotl-ai-cloud/axolotl?tab=readme-ov-file#tokenization-mismatch-bw-inference--training
- https://hamel.dev/notes/llm/finetuning/05_tokenizer_gotchas.html
- https://youtu.be/mmsa4wDsiy0?feature=shared&t=1927

##### Adjust Input Format
Likely improvements to be made to formatting prompts (XML like separators).
Formatting in [prep_data.py](src/prep_data.py).

### Ditch Axolotl
Axolotl was used because it is what Modal pushed for finetuning as
part of its tutorial. It is not required to use axolotl. It is worth seeing if the [original training code](https://github.com/kolenaIO/research/pull/168/files) can be adapted to run on Modal's serverless platform.
Example of training without axolotl https://modal.com/docs/examples/slack-finetune
