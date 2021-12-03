import click
import collections


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    files = open(f'{inp}')
    matrix = []
    for i in files:
        sublist = []
        i = i.rstrip()
        for ii in i:
            sublist.append(int(ii))

        matrix.append(sublist)

    t_matrix = map(list, zip(*matrix))
    mostcommon = []
    leastcommon = []
    for i in t_matrix:
        mostcommon.append(collections.Counter(i).most_common(1)[0][0])
        leastcommon.append(collections.Counter(i).most_common(2)[1][0])
    mostcommon = int("0b" + "".join([str(thing) for thing in mostcommon]), 2)
    leastcommon = int("0b" + "".join([str(thing) for thing in leastcommon]), 2)

    print(mostcommon * leastcommon)


if __name__ == "__main__":
    main()
