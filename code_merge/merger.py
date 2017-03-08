import os
# input type should be file directory


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


def merge(old, new):
    print('merging test')

    input = []
    with open(old, 'r') as f:
        input = f.readlines()

    print('input lines : ', input)


if __name__ == "__main__":
    updateUI('./sampleinput.py', './sampleoutput.py')
