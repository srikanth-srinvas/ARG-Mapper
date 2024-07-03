import os
import subprocess

def call_variants(mapped_reads_dir, reference_genome, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    bam_files = [f for f in os.listdir(mapped_reads_dir) if f.endswith('.bam')]
    for bam_file in bam_files:
        output_vcf = os.path.join(output_dir, bam_file.replace('.bam', '.vcf'))
        subprocess.run(['samtools', 'mpileup', '-uf', reference_genome, os.path.join(mapped_reads_dir, bam_file), '|', 'bcftools', 'call', '-mv', '-Ov', '-o', output_vcf])
