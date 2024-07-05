import argparse
import os
from scripts.data_preprocessing import run_fastqc, trim_adapters
from scripts.read_mapping import map_reads
from scripts.variant_calling import call_variants
from scripts.arg_detection import detect_args
from scripts.comparative_analysis import load_arg_results, compare_args
from scripts.visualization import plot_arg_distribution
from scripts.utils import find_reference_genome

def print_ascii_art():
    art = r"""
     ___    ____   _____ 
    / _ \  |  _ \ |  ___|
   | | | | | |_) || |___ 
   | | | | |  _ < |  ___|
   | |_| | | |_) || |___ 
    \___/  |____/ |_____|
    """
    print(art)
    print("     ARG Framework")

def main(args):
    raw_reads_dir = args.raw_reads_dir
    reference_genome = find_reference_genome(args.species_name)
    qc_reports_dir = 'data/qc_reports'
    trimmed_reads_dir = 'data/trimmed_reads'
    mapped_reads_dir = 'data/mapped_reads'
    variants_dir = 'data/variants'
    args_dir = 'data/ARG_results'
    
    run_fastqc(raw_reads_dir, qc_reports_dir)
    trim_adapters(raw_reads_dir, trimmed_reads_dir)
    run_fastqc(trimmed_reads_dir, qc_reports_dir)
    map_reads(reference_genome, trimmed_reads_dir, mapped_reads_dir)
    call_variants(mapped_reads_dir, reference_genome, variants_dir)
    detect_args(variants_dir, args_dir)
    
    arg_data = load_arg_results(args_dir)
    summary = compare_args(arg_data)
    summary.to_csv('results/arg_comparison.csv')
    
    plot_arg_distribution(summary, 'results/arg_distribution.png')

if __name__ == "__main__":
    print_ascii_art()
    
    parser = argparse.ArgumentParser(description="Comparative ARG Framework")
    parser.add_argument('--raw_reads_dir', type=str, required=True, help="Directory containing raw FASTQ files")
    parser.add_argument('--species_name', type=str, required=True, help="Species name to find reference genome")
    
    args = parser.parse_args()
    main(args)
