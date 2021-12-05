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
    newd = all_cards.copy()
    for i in sequence:
        if stop:
            break
        else:
            for k, card in all_cards.items():
                if stop:
                    break
                dcard = []
                for line in card:
                    if len(line) == 0:
                        if len(newd) == 2:
                            rkey = list(newd.keys())[0].replace('t_', "", 1)
                            rcard = all_cards[rkey]
                            for ll in rcard:
                                if len(ll) == 0:
                                    stop = True
                                    total = 0
                                    for ar in rcard:
                                        total = total + np.sum(ar)
                                    print(int(i), total, (total) * int(i))
                        else:
                            key = k.replace("t_", '', 1)
                            newd.pop(key, None)
                            newd.pop(f't_{key}', None)
                    nline = np.delete(line, np.where(line == int(i)))
                    dcard.append(nline)
                    all_cards[k] = dcard


if __name__ == "__main__":
    main()
