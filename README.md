map-conservation
================

Performs mapping of residue conservation into PDB structures

## Conservation Mapping Protocol

### Objective

To derive residue conservation scoring from a multiple alignment of homologous proteins and map it into the structure of one of the aligned sequences

### Requirements

<ol>
<li>PDB file of the solved structure</li>
<li>Protein sequences of homologs</li>
<li>MUSCLE multiple alignment program
    <ul><li>Web server address: http://www.ebi.ac.uk/Tools/msa/muscle</li></ul>
    <ul><li>The source file can be downloaded from: http://www.drive5.com/muscle</li></ul>
</li>
<li>PyMOL molecular graphics program</li>
<li>Conservation mapping program (installation is described below)</li>
</ol>

### Procedure
<ol>

<li>Installation of the conservation mapping program
    <ol>
        <li>Open Terminal (available only in Mac OS and Linux)</li>
        <li>Make sure that pip is installed by running this command in the Terminal:
            <ul><li>easy_install pip</li></ul>
        </li>
        <li>Install the conservation mapping program using pip with the following the Terminal:
            <ul><li>pip install git+https://github.com/joemarct/map-conservation.git</li></ul>
        </li>
</li>

<li>Preparation of the structure and derived sequence
    <ol>
        <li>Get the amino acid sequence of the solved structure in FASTA format. If you do not have it
separately, you can extract the sequence from the PDB file by opening it in PyMOL and saving the
molecule in FASTA format.</li>
        <li>If you have exported your sequence from PyMOL, check the sequence to make sure the written
sequence matches with what is displayed in PyMOL. Correct the exported sequence, if necessary.</li>
        <li>Rename the PDB file into structure.pdb.</li>
    </ol>
</li>

<li>Multiple sequence alignment
    <ol>
        <li>Convert the sequence file of the homologs into FASTA format, if it is not in that format yet.</li>
        <li>Append the sequence of the solved structure into the sequence file of the homologs.</li>
        <li>Do a multiple alignment of the combined sequence file using MUSCLE. Manually check the
alignment and remove odd sequences, if necessary. You may use Jalview for this
(www.jalview.org).</li>
        <li>Rename the output alignment file into input_alignment.fasta.</li>
    </ol>
</li>

<li>Residue conservation scoring and mapping
    <ol>
        <li>Put the structure.pdb and input_alignment.fasta file into a single folder / directory.</li>
        <li>Open Terminal, change directory to the working folder with the following command:
            <ul><li>cd [path_to_the_directory]</li></ul>
        </li>
        <li>Execute the conservation mapping script by issuing the following command:
            <ul><li>map_conservation.py</ul></li>
        </li>
        <li>Drag the resulting conservation_mapping.py file into PyMOL. This will show the color mapping of the residue conservation. By default, the color spectrum is yellow-white-blue in order of increasing conservation. Hence, the least conserved residues are in yellow and the more conserved ones are in blue.</li>
    </ol>
</li>

</ol>
