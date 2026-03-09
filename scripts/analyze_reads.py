import sys
import csv
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def calculate_metrics(fastq_path, output_csv):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Read_ID', 'GC_Content_Percent', 'Read_Length', 'Mean_Quality_Score'])

        for record in SeqIO.parse(fastq_path, "fastq"):
            read_id = record.id

            read_length = len(record.seq)

            gc_content = gc_fraction(record.seq) * 100

            quality_scores = record.letter_annotations["phred_quality"]
            mean_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0

            writer.writerow([read_id, round(gc_content, 2), read_length, round(mean_quality, 2)])


if __name__ == "__main__":
    input_fastq = sys.argv[1]
    output_csv = sys.argv[2]
    calculate_metrics(input_fastq, output_csv)