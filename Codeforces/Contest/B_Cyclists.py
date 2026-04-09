import heapq
from collections import deque
import sys

def solve():
    # Đọc nhanh toàn bộ input
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    t_cases = int(next(it))
    
    for _ in range(t_cases):
        n = int(next(it))
        k = int(next(it))
        p = int(next(it))
        m = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        
        # Lưu index của lá bài thắng (0-based)
        target_idx = p - 1
        target_val = a[target_idx]
        
        # Mô phỏng deck bằng deque chứa (giá_trị, có_phải_target_không)
        deck = deque()
        for i in range(n):
            deck.append((a[i], i == target_idx))
            
        wins = 0
        
        # Duy trì một Min-Heap chứa k lá bài đầu tiên
        # Mỗi phần tử trong heap: (giá_trị, có_phải_target_không)
        # Lưu ý: Python heap so sánh tuple, nên ta cần ép nó chọn target_val 
        # Nếu target_val nằm trong top k, Bob LUÔN chọn nó.
        
        while True:
            # Lấy k lá bài đầu tiên ra xem xét
            current_options = []
            has_target_in_k = False
            target_in_k_val = -1
            
            # Kiểm tra xem trong k lá đầu có target không
            for i in range(min(k, len(deck))):
                val, is_target = deck[i]
                if is_target:
                    has_target_in_k = True
                    target_in_k_val = val
                    target_pos_in_k = i
                    break
            
            if has_target_in_k:
                # Ưu tiên số 1: Nếu có target trong k vị trí đầu, chơi nó!
                if m >= target_in_k_val:
                    m -= target_in_k_val
                    wins += 1
                    # Xóa target khỏi vị trí cũ, đẩy xuống cuối deck
                    card = deck[target_pos_in_k]
                    del deck[target_pos_in_k]
                    deck.append(card)
                else:
                    break
            else:
                # Ưu tiên số 2: Chơi lá rẻ nhất trong k vị trí đầu để đẩy target lên
                # Tìm index của lá rẻ nhất trong k vị trí đầu
                min_val = float('inf')
                min_idx = -1
                for i in range(k):
                    if deck[i][0] < min_val:
                        min_val = deck[i][0]
                        min_idx = i
                
                if m >= min_val:
                    m -= min_val
                    # Chơi lá rẻ nhất, đẩy xuống cuối
                    card = deck[min_idx]
                    del deck[min_idx]
                    deck.append(card)
                else:
                    break
                    
        print(wins)

solve()