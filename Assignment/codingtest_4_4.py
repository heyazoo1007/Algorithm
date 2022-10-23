from queue import PriorityQueue

def solution(start, time):
    tasks = [(st[0], st[1], i)
            for i, st in enumerate(zip(start, time))]
    
    tasks.sort(key=lambda x: (x[0], x[2]))
    
    pq = PriorityQueue()
    answer = [0 for _ in range(len(tasks))]
    idx = 0
    time = 0
    while idx < len(answer):
        while tasks and time >= tasks[0][0]:
            start_, time_, idx_ = tasks[0]
            pq.put((time_, idx_, start_))
            del tasks[0]

        if not pq.empty():
            current_task = pq.get()
            time += current_task[0]
            answer[idx] = current_task[1]
            idx += 1
        else:
            time = tasks[0][0]
            while tasks and time >= tasks[0][0]:
                start_, time_, idx_ = tasks[0]
                pq.put((time_, idx_, start_))
                del tasks[0]
    return answer
