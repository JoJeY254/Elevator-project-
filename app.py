from flask import Flask, send_from_directory, request, jsonify
from collections import deque
import heapq

app = Flask(__name__, static_folder='.')

# State storage
request_queue = deque()  # Queue for FIFO logic
priority_queue = []      # Min-Heap for "Nearest Floor" logic

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/api/request', methods=['POST'])
def handle_request():
    floor = request.json.get('floor')
    request_queue.append(floor)
    heapq.heappush(priority_queue, floor) # Logically prioritizing
    return jsonify({"status": "Added", "queue": list(request_queue)})

@app.route('/api/next_move', methods=['GET'])
def get_next_move():
    if priority_queue:
        target = heapq.heappop(priority_queue)
        return jsonify({"target_floor": target})
    return jsonify({"target_floor": None})

if __name__ == '__main__':
    app.run(debug=True)