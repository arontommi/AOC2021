import click


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    with open(f'{inp}', 'r') as f:
        moves = []
        for line in f:
            move, n = line.rstrip().split()
            moves.append((move, int(n)))

    def day2_pt1(moves):
        horiz, depth = 0, 0
        for move, n in moves:
            if move == 'up':
                depth -= n
            elif move == 'down':
                depth += n
            else:
                horiz += n
        return horiz * depth

    print(day2_pt1(moves))


if __name__ == "__main__":
    main()
