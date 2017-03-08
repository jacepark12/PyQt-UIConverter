import os
# input type should be file directory

def updateUI(input, ouput):
    # check if exists or not


def merge(old, new):
    print('merging test')

    input = []
    with open(old, 'r') as f:
        input = f.readlines()

    print('input lines : ', input)

if __name__ == "__main__":
    merge('./sampleinput.py', './sampleoutput.py')
