from subprocess import Popen, PIPE
import os

# Look for cfish executable in the current directory
cfish_path = "./cfish"
process = Popen([cfish_path], stdin=PIPE, stdout=PIPE, text=True)
process.stdin.write("uci\n")
process.stdin.flush()  # Flush after UCI command

def chess_bot(obs):
    process.stdin.write(f"position fen {obs.board}\n")
    process.stdin.write("go movetime 500\n")
    process.stdin.flush()
    
    while True:
        line = process.stdout.readline().strip()
        if not line:  # Skip empty lines
            continue
            
        parts = line.split()
        if not parts:  # Skip lines that split into empty lists
            continue
            
        if parts[0] == "bestmove":
            move = parts[1]
            process.stdin.write(f"position fen {obs.board} moves {move}\n")
            process.stdin.flush()
            return move
