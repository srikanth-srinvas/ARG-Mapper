# Comparative ARG Framework

Welcome to the Comparative ARG Framework! This tool is designed to streamline the analysis of antibiotic resistance genes (ARGs) in bacterial genomes. By providing a standardized pipeline, it allows researchers to compare ARG prevalence and distribution across different bacterial species and environments, helping to identify emerging threats and inform intervention strategies.

## Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Output](#output)
6. [Credits](#credits)
7. [Software Dependencies](#software-dependencies)

## Introduction

Antibiotic resistance is a significant global health challenge. The Comparative ARG Framework enables researchers to:
- Compare ARG prevalence and distribution across bacterial populations.
- Identify novel or concerning resistance profiles.
- Contribute to the development of targeted therapies and public health measures.

## Features

- **Data Acquisition and Preprocessing**: Handles raw FASTQ files and performs quality control.
- **Reference Genome Selection**: Selects the appropriate reference genome for read mapping.
- **Standardized Analysis Workflow**: Includes read mapping, variant calling, and ARG detection.
- **Comparative Analysis and Visualization**: Compares ARG profiles and visualizes the results.
- **Modular Design**: Ensures reusability and easy integration with other projects.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/comparative-arg-framework.git
    cd comparative-arg-framework
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv biopython_env
    source biopython_env/bin/activate
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Prepare your data

1. Place your raw FASTQ files in a directory.
2. Ensure you have the species name for the reference genome.

### Run the pipeline

```sh
python src/main.py --raw_reads_dir path/to/your/fastq/files --species_name "YourSpeciesName"
```

## Example 
```sh
python src/main.py --raw_reads_dir data/example_fastq --species_name "Escherichia_coli"
```
This command will process the FASTQ files, map the reads to the reference genome, call variants, detect ARGs, and generate comparative analysis results.

## Output

The pipeline generates the following outputs:

- **QC Reports**: Quality control reports for raw and trimmed reads.
- **Mapped Reads**: BAM files of mapped reads.
- **Variants**: VCF files of identified variants.
- **ARG Results**: Detected ARGs in CSV format.
- **Comparative Analysis**: Summary table and visualizations of ARG distribution.

## Credits

This project utilizes the following software and libraries:

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
- [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)
- [BWA MEM](http://bio-bwa.sourceforge.net/)
- [SAMtools](http://www.htslib.org/)
- [BCFtools](http://www.htslib.org/)
- [ABRicate](https://github.com/tseemann/abricate)
- [pandas](https://pandas.pydata.org/)
- [Biopython](https://biopython.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [SciPy](https://www.scipy.org/)
- [Bokeh](https://bokeh.org/)
- [Plotly](https://plotly.com/)

## Software Dependencies

Ensure the following software dependencies are installed:

- Python 3.6 or higher
- FastQC
- Trimmomatic
- BWA MEM
- SAMtools
- BCFtools
- ABRicate