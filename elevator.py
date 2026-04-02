import heapq

class ElevatorSystem:
    def __init__(self):
        # We use a list to represent our heap
        self.pending_requests = [] 
        self.current_floor = 1

    def add_request(self, target_floor):
        # Calculate distance (absolute difference) to act as priority
        priority = abs(self.current_floor - target_floor)
        # Push to heap (priority, floor_number)
        heapq.heappush(self.pending_requests, (priority, target_floor))
        print(f"Added Floor {target_floor} to priority queue.")

    def process_next_request(self):
        if not self.pending_requests:
            return None
        
        # Pop the nearest floor (O(log n) operation)
        _, target_floor = heapq.heappop(self.pending_requests)
        self.current_floor = target_floor
        return target_floor

    def get_queue(self):
        # Return sorted list for UI display
        return [item[1] for item in sorted(self.pending_requests)]
