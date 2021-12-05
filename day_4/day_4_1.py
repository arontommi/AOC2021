import click
import collections
import numpy as np


@click.command(context_settings={"help_option_names": ["-h", "--help"]},
               no_args_is_help=True)
@click.option('-i', '--inp', help='some data')
def main(inp):
    with open(f'{inp}') as f:
        sequence = f.readline().strip().split(',')
        bingocard = False
        bingocardcounter = 0
        bingocardholder = {}
        for i in f:
            if i == '\n':
                if bingocard:
                    bingocardholder[f"{bingocardcounter}"] = np.array(
                        bingocard)
                bingocard = []
                bingocardcounter = bingocardcounter + 1
            else:
                bingoline = i.strip().split()
                bingoline = list(map(int, bingoline))
                bingocard.append(bingoline)

        bingocardholder[f"{bingocardcounter}"] = np.array(bingocard)
    t_bingocardholder = {}
    for k, v in bingocardholder.items():
        t_bingocardholder[f"t_{k}"] = np.transpose(v)
    all_cards = {**t_bingocardholder, **bingocardholder}
    stop = False
    for i in sequence:
        if stop:
            break
        else:
            for k, card in all_cards.items():
                dcard = []
                for line in card:
                    nline = np.delete(line, np.where(line == int(i)))
                    dcard.append(nline)
                    if len(nline) == 0:

                        total = 0
                        for ar in card:
                            total = total + np.sum(ar)
                        print((total - int(i)) * int(i))
                        stop = True
                all_cards[k] = dcard


if __name__ == "__main__":
    main()
