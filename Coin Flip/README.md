# Coin Flip Simulations

Simple Python scripts to simulate coin tosses and observe head/tail distribution.

## Files

- `coin flip.py`: interactive 5-toss simulator in a loop.
- `Coin flip counter.py`: multi-trial simulation with increasing toss counts and average head/tail gap summary.
- `Coin flip counter.pdf`: supporting document/output file.

## 1) Quick Interactive Simulation

File: `coin flip.py`

Behavior:
- Repeats until you type `q`.
- Any other input runs 5 tosses.
- Prints counts of `Head` and `Tail` for that round.

Run:

```bash
python "coin flip.py"
```

## 2) Statistical Counter Simulation

File: `Coin flip counter.py`

Behavior:
- Runs 4 groups of experiments (`10`, `100`, `1000`, `10000` tosses).
- For each group, performs 5 trials and prints percentages.
- Prints average head/tail percentages and their gap per group.

Run:

```bash
python "Coin flip counter.py"
```

## Requirements

- Python 3.x
- Standard library only (`random`)

## Notes

- This is a learning/project script for probability intuition.
- Very large ranges may take noticeably longer to run.
