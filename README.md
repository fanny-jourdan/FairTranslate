# FairTranslate

This repository contains resources, scripts, and notebooks related to the paper:
**"FairTranslate: an English-French Dataset for Gender Bias Evaluation in Machine Translation by Overcoming Gender Binarity"**.

The dataset associated with this research is publicly available on Hugging Face. The repository also includes notebooks for visualizing the experiments conducted in the paper.

---

## 📄 Paper and Dataset

- **Paper**: [FairTranslate: an English-French Dataset for Gender Bias Evaluation in Machine Translation by Overcoming Gender Binarity](https://arxiv.org/abs/2504.15941)
- **Dataset**: The dataset is hosted on Hugging Face and can be accessed here:  
  [![Hugging Face Dataset](https://img.shields.io/badge/Dataset-Hugging%20Face-blue)](https://huggingface.co/datasets/Fannyjrd/FairTranslate_fr)

---

## 📊 Notebooks

This repository provides two Jupyter notebooks that replicate the analysis and visualizations from the paper:


1. [**`Analysis_translation_performance.ipynb`**:](./Analysis_translation_performance.ipynb)
   Visualization and analysis of gender-specific translation performance. 

2. [**`Analysis_inclusive_gender.ipynb`**:](Analysis_inclusive_gender.ipynb)
   Analyzes the translation of gendered forms of occupation and how inclusive gendered words are translated.


## Citation

If you use this code or FairTranslate dataset, please cite the associated paper.

```bibtex
@inproceedings{jourdan2025FairTranslate,
  TITLE = {{FairTranslate: An English-French Dataset for Gender Bias Evaluation in Machine Translation by Overcoming Gender Binarity}},
  AUTHOR = {Jourdan, Fanny and Chevalier, Yannick and Favre, C{\'e}cile},
  URL = {https://hal.science/hal-05042789},
  BOOKTITLE = {{8th annual ACM FAccT conference (FAccT 2025)}},
  ADDRESS = {Ath{\`e}nes, Greece},
  ORGANIZATION = {{ACM}},
  YEAR = {2025},
  MONTH = Jun,
  KEYWORDS = {Fairness ; Natural Language Processing ; Translation ; LLM ; Gender},
  PDF = {https://hal.science/hal-05042789v1/file/ACM_FAccT_Conference-4.pdf},
  HAL_ID = {hal-05042789},
  HAL_VERSION = {v1},
}
