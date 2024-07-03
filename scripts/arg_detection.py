import os
import subprocess

def detect_args(assembled_contigs_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    contig_files = [f for f in os.listdir(assembled_contigs_dir) if f.endswith('.fasta')]
    for contig_file in contig_files:
        output_file = os.path.join(output_dir, contig_file.replace('.fasta', '_args.txt'))
        subprocess.run(['abricate', '--db', 'ncbi', os.path.join(assembled_contigs_dir, contig_file), '>', output_file])
