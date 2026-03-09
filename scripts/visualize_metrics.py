import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_visualizations(csv_path, gc_out, length_out, quality_out, summary_out):
    df = pd.read_csv(csv_path)

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(df['GC_Content_Percent'], bins=50, kde=True, color='green')
    plt.title('Distribution of GC Content (%)')
    plt.xlabel('GC Content (%)')
    plt.ylabel('Frequency')
    plt.savefig(gc_out)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.histplot(df['Read_Length'], bins=50, kde=True, color='blue')
    plt.title('Distribution of Read Lengths')
    plt.xlabel('Read Length (bp)')
    plt.ylabel('Frequency')
    plt.savefig(length_out)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.histplot(df['Mean_Quality_Score'], bins=50, kde=True, color='purple')
    plt.title('Distribution of Mean Read Quality Scores')
    plt.xlabel('Mean Phred Quality Score')
    plt.ylabel('Frequency')
    plt.savefig(quality_out)
    plt.close()

    summary_stats = df.describe()
    with open(summary_out, 'w') as f:
        f.write("Summary Statistics for Long-Read QC\n")
        f.write("===================================\n\n")
        f.write(f"Mean Read Length: {df['Read_Length'].mean():.2f} bp\n")
        f.write(f"Median Read Length: {df['Read_Length'].median():.2f} bp\n")
        f.write(f"Mean Quality Score: {df['Mean_Quality_Score'].mean():.2f}\n")
        f.write(f"Median Quality Score: {df['Mean_Quality_Score'].median():.2f}\n")
        f.write(f"Mean GC Content: {df['GC_Content_Percent'].mean():.2f}%\n")
        f.write(f"Median GC Content: {df['GC_Content_Percent'].median():.2f}%\n")

    print(summary_stats)


if __name__ == "__main__":
    csv_file = sys.argv[1]
    gc_plot = sys.argv[2]
    length_plot = sys.argv[3]
    quality_plot = sys.argv[4]
    summary_txt = sys.argv[5]
    generate_visualizations(csv_file, gc_plot, length_plot, quality_plot, summary_txt)