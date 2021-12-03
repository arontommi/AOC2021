import click
import collections


def subset_based_on_starting(files, subsetter):
    selected = []
    stopper = True
    if subsetter == 'none':
        selected = files
    else:
        selected = {}
        for k, i in files.items():
            if str(i[0]) == str(subsetter):
                if len(i) == 1:
                    selected[k] = i
                else:
                    selected[k] = i[1:]
    if len(selected) == 1:
        stopper = False
    return selected, stopper


def most_common_first(t_matrix, ):
    counter = collections.Counter(t_matrix[0])
    if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
        mostcommon = 1
    else:
        mostcommon = collections.Counter(t_matrix[0]).most_common(1)[0][0]
    return mostcommon


def least_common_first(t_matrix, ):
    counter = collections.Counter(t_matrix[0])
    if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
        mostcommon = 0
    else:
        mostcommon = collections.Counter(t_matrix[0]).most_common(2)[1][0]
    return mostcommon


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    masterlist = {}
    files = open(f'{inp}')
    for nr, i in enumerate(files):
        masterlist[nr] = i.rstrip()
    original = masterlist.copy()

    subsetter = 'none'
    stopper = True

    while stopper:
        t_matrix = list(map(list, zip(*masterlist.values())))
        subsetter = most_common_first(t_matrix)
        masterlist, stopper = subset_based_on_starting(masterlist, subsetter)
    v1 = int("0b" + original[list(masterlist.keys())[0]], 2)

    subsetter = 'none'
    stopper = True
    masterlist = original.copy()
    while stopper:
        t_matrix = list(map(list, zip(*masterlist.values())))
        subsetter = least_common_first(t_matrix)
        masterlist, stopper = subset_based_on_starting(masterlist, subsetter)
    v2 = int("0b" + original[list(masterlist.keys())[0]], 2)

    print(v1 * v2)


if __name__ == "__main__":
    main()
