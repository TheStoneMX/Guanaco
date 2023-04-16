# Guanaco
Guanaco Spanish finetuned LLaMA Model like ChatGPT


The purpose of this repository is to disseminate the process and resources we employed to refine our adaptation of the LLaMA model.
This model is intended solely for research applications and must not be utilized for commercial or entertainment purposes.
These achievements were made possible due to the solid foundation laid by others in the field. Our work is primarily based on the efforts of the following groups and individuals: LLaMA, Stanford Alpaca, Alpaca Lora, ChatGPT, Cabrita, and Hugging Face. We are grateful for their exceptional work and for making it accessible to everyone!

The Dataset We converted the alpaca_data.json file to Spanish using ChatGPT-4 . For more information about the dataset's construction, please visit: Stanford Alpaca.

Fine-tuning Process To fine-tune the LLaMA model, we employed the code provided by Alpaca Lora and Fabric, which offers a method for fine-tuning the LLaMA model utilizing PEFT from Hugging Face. 

This allowed us to execute the fine-tuning stage using a single two A6000 locally, building upon LLaMA-7B, 13 and 30. After training for several hours, I was impressed by the remarkable outcomes. 

