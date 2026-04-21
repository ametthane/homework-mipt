import sys
import random
from dataclasses import dataclass

from pixel_memory import PixelMemory
from evaluator import Evaluator, QueryRecord, FactRecord


@dataclass
class WindowStat:
    window: str
    queries: int
    correct: int
    accuracy: float


def run_evaluation(
    total_facts: int = 50,
    stream_seed: int = 42,
    query_seed: int = 7,
    threshold: float = 0.65,
    verbose: bool = True,
):
    evaluator = Evaluator()
    memory = PixelMemory()

    stream = evaluator.generate_stream(total=total_facts, seed=stream_seed)

    all_facts: list[FactRecord] = list(evaluator.key_facts) + list(evaluator.filler_facts)
    fact_by_id = {i: f for i, f in enumerate(all_facts)}

    key_fact_ids = set(i for i, f in enumerate(evaluator.key_facts))
    evicted_ids: set[int] = set()

    if verbose:
        print()
        print("=" * 72)
        print("  PIXEL LEARNS: FACT STREAM PROCESSING")
        print("=" * 72)
        print()
        print(f"  {'#':<4} {'Fact':<60} {'Action':<8}")
        print(f"  {'-'*3:<1} {'-'*59:<1} {'-'*7:<1}")

    for i, fact in enumerate(stream):
        fid = all_facts.index(fact)
        action, topic = memory.add(fact.text)

        if action == "evicted" and verbose:
            evicted_ids.add(fid)

        if verbose and i < 20:
            preview = fact.text[:57] + ("..." if len(fact.text) > 57 else "")
            print(f"  {i+1:<3}  {preview:<60} {action:<8}")

    if verbose and total_facts > 20:
        print(f"  ... ({total_facts - 20} more facts processed)")

    test_queries = evaluator.get_test_queries(all_facts)
    random.seed(query_seed)
    random.shuffle(test_queries)

    window_size = 10
    total_correct = 0
    total_queries = 0
    window_stats: list[WindowStat] = []
    all_windows_pass = True

    for w_start in range(0, len(test_queries), window_size):
        w_end = w_start + window_size
        w_queries = test_queries[w_start:w_end]
        w_correct = 0
        for q in w_queries:
            returned_topic, _ = memory.query(q.text)
            if returned_topic == q.expected_topic:
                w_correct += 1
                memory.record_correct()

        total_correct += w_correct
        total_queries += len(w_queries)
        acc = w_correct / max(1, len(w_queries))
        window_num = (w_start // window_size) + 1
        window_stats.append(WindowStat(
            window=f"Window {window_num}",
            queries=len(w_queries),
            correct=w_correct,
            accuracy=acc,
        ))
        if acc < threshold:
            all_windows_pass = False

    evaluator.print_results_table(
        stats=[
            {"window": ws.window, "queries": ws.queries, "correct": ws.correct, "accuracy": ws.accuracy}
            for ws in window_stats
        ],
        total_correct=total_correct,
        total_queries=total_queries,
        all_pass=all_windows_pass,
        threshold=threshold,
    )

    if verbose:
        print()
        print("  Memory snapshot (topics stored):")
        print()
        snapshot = memory.get_memory_snapshot()
        for i, slot in enumerate(snapshot):
            print(f"    Slot {i+1:<2} | Topic: {slot['topic']:<12} | Merges: {slot['merge_count']} | Access: {slot['access_count']} | {slot['content']}")
        print()

    overall_acc = total_correct / max(1, total_queries)
    return overall_acc >= threshold and all_windows_pass, overall_acc


if __name__ == "__main__":
    passed, accuracy = run_evaluation(
        total_facts=50,
        stream_seed=42,
        query_seed=7,
        threshold=0.65,
        verbose=True,
    )
    sys.exit(0 if passed else 1)