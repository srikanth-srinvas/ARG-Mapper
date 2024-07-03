import os

def find_reference_genome(species_name):
    reference_dir = 'data/reference_genomes'
    for filename in os.listdir(reference_dir):
        if species_name in filename:
            return os.path.join(reference_dir, filename)
    return None
