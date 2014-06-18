#!/usr/bin/env python

from subprocess import Popen, PIPE
import os, sys


def show_usage_guide(show_error=False):
    if show_error:
        error_msg = '\nOops! Something went wrong here. You missed some input parameters.'
        error_msg += '\nCheck the guide below for correct usage.'
        print error_msg
    print '\nUsage guide:\n'
    print 'map_conservation.py <alignment_file> <pdb_file> <name_of_structure>'
    print '\nParameters:\n\nalignment_file ==> path to the alignment file'
    print 'pdb_file ==> path to the pdb_file'
    print 'name_of_structure ==> the FASTA ID of the sequence derived from the structure\n'
    

def execute_mapping(aln_file=None, pdb_file=None, structure_name=None):
    # Errors counter
    errors = 0
    # Read the PDB file
    if not errors:
        if pdb_file:
            pdb = open(pdb_file, 'r').read()
        else:
            try:
                pdb = open('structure.pdb', 'r').read()
            except IOError:
                errors += 1
                raise Exception("\n\nError: No 'structure.pdb' file found\n")
    # Read the alignment file if no error so far
    if not errors:
        if not aln_file:
            aln_file = 'input_alignment.fasta'
        aln = open(aln_file, 'r').read()
        try:
            aln = open('input_alignment.fasta', 'r').read()
        except IOError:
            raise Exception("\n\nError: No 'input_alignment.fasta' file found\n")
    # Verify structure name if no error so far
    if not errors:
        if not structure_name:
            structure_name = 'structure'
        # Check if structure name is present in the alignment
        accessions = [x.split()[0] for x in aln.split('>') if x]
        accessions = [x.split('/')[0] for x in accessions if '/' in x]
        if structure_name not in accessions:
            errors += 1
            raise Exception('\n\nError: Structure name does not match any sequence name in the alignment\n')
    # If no errors, proceed
    if not errors:
        # Get the working directory
        if aln_file:
            # If aln_file is given, its location is used
            working_dir = os.path.split(aln_file)[0]
        else:
            # Otherwise, the current working directory is used
            working_dir = os.getcwd()
        # Execute the scoring
        data_dir = os.path.join(sys.prefix, 'src', 'score-conservation')
        matrix = os.path.join(data_dir, 'matrix', 'blosum62.bla')
        distribution = os.path.join(data_dir, 'distributions', 'blosum62.distribution')
        cmd = 'score_conservation.py'
        cmd += ' -m %s -d %s -g 0.999999999999' % (matrix, distribution)
        cmd += ' -s js_divergence %s' % aln_file
        p = Popen(cmd, shell=True, stdout=PIPE)
        scores, stderr = p.communicate()
        # Build the conservation mapping script
        args = (pdb, aln, scores, structure_name)
        params = 'pdb_string="""%s"""\naln_string="""%s"""\nconservation_scores="""%s"""\nstructure_name="%s"' % args
        script_path = os.path.join(sys.prefix, 'src', 'map-conservation', 'conservation_mapping_script_base.txt')
        mapping_script = open(script_path, 'r').read()
        combined = params + '\n' + mapping_script
        outf_path = os.path.join(working_dir, 'conservation_mapping.py')
        outf = open(outf_path, 'w')
        outf.write(combined)
        outf.close()
    print '\nThe output conservation_mapping.py script has been written.' 
    print 'Drag that file to PyMOL to visualize the mapping.\n'


if __name__ == '__main__':
    
    # If the number of arguments provided is less than the expected
    if len(sys.argv[1:]) == 0:
        execute_mapping()
    elif len(sys.argv[1:]) < 3:
        try:
            # Get the command line arguments
            aln_file = sys.argv[1]
            pdb_file = sys.argv[2]
            structure_name = sys.argv[3]
            # Execute the mapping function
            execute_mapping(aln_file=aln_file, pdb_file=pdb_file, structure_name=structure_name)
        except IndexError:
            show_usage_guide(show_error=True)
        