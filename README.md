# Guanaco
Guanaco Spanish finetuned LLaMA Model like ChatGPT

The purpose of this repository is to disseminate the process and resources we employed to refine our adaptation of the LLaMA model.

This model is intended solely for research applications and must not be utilized for commercial or entertainment purposes.

## Refereces 
These achievements were made possible due to the solid foundation laid by others in the field. My work is primarily based on the efforts of the following groups and individuals:
[LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), 
[Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), 
[Alpaca Lora](https://github.com/tloen/alpaca-lora), 
[ChatGPT](https://openai.com/blog/chatgpt) and [Hugging Face](https://huggingface.co/).. I am grateful for their exceptional work and for making it accessible to everyone!

## Data
The Dataset I converted the alpaca_data.json file to Spanish. For more information about the dataset's construction, please visit: Stanford Alpaca.

## Finetuning
Fine-tuning Process To fine-tune the LLaMA model, I employed the code provided by Alpaca Lora and Fabric, which offers a method for fine-tuning the LLaMA model utilizing PEFT from Hugging Face. 

This allowed us to execute the fine-tuning stage using a two A6000 locally, building upon LLaMA-7B, 13 and 30. After training for several hours, I was impressed by the remarkable outcomes. 

There were different translations, using translate.ggogle.com. MS Word and ChatGPT, plus all the prompts I use on my membership with ChatGPT-4

anyone that will want to help on this proect please write me.

## Example outputs

Alpaca de Stanford:
```
Instrucción: Inventa una excusa creativa para  decir que no necesito ir a la fiesta. 
Respuesta: Necesito concentrarme en un trabajo importante para mí, así que  no  puedo ir a la fiesta.
```

Guanaco:
```
Instrucción: Inventa una excusa creativa para  decir que no necesito ir a la fiesta. 
Respuesta: "Necesito quedarme en casa para cuidar de mis mascotas". 
```
Alpaca de Stanford:
```
Instrucción: ¿Cómo puedo comenzar mi carrera como científico de datos?  Escriba en forma de lista.
Respuesta:
1. Comience  por especializarse en un campo específico, como big data, computación, bioinformática o estadística.
2. Obtener  el diploma  en un programa de grado relacionado con  la ciencia de datos,  como informática, matemáticas o estadística. 
3. Obtener experiencia práctica a través de pasantías o  proyectos en empresas o instituciones. 
4. Mejore su resumen  y  currículum con resultados relevantes y  experiencia laboral relacionada  .
5. Lea artículos, libros y actualizaciones sobre  ciencia de datos.
6. Crea un portafolio de proyectos y experimentos que hayas realizado.
7. Recibir  el certificado  de calificación mmm en alguna área  de la ciencia de datos.
8. Trate de ponerse en contacto con profesionales en el campo para hablar sobre  oportunidades de trabajo.
9. Acceder a redes sociales, como LinkedIn, para encontrar trabajo y conexiones.
10. Continué mi formación actualizándome  con tecnologías y herramientas de ciencia de datos  .
```

Guanaco:
```
Instrucción: ¿Cómo puedo comenzar una carrera como científico de datos?  Escriba en forma de lista.
Respuesta: 
1. Obtenga una maestría en  ciencia de datos o  ingeniería de datos.
2. Encuentra un trabajo como científico de datos o  ingeniero de  datos.
3. Conoce las principales herramientas de análisis de datos   como Python, R y SQL.
4. Conozca las principales  técnicas de análisis de datos  ,  como  la regresión lineal, la regresión logística   y el análisis de agrupamiento.
5. Aprenda sobre  los enfoques  de análisis de datos clave,  como  el análisis  exploratorio,   el análisis de asociación y el análisis de regresión.
6. Obtenga información sobre las principales herramientas de visualización de datos  ,  como Tableau, QlikView y Power BI.
7. Aprenda sobre  los enfoques  de análisis de datos clave,  como   el análisis de asociación,  el análisis de regresión y el análisis exploratorio.


