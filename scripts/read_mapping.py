import os
import subprocess

def map_reads(reference_genome, reads_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    read_files = [f for f in os.listdir(reads_dir) if f.endswith('_trimmed.fastq.gz')]
    for read_file in read_files:
        output_file = os.path.join(output_dir, read_file.replace('_trimmed.fastq.gz', '.bam'))
        subprocess.run(['bwa', 'mem', reference_genome, os.path.join(reads_dir, read_file), '|', 'samtools', 'view', '-Sb', '|', 'samtools', 'sort', '-o', output_file])
