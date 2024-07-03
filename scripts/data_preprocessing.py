import os
import subprocess

def run_fastqc(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fastq_files = [f for f in os.listdir(input_dir) if f.endswith('.fastq.gz')]
    for fastq_file in fastq_files:
        subprocess.run(['fastqc', os.path.join(input_dir, fastq_file), '-o', output_dir])

def trim_adapters(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fastq_files = [f for f in os.listdir(input_dir) if f.endswith('.fastq.gz')]
    for fastq_file in fastq_files:
        output_file = os.path.join(output_dir, fastq_file.replace('.fastq.gz', '_trimmed.fastq.gz'))
        subprocess.run(['trimmomatic', 'SE', '-phred33', os.path.join(input_dir, fastq_file), output_file, 'ILLUMINACLIP:TruSeq3-SE.fa:2:30:10'])
