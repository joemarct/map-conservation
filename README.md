map-conservation
================

Performs mapping of residue conservation into PDB structures

## Conservation Mapping Protocol

### Objective

To derive residue conservation scoring from a multiple alignment of homologous proteins and map it into the structure of one of the aligned sequences

### Requirements

1. PDB file of the solved structure
2. Protein sequences of homologs
3. MUSCLE multiple alignment program Web server address:
http://www.ebi.ac.uk/Tools/msa/muscle The source file can be downloaded from:
http://www.drive5.com/muscle
4. PyMOL molecular graphics program
5. Conservation mapping program (installation is described below)

### Procedure

1. Installation of the conservation mapping program
__1.1. Open Terminal (available only in Mac OS and Linux)
__1.2. Make sure that pip is installed by running this command in the Terminal:
_______easy_install pip
__1.3. Install the conservation mapping program using pip with the following the Terminal:
_______pip install git+https://github.com/joemarct/map-conservation.git

2. Preparation of the structure and derived sequence
__2.1. Get the amino acid sequence of the solved structure in FASTA format. If you do not have it
separately, you can extract the sequence from the PDB file by opening it in PyMOL and saving the
molecule in FASTA format.
__2.2. If you have exported your sequence from PyMOL, check the sequence to make sure the written
sequence matches with what is displayed in PyMOL. Correct the exported sequence, if necessary.
__2.3. Rename the PDB file into structure.pdb.

3. Multiple sequence alignment
__3.1. Convert the sequence file of the homologs into FASTA format, if it is not in that format yet.
__3.2. Append the sequence of the solved structure into the sequence file of the homologs.
__3.3. Do a multiple alignment of the combined sequence file using MUSCLE. Manually check the
alignment and remove odd sequences, if necessary. You may use Jalview for this
(www.jalview.org).
__3.4. Rename the output alignment file into input_alignment.fasta.

4. Residue conservation scoring and mapping
__4.1. Put the structure.pdb and input_alignment.fasta file into a single folder / directory.
__4.2. Open Terminal, change directory to the working folder with the following command:
_______cd <path_to_the_directory>
__4.3. Execute the conservation mapping script by issuing the following command:
map_conservation.py
__4.4. Drag the resulting conservation_mapping.py file into PyMOL. This will show the color mapping of the residue conservation. By default, the color spectrum is yellow-white-blue in order of increasing conservation. Hence, the least conserved residues are in yellow and the more conserved ones are in blue.
