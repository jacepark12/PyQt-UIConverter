import os
# input type should be file directory

# names of methods which will be changed
MERGE_METHODS = ['def setupUi(self, MainWindow):']


def updateUI(input, output):

    # check if exists or not
    if os.path.isfile(input):
        lines = []
        with open(input, 'r') as f:
            lines = f.readlines()

        # write py file
        with open(output, 'w+') as f:
            f.writelines(lines)

    else:
        merge(input, output)

    print('======convert complete')


def merge(input, output):
    print('merging test')

    input_lines = []
    change_line_numbers = []
    with open(input, 'r') as f:
        input_lines = f.readlines()

    for line in input_lines:
        if line in MERGE_METHODS:

        else:


    print('input lines : ', input_lines)


if __name__ == "__main__":
    updateUI('./sampleinput.py', './sampleoutput.py')
