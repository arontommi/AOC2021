import click


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    file = open(f'{inp}')
    ints = list(map(int, file))

    previous_window = 0
    counter = 0
    for nr, i in enumerate(ints):
        window = sum(ints[nr:nr + 3])
        if len(ints[nr:nr + 3]) < 3:
            break
        if window > int(previous_window):
            counter = counter + 1
        previous_window = window
    print(counter - 1)


if __name__ == "__main__":
    main()
