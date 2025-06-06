# Bioinformatics Lab Exercises - BIOL668
## Description
This is a compilation of bioinformatics exercises assigned during lab, for the BIOL 668 course taught by Dr. Scott Kelley at San Diego State. Through these exercises, students become familar with a variety of biological data analysis methods, and expand their computational skillset for applications to their thesis research.
- Required data and files vary based on the assignment. These will be listed with respective subheadings under the instructions section.

## Instructions 

### R Lab 01

You will need the following files:
- RTestData.txt
- primer-1.csv
- r_bash.sh
- r.py
- test.r

You will utilize RTestData.txt to do some basic statistical analyses of several bacteria. The shell and python scripts are provided to attempt to run in the terminal, on the command line of your device.

### Pandas and Python

Utilize these files: 
- PandasScipyPractice.ipynb
- hist_taxa_treat2.txt

You will follow the guided tutorial provided in the Jupytr Notebook, to introduce you to utilizing the platform, and the ``pandas`` module.

Ensure that you always import at the top of the file: in the case of Jupytr Notebook, within the first cell. 

```
import os
import re
import pandas as pd
from scipy import stats
```

The file will allow you, in the last part, create a function that calculates basic statistics of different columns of your test data. There are examples for you to test your function on.

```
out=calc_stats("hist_taxa_treat2.txt", "Count")
print(out)
#Should print [233173.0, 28.0, 218.32677902621722, 448.92572275301353, 0.0, 4317.0]
```

### Python OOP Lab 1

This exercise introduces students to object-oriented programming, out of the context of biological data analysis. Tasks provided explain concepts through video game-like programming.

Files required include:
- Harnden_person.py
- make_person.py (instances to test your class on)
- Harnden_wizard_class_HW.py

You will begin with person.py file, creating a subclass from the parent class, Person. You can then use make_person.py to test your class, as it includes a couple of examples of instances.

With the final script, you will practice further with objectoriented programming by perfecting functions associated with both the parent class and the derived class, Wizard.

You can use ``super()`` to transfer all the methods and data from the parent class, Character, into Wizard.

There are a variety of instances at the end, to test your functioning code, preceded by the following lines:

```
if __name__=="__main__":
print("Ready...Set...Fight!")
```

This condition will not be met if this script is imported elsewhere.

### QIIME2

Required data:
- https://data.qiime2.org/2024.10/tutorials/moving-pictures/sample_metadata.tsv
- https://data.qiime2.org/2024.10/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz
- https://data.qiime2.org/2024.10/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz

You will use an online tutorial to gain experience with QIIME2, at https://docs.qiime2.org/2024.10/tutorials/moving-pictures/. One can install QIIME2 step-by-step at https://docs.qiime2.org/2024.10/install/.

It is expected that you complete this activty in the terminal-- you will be writing on the command line to complete this exercise. 

Various analyses with QIIME2 will be implemented, including quality control measures and checks, which are extremely helpful for large volumes of sequence data and reads.

### RNA_SEQ_LAB

The following data will guide you with unveiling three RNA sequencing analysis tools:
- rna_counts_data.csv
- rna_map_update copy.csv
- pbmc3k_filtered_gene_bc_matrices.tar.gz

You may create separate R notebooks for each exercise, which will equip you with code to use potentially as pipelines for future RNA data analysis.

For part 1, you will follow the associated Bioconductor project's tutorial, at https://bioconductor.org/packages/release/workflows/vignettes/RNAseq123/inst/doc/limmaWorkflow.html. Here, you will learn how to use ``Glimma``, ``limma``, and ``edgeR`` packages in RStudio, which provide everything from methods to filter and organize data, to modeling differential expression data, to generating interactive plots, allowing for clear investigation into your data.

In part 2, you will stick to a guided tutorial from Dr. Ashley Schwartz, will be followed for learning DESeq2 for running Differential Gene Expression (DGE) analysis, between a treatment and control group, construying it into one giant data table. In this case, you will be comparing mutants with wild types, derived from cancer cell lines. Here, you will utilize the second file listened above.

Begin with relevant installations. Thes may take a while, so be patient.

```
# install DESeq2
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("DESeq2")

# install tidyverse (ggplot2 is in tidyverse)
install.packages("tidyverse")
```

You can then proceed through the tutorial, replacing entries of Dr. Schwartz data with your own read count files. 


In part 3, you will learn how to analyze single-cell RNA (scRNA) sequences with Seurat, following a tutorial from their website, https://satijalab.org/seurat/. This involves using the final dataset, which consists of 2,700 single cells sequenced utilzing Illumina NextSeq 500.

Thus, ensure you unzip the tarball file before use, which can be done on the command line.

```
tar -xvzf pbmc3k_filtered_gene_bc_matrices.tar.gz
```

Begin by opening a new notebook, and downloading and installing the Seurat package in R Studio, via CRAN mirror. You can find this under "Install" on their website. There are additional packages that the site recommends to install, as they can improve the speed and performance of Seurat.

```
# Enter commands in R (or R studio, if installed)
install.packages('Seurat')
library(Seurat)

# Additionally recommended installations
setRepositories(ind = 1:3, addURLs = c('https://satijalab.r-universe.dev', 'https://bnprks.r-universe.dev/'))
install.packages(c("BPCells", "presto", "glmGamPoi"))

# Install the remotes package, which enhance Seurat's functionality
if (!requireNamespace("remotes", quietly = TRUE)) {
  install.packages("remotes")
}
install.packages('Signac')
remotes::install_github("satijalab/seurat-data", quiet = TRUE)
remotes::install_github("satijalab/azimuth", quiet = TRUE)
remotes::install_github("satijalab/seurat-wrappers", quiet = TRUE)
```
Now, navigate to the "Getting Started" page, and choose the Guided Tutorial -- 2,700 PBMC's (https://satijalab.org/seurat/articles/pbmc3k_tutorial).

Read in your data and proceed through the tutorial to pre-process, normalize, cluster, and visualize differential expression amongst cell types, as to generate clear, compelling graphs.


### AlgsAndGenomes

This final lab familiarizes studes with metagenomic analysis. It is to be completed in the shell.

Required files: 
- out.insub732_2_R1_fastp.fastq
- insub732_2_R2.fastp.fastq.gz
- reads_1.fq
- reads_2.fq

In the first exercise, fastq file processing will be done, using fastp. Fastp can be downloaded according to the GitHub tutorial at https://github.com/OpenGene/fastp#get-fastp.

The out.insub732_2_R1_fastp.fastq and insub732_2_R2.fastp.fastq.gz forward (R1) and reverse (R2) paired-end read files will be used.

If one's terminal of virtual box is not working properly, ``ssh`` can be used from another computer.

Begin by creating a conda environment that allows for use and activation of ``fastp`` within it. 

```
conda creaete -n fastp
conda  activate fastp
conda install -c bioconda fastp
```

Onward, fastp can be used within the created environment to filter the data, and export a summary output -- a fastp report -- of the data prior and after processing, shedding insight on determinig factors like quality and length.

In the second exercise, you will download and install ``Kaiju`` to investigate a viral metagenomic dataset. Follow the instructions provided at https://github.com/bioinformatics-centre/kaiju/blob/master/README.md.

Since it is similarly avaialble with the bioconda channel, one can use the following commands to install Kaiju:

```
conda install -c bioconda kaiju
# or
mamba install -c bioconda kaiju
```

The ``viruses`` database provided by the tutorial should then be downloaded, alongside the test files given here, reads_1.fq and reads_2.fq. Be sure to unzip the tarball ``viruses`` file.

One can then create output files comparing the test data to the database provided for classifying the information as viral or non-viral.
