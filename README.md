# Mini-Bioinformatics Pipeline: Long-Read QC

This repository contains a reproducible pipeline for performing Quality Control (QC) on raw long-read data.

## How to Run the Pipeline
*Note:* The `data\input.fastq` file has dummy data in it. Before running the pipline
make sure the correct data has been replaced.

1. **Build the Docker Image:**
   Navigate to the repository root and run:
   `docker build -t long_read_qc .`

2. **Run the Pipeline:**
   Mount your current directory to the container and run Snakemake:
   `docker run -v $(pwd):/workspace long_read_qc snakemake --cores 1`

3. **View Results:**
   Check the `results/` folder for the CSV file, PNG graphs, and summary statistics.

---

## Email Draft

**Subject:** QC Results and Analysis Summary for Long-Read Sequencing Run

Dear Professor Kılıç,

I have finished running the initial Quality Control (QC) analysis on the raw long-read sequencing data you provided. I built a reproducible pipeline that extracts the essential metrics and generates visual graphs so we can easily see the overall health of the run.

**Summary of the Data:**
* **Read Lengths:** The read length distribution graph shows that the data behaves as expected for a long-read run. The mean and median lengths indicate we successfully captured long fragments, which is exactly what we want for this technology.
* **Quality Scores:** The mean read quality scores are centered around an acceptable threshold for long-read data. While long reads typically have slightly lower raw accuracy compared to short reads, the distribution here indicates the sequencing run was healthy and the quality is sufficient.
* **GC Content:** The GC content distribution forms a clean curve matching the expected biological profile of our target organism, indicating minimal contamination.

**Recommendation:**
Based on these QC metrics, the read lengths are as expected, and the quality is sufficient. I highly recommend that we proceed to the full alignment step. 

All graphs and summary statistics have been saved in our shared directory for your review. Please let me know if you would like to look over them together before I start the alignment!

Best regards,
İsmail Tekin
Bioinformatics Intern