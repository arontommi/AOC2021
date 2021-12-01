import click


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    print(f'{inp}')
    file = open(f'{inp}')
    previous = 0
    counter = 0
    for i in file:
        if int(i) > int(previous):
            counter = counter + 1
        previous = i
    print(counter)


if __name__ == "__main__":
    main()
