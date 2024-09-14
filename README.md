# Exploratory Data Analysis of Urdu Common Voice Dataset

This repository contains an exploratory data analysis (EDA) of an Urdu dataset from [Common Voice](https://commonvoice.mozilla.org/en/datasets). The project focuses on two main objectives:

1. **Investigating the Influence of Fluency on Pronunciation Scores**
2. **Evaluating the Performance of Advanced Transcription Tools for Urdu**

---

## Introduction

The Urdu Common Voice dataset is a collection of user-submitted audio recordings aimed at improving speech recognition technologies for the Urdu language. Understanding the factors that influence pronunciation quality and assessing current transcription tools are essential steps toward enhancing these technologies.

---

## Objective 1: Influence of Fluency on Pronunciation Scores

### Background

Pronunciation scores in the dataset are determined by the difference between upvotes and downvotes each recording receives from listeners. A key question is whether a speaker's fluency in Urdu affects these scores. However, the dataset does not explicitly indicate each speaker's fluency level.

### Methodology

#### Extracting Fluency Information

Speakers often included descriptions of their accent or background, such as:

> "I am Pakistani, so I have been speaking Urdu since childhood."

These self-reported descriptions provide insights into their fluency.

#### Classification Using Llama 3 70B

- **Tool Used**: Employed the [Llama 3 70B](https://www.groq.com/) language model from Groq Cloud.
- **Purpose**: Classified speakers as "Fluent" or "Non-Fluent" based on their textual descriptions.
- **Process**:
  - Collected and cleaned the accent descriptions.
  - Input the text into the LLM for classification.
  - Labeled each data entry accordingly.

#### Statistical Analysis

- **Hypothesis**: Fluent speakers receive higher pronunciation scores than non-fluent speakers.
- **Data Analysis**:
  - Calculated pronunciation scores (upvotes minus downvotes).
  - Compared scores between fluent and non-fluent groups.
- **Statistical Tests**:
  - Performed t-tests to determine if differences were statistically significant.

### Results

- **Significant Difference**: Fluent speakers had significantly higher pronunciation scores.
- **Implication**: Fluency positively influences how listeners perceive and rate pronunciations.

### Conclusion

The analysis confirms that fluency is a significant factor affecting pronunciation scores in the Urdu Common Voice dataset. This insight can help in filtering and prioritizing data for training speech recognition models.

---

## Objective 2: Evaluating Advanced Transcription Tools for Urdu

### Background

Assessing the performance of current transcription models on high-quality Urdu data provides valuable feedback on the state of speech recognition technology for the language.

### Methodology

#### Transcription with AssemblyAI's Nano Model

- **Tool Used**: [AssemblyAI's](https://www.assemblyai.com/) nano model for speech-to-text transcription.
- **Process**:
  - Submitted the high-quality audio recordings from the dataset to the model.
  - Collected the transcribed text outputs for analysis.

#### Measuring Accuracy with Levenshtein Distance

- **Levenshtein Distance**:
  - A metric that calculates the minimum number of single-character edits required to change one word into another.
- **Application**:
  - Compared the transcribed text to the original sentences spoken in the recordings.
  - Calculated the similarity percentage based on the Levenshtein distance.

### Results

- **Approximate 50% Similarity**: The transcriptions were only about 50% similar to the original text.
- **Interpretation**:
  - Indicates that the model struggles with accurately transcribing Urdu.
  - Highlights the challenges in developing effective speech recognition for the language.

### Conclusion

Current advanced transcription tools like AssemblyAI's nano model have limited accuracy in transcribing Urdu audio. This underscores the need for further research and development to improve speech recognition technologies for Urdu.

---

## Overall Conclusion

The project reveals important findings:

- **Fluency Impact**: There's a significant positive correlation between a speaker's fluency and their pronunciation scores.
- **Transcription Limitations**: Existing transcription models are not yet sufficiently accurate for Urdu, even with high-quality audio data.

These insights emphasize the importance of considering speaker fluency in data collection and the need for continued advancement in Urdu speech recognition technology.

---

## Repository Structure

- `data/`:
  - Link to download data.
- `scripts/`:
  - Python scripts for the LLM classifier.
- `notebooks/`:
  - Jupyter notebooks detailing each step of the EDA, statistical analysis, and transcription evaluation.
- `README.md`:
  - Project overview.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Jupyter Notebook or JupyterLab
- Required Python packages listed in `requirements.txt`

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/hash2004/EDA-Voice-Data.git
   cd EDA-Voice-Data
   ```
2. **Download the data**
3. **Run the notebook**
