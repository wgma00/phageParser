'''
Script to interpret blaster XML files.
    Usage:
        blast_analyzer file [cutoff]
        tfile - path XML file produced by the BLAST function in issue
        cutoff- optional, expected value cutoff, default is set to 1.
'''


import sys
from Bio.Blast import NCBIXML as NCBIXML


def usage():
    print("Usage:\n\tblast_analyzer file [cutoff]")
    print("\tfile - path XML file produced by the BLAST function in issue")
    print("\tcutoff- optional, expected value cutoff, default is set to 1.")


def analyzer(file, cutoff=1):
    try:
        result_handle = open(file)
        blast_record = NCBIXML.parse(result_handle)

    except FileNotFoundError:
        print('File not found at specified path:', xml_file_path)
        exit(1)

if __name__ == '__main__':
    # argv has n+1 entries, for function inputs and the executable itself
    args = sys.argv
    if 2 <= len(args) <= 3:
        xml_file_path = str(args[1])
        cutoff_val = 1
        if len(args) == 3:
            cutoff_val = str(args[2])
        analyzer(xml_file_path, cutoff_val)
    else:
        usage()
        exit(1)
