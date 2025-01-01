from subprocess import Popen, PIPE
process = Popen(["cfish"], stdin=PIPE, stdout=PIPE, text=True)
process.stdin.write("uci")
def chess_bot(obs):
    process.stdin.write(f"position fen {obs.board}\n")
    process.stdin.write("go movetime 500\n")
    process.stdin.flush()
    while True:
        line = process.stdout.readline().strip().split()
        if line[0] == "bestmove":
            process.stdin.write(f"position fen {obs.board} moves {line[1]}\n")
            process.stdin.flush()
            return line[1]
