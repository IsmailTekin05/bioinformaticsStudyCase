rule all:
    input:
        "results/nanoplot_output/NanoPlot-report.html",
        "results/read_metrics.csv",
        "results/gc_content_dist.png",
        "results/read_length_dist.png",
        "results/mean_quality_dist.png",
        "results/summary_statistics.txt"

rule run_nanoplot:
    input:
        "data/input.fastq"
    output:
        "results/nanoplot_output/NanoPlot-report.html"
    shell:
        """
        NanoPlot --fastq {input} -o results/nanoplot_output
        """

rule analyze_reads:
    input:
        "data/input.fastq"
    output:
        "results/read_metrics.csv"
    shell:
        """
        python scripts/analyze_reads.py {input} {output}
        """

rule visualize_metrics:
    input:
        "results/read_metrics.csv"
    output:
        gc_plot="results/gc_content_dist.png",
        length_plot="results/read_length_dist.png",
        quality_plot="results/mean_quality_dist.png",
        summary="results/summary_statistics.txt"
    shell:
        """
        python scripts/visualize_metrics.py {input} {output.gc_plot} {output.length_plot} {output.quality_plot} {output.summary}
        """