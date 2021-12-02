import click


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    files = open(f'{inp}')
    starting_pos = {"hp": 0, "d": 0, 'aim': 0}

    for n, i in enumerate(files):
        try:
            instruction, increment = i.split()
        except ValueError:
            instruction, increment = [i, 1]
        if instruction == 'forward':
            starting_pos['hp'] = starting_pos['hp'] + int(increment)
            starting_pos[
                'd'] = starting_pos['d'] + starting_pos['aim'] * int(increment)
        if instruction == 'down':
            starting_pos['aim'] = starting_pos['aim'] + int(increment)
        if instruction == 'up':
            starting_pos['aim'] = starting_pos['aim'] - int(increment)
        print(instruction, increment, starting_pos)
    print(starting_pos['hp'] * starting_pos['d'])


if __name__ == "__main__":
    main()
