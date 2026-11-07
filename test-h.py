# Code from Gemini

# test_harness.py - Simple, zero-parser test harness
import cantorpairs as cp
import time

def run_tests():
    print("--- 1. Testing Immutability & Copy-on-Write ---")
    seq1 = cp.pair(10, 20)
    seq2 = cp.update(seq1, 0, 99) # Or cp.Update combinator
    
    assert cp.left(seq1) == 10, "FAIL: Original sequence was mutated!"
    assert cp.left(seq2) == 99, "FAIL: Updated sequence has wrong value!"
    print("PASS: Immutability preserved.")

    print("\n--- 2. Testing Lazy Integer Conversion ---")
    # Forces Cantor unpair on legacy engine, O(1) fetch on dict engine
    val = cp.left(seq2)
    assert cp.to_int(val) == 99, "FAIL: Lazy sync failed!"
    print("PASS: Synchronization working.")

    print("\n--- 3. Sequence Update Benchmark ---")
    start = time.time()
    s = cp.from_list(list(range(500))) # Build 500-element sequence
    for i in range(100):
        s = cp.update(s, i, i * 2)
    elapsed = time.time() - start
    print(f"PASS: 100 updates completed in {elapsed:.4f}s")

if __name__ == "__main__":
    run_tests()

