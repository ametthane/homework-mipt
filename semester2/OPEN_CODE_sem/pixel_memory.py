import math
import re
import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MemorySlot:
    id: int
    content: str
    topic: str
    access_count: int = 0
    last_accessed: float = field(default_factory=time.time)
    merge_count: int = 0
    merged_ids: list[int] = field(default_factory=list)
    importance_score: float = 0.0


def tokenize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = text.split()
    return [t for t in tokens if len(t) > 2]


def tf_idf_vectorize(documents: list[str]) -> list[dict[str, float]]:
    docs = [tokenize(d) for d in documents]
    vocab = set()
    for d in docs:
        vocab.update(d)
    vocab = sorted(vocab)
    vocab_index = {w: i for i, w in enumerate(vocab)}

    idf: dict[str, float] = {}
    for w in vocab:
        doc_count = sum(1 for d in docs if w in d)
        idf[w] = math.log(len(docs) / max(1, doc_count)) + 1

    vectors: list[dict[str, float]] = []
    for d in docs:
        tf: Counter[str] = Counter(d)
        max_tf = max(tf.values()) if tf else 1
        vec: dict[str, float] = {}
        for w, count in tf.items():
            if w in vocab_index:
                vec[w] = (count / max_tf) * idf.get(w, 1)
        vectors.append(vec)

    return vectors


def cosine_similarity(v1: dict[str, float], v2: dict[str, float]) -> float:
    common = set(v1.keys()) & set(v2.keys())
    if not common:
        return 0.0
    dot = sum(v1[w] * v2[w] for w in common)
    mag1 = math.sqrt(sum(v1[w] ** 2 for w in v1))
    mag2 = math.sqrt(sum(v2[w] ** 2 for w in v2))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)


TOPIC_KEYWORDS: dict[str, list[str]] = {
    "food": ["pizza", "burger", "salad", "apple", "banana", "rice", "bread", "pasta", "cake", "soup", "chicken", "fish", "steak", "egg", "noodle", "sandwich", "fruit", "vegetable", "breakfast", "lunch", "dinner", "cook", "taste", "yummy", "delicious", "favorite", "meal", "snack", "dessert", "honey", "lemon", "orange", "grape", "berry", "tomato", "potato", "onion", "garlic", "pepper", "salt", "sugar", "chocolate", "ice cream", "coffee", "tea", "juice", "milk", "cheese", "butter", "recipe", "kitchen"],
    "weather": ["rain", "sunny", "cloudy", "wind", "snow", "cold", "hot", "warm", "cool", "storm", "thunder", "lightning", "fog", "humid", "dry", "wet", "rainy", "sunshine", "temperature", "degree", "forecast", "climate", "season", "spring", "summer", "autumn", "winter", "morning", "afternoon", "evening", "night", "sunrise", "sunset", "hail", "sleet", "breeze", "shower", "drizzle", "umbrella", "jacket", "coat", "scarf", "gloves"],
    "family": ["mom", "dad", "mother", "father", "sister", "brother", "grandma", "grandpa", "grandmother", "grandfather", "aunt", "uncle", "cousin", "family", "parent", "child", "baby", "daughter", "son", "husband", "wife", "home", "house", "birthday", "celebrate", "party", "holiday", "vacation", "trip", "visit", "call", "love", "miss", "hug", "kiss", "dinner", "lunch", "breakfast", "together"],
    "school": ["teacher", "class", "homework", "study", "exam", "test", "lesson", "book", "pencil", "pen", "notebook", "desk", "chair", "school", "student", "friend", "math", "science", "history", "english", "art", "music", "sport", "playground", "bus", "backpack", "report", "grade", "score", "learn", "read", "write", "draw", "run", "jump", "team", "club", "library", "principal"],
    "health": ["sleep", "exercise", "run", "walk", "doctor", "medicine", "headache", "stomach", "pain", "hurt", "rest", "water", "healthy", "sick", "fever", "cold", "cough", "vitamin", "gym", "yoga", "stretch", "heart", "body", "strong", "energy", "tired", "weak", "fit", "weight", "diet", "tooth", "toothbrush", "wash", "clean", "bath", "shower", "hair", "skin", "eye", "ear", "nose", "mouth"],
    "hobbies": ["draw", "paint", "game", "play", "toy", "book", "read", "music", "song", "sing", "dance", "craft", "build", "lego", "puzzle", "bike", "swim", "skate", "ball", "football", "basketball", "tennis", "soccer", "video", "movie", "watch", "tv", "photo", "camera", "collect", "hobby", "fun", "enjoy", "free", "summer", "park", "beach", "camp", "nature", "animal", "pet", "dog", "cat", "fish", "bird"],
}


def detect_topic(text: str) -> str:
    text_lower = text.lower()
    best_topic = "general"
    best_score = 0
    for topic, keywords in TOPIC_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > best_score:
            best_score = score
            best_topic = topic
    return best_topic


class Embedder:
    def __init__(self):
        self.documents: list[str] = []
        self.vectors: list[dict[str, float]] = []
        self._dirty = True

    def fit(self, texts: list[str]):
        self.documents = list(texts)
        self.vectors = tf_idf_vectorize(self.documents)
        self._dirty = False

    def add_text(self, text: str) -> int:
        self.documents.append(text)
        self._dirty = True
        return len(self.documents) - 1

    def _ensure_fitted(self):
        if self._dirty or not self.vectors:
            self.vectors = tf_idf_vectorize(self.documents)
            self._dirty = False

    def transform(self, texts: list[str]) -> list[dict[str, float]]:
        if not self.documents and texts:
            self.fit(texts)
        elif texts:
            combined = self.documents + texts
            self.vectors = tf_idf_vectorize(combined)
        else:
            return []
        return self.vectors

    def similarity(self, text1: str, text2: str) -> float:
        vec = tf_idf_vectorize([text1, text2])
        if len(vec) < 2:
            return 0.0
        return cosine_similarity(vec[0], vec[1])

    def similarities(self, query: str, texts: list[str]) -> list[float]:
        if not texts:
            return []
        vec = tf_idf_vectorize([query] + texts)
        if len(vec) < 2:
            return [0.0] * len(texts)
        qv = vec[0]
        sims = [cosine_similarity(qv, tv) for tv in vec[1:]]
        return sims


class PixelMemory:
    MAX_SLOTS = 10
    MAX_MERGES_PER_SLOT = 5
    MERGE_SIMILARITY_THRESHOLD = 0.30

    WEIGHT_ACCESS = 0.30
    WEIGHT_RECENCY = 0.20
    WEIGHT_DIVERSITY = 0.20
    WEIGHT_MERGE = 0.15
    WEIGHT_TOPIC_FREQ = 0.15

    def __init__(self):
        self.slots: list[MemorySlot] = []
        self.next_id = 1
        self.embedder = Embedder()
        self.topic_counter: Counter[str] = Counter()
        self.fact_count = 0
        self._total_queries = 0
        self._correct_queries = 0

    def _compute_priority(self, slot: MemorySlot) -> float:
        now = time.time()
        age_hours = max(1.0, (now - slot.last_accessed) / 3600.0)
        recency = 1.0 / age_hours

        total_in_memory = len(self.slots)
        topic_count = self.topic_counter.get(slot.topic, 0)
        topic_freq = (total_in_memory - topic_count) / max(1, total_in_memory)

        topics_present = set(s.topic for s in self.slots if s is not slot)
        diversity = 1.0 / max(1, len(topics_present))

        recency_of_access = min(1.0, 1.0 / max(1.0, age_hours))
        score = (
            self.WEIGHT_ACCESS * min(slot.access_count / max(1, self.fact_count), 1.0) +
            recency_of_access * 0.5 +
            self.WEIGHT_RECENCY * recency +
            self.WEIGHT_DIVERSITY * diversity +
            self.WEIGHT_MERGE * min(slot.merge_count / 5.0, 1.0) +
            self.WEIGHT_TOPIC_FREQ * topic_freq
        )
        return score

    def _find_related(self, fact: str) -> tuple[int, float] | tuple[None, None]:
        if len(self.slots) == 0:
            return None, None

        fact_topic = detect_topic(fact)
        texts = [s.content for s in self.slots]
        sims = self.embedder.similarities(fact, texts)

        best_idx = None
        best_score = -1.0

        for i, slot in enumerate(self.slots):
            same_topic = 1.0 if (fact_topic == slot.topic or fact_topic in slot.topic) else 0.0
            merge_penalty = 0.5 if slot.merge_count >= self.MAX_MERGES_PER_SLOT else 0.0
            score = sims[i] + same_topic * 0.5 - merge_penalty
            if score > best_score:
                best_score = score
                best_idx = i

        if best_score >= self.MERGE_SIMILARITY_THRESHOLD:
            return best_idx, float(best_score)
        return None, None

    def _evict(self) -> int | None:
        if len(self.slots) == 0:
            return None

        candidates = [(slot, self._compute_priority(slot)) for slot in self.slots]
        candidates.sort(key=lambda x: x[1])
        victim = candidates[0][0]

        idx = next(i for i, s in enumerate(self.slots) if s.id == victim.id)
        self.slots.pop(idx)
        self.topic_counter.subtract([victim.topic])
        return victim.id

    def _merge(self, slot: MemorySlot, new_fact: str, new_topic: str):
        slot.content += " [SEP] " + new_fact
        old_topic = slot.topic
        combined_topic = detect_topic(slot.content)
        if combined_topic != old_topic:
            self.topic_counter.subtract([old_topic])
            slot.topic = combined_topic
        slot.merge_count += 1
        slot.merged_ids.append(self.next_id)
        slot.last_accessed = time.time()
        self.next_id += 1

    def add(self, fact: str) -> tuple[str, str]:
        self.fact_count += 1
        new_topic = detect_topic(fact)

        if len(self.slots) < self.MAX_SLOTS:
            slot = MemorySlot(
                id=self.next_id,
                content=fact,
                topic=new_topic,
                importance_score=0.0,
            )
            self.slots.append(slot)
            self.topic_counter[new_topic] += 1
            self.next_id += 1
            self.embedder.add_text(fact)
            return "stored", new_topic

        related_idx, sim = self._find_related(fact)
        if related_idx is not None:
            slot = self.slots[related_idx]
            old_topic = slot.topic
            self._merge(slot, fact, new_topic)
            if old_topic != slot.topic:
                self.topic_counter[slot.topic] += 1
            else:
                self.topic_counter[old_topic] += 1
            self.embedder.add_text(fact)
            return "merged", slot.topic

        victim_id = self._evict()
        new_slot = MemorySlot(
            id=self.next_id,
            content=fact,
            topic=new_topic,
            importance_score=0.0,
        )
        self.slots.append(new_slot)
        self.topic_counter[new_topic] += 1
        self.next_id += 1
        self.embedder.add_text(fact)
        return "evicted", new_topic

    def query(self, question: str) -> tuple[Optional[str], float]:
        self._total_queries += 1

        if len(self.slots) == 0:
            return None, 0.0

        query_topic = detect_topic(question)
        texts = [s.content for s in self.slots]
        sims = self.embedder.similarities(question, texts)

        best_idx = None
        best_score = -1.0

        for i, slot in enumerate(self.slots):
            topic_match = 1.0 if query_topic == slot.topic else 0.0
            access_boost = min(slot.access_count * 0.05, 0.5)
            score = sims[i] + topic_match * 0.4 + access_boost
            if score > best_score:
                best_score = score
                best_idx = i

        best_slot = self.slots[best_idx]
        best_slot.access_count += 1
        best_slot.last_accessed = time.time()

        primary_topic = query_topic if query_topic != "general" else best_slot.topic
        return primary_topic, float(best_score)

    def get_memory_snapshot(self) -> list[dict]:
        return [{
            "id": s.id,
            "content": s.content[:60] + ("..." if len(s.content) > 60 else ""),
            "topic": s.topic,
            "access_count": s.access_count,
            "merge_count": s.merge_count,
        } for s in self.slots]

    def accuracy_stats(self) -> dict:
        rate = self._correct_queries / max(1, self._total_queries)
        return {
            "total": self._total_queries,
            "correct": self._correct_queries,
            "rate": rate,
        }

    def record_correct(self):
        self._correct_queries += 1