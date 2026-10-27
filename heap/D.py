import heapq
import sys

H = []
heapq.heapify(H)

for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0].upper()
        if command == "CLEAR":
            H.clear()
        elif command == "ADD":
            n = int(parts[1])
            heapq.heappush(H, -n)
        elif command == "EXTRACT":
            if H == []:
                print("CANNOT")
            else:
                print(-heapq.heappop(H))
        