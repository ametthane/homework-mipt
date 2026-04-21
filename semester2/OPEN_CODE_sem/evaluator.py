import random
import sys
from dataclasses import dataclass


@dataclass
class FactRecord:
    text: str
    topic: str
    is_key: bool


@dataclass
class QueryRecord:
    text: str
    expected_topic: str
    source_fact_id: int
    is_hard: bool


KEY_FACTS: list[FactRecord] = [
    FactRecord("My favorite food is pepperoni pizza with extra cheese", "food", True),
    FactRecord("The weather today is sunny and warm, about 25 degrees", "weather", True),
    FactRecord("My mom bakes delicious chocolate chip cookies every Sunday", "family", True),
    FactRecord("I have a math test tomorrow on fractions and decimals", "school", True),
    FactRecord("Running in the morning gives me lots of energy for the day", "health", True),
    FactRecord("I love playing soccer with my friends at the park", "hobbies", True),
    FactRecord("My favorite food is fresh garden salad with vinaigrette dressing", "food", True),
    FactRecord("It rained heavily yesterday and the temperature dropped to 10 degrees", "weather", True),
    FactRecord("My dad taught me how to ride a bike without training wheels", "family", True),
    FactRecord("The science fair project needs to be finished by Friday", "school", True),
    FactRecord("Drinking eight glasses of water daily keeps me healthy", "health", True),
    FactRecord("I collect trading cards and keep them in a special binder", "hobbies", True),
    FactRecord("My favorite food is crispy fried chicken with mashed potatoes", "food", True),
    FactRecord("A snowstorm is expected this weekend with heavy accumulation", "weather", True),
    FactRecord("My grandma knits warm scarves and gives them as birthday gifts", "family", True),
    FactRecord("The history essay about ancient Egypt got an A grade", "school", True),
    FactRecord("I do yoga stretches every morning to stay flexible", "health", True),
    FactRecord("Building with Lego blocks is my favorite weekend activity", "hobbies", True),
    FactRecord("My favorite food is a big bowl of fruity breakfast cereal with milk", "food", True),
    FactRecord("Thunder and lightning were reported across the city this afternoon", "weather", True),
]

FILLER_FACTS: list[FactRecord] = [
    FactRecord("Apples are rich in fiber and make a great healthy snack", "food", False),
    FactRecord("Raincoats help keep you dry when walking in the rain", "weather", False),
    FactRecord("Families often gather for dinner during holidays", "family", False),
    FactRecord("Pencils are useful tools for sketching and drawing", "school", False),
    FactRecord("Taking breaks during study sessions improves focus", "health", False),
    FactRecord("Photography captures special moments in time", "hobbies", False),
    FactRecord("Bread serves as the base for many delicious sandwiches", "food", False),
    FactRecord("Weather forecasts help people plan outdoor activities", "weather", False),
    FactRecord("Family traditions create lasting memories for everyone", "family", False),
    FactRecord("Reading books expands vocabulary and knowledge", "school", False),
    FactRecord("A balanced diet includes fruits vegetables and grains", "health", False),
    FactRecord("Music brings joy and can lift everyone's mood", "hobbies", False),
    FactRecord("Pasta comes in many different shapes and sizes", "food", False),
    FactRecord("Cloudy skies sometimes signal an approaching rainstorm", "weather", False),
    FactRecord("Family game nights strengthen bonds between members", "family", False),
    FactRecord("Homework helps reinforce lessons learned in class", "school", False),
    FactRecord("Regular exercise improves both physical and mental health", "health", False),
    FactRecord("Playing video games can be a fun group activity", "hobbies", False),
    FactRecord("Honey is a natural sweetener used in many recipes", "food", False),
    FactRecord("Morning dew forms on grass blades during cool nights", "weather", False),
    FactRecord("Siblings often share a bedroom in family homes", "family", False),
    FactRecord("Libraries provide free access to books and resources", "school", False),
    FactRecord("Walking barefoot on grass feels relaxing and grounding", "health", False),
    FactRecord("Painting allows expression of creativity and imagination", "hobbies", False),
    FactRecord("Grapes grow on vines and come in red or green varieties", "food", False),
    FactRecord("Humid weather makes the air feel heavier and warmer", "weather", False),
    FactRecord("Family reunions bring together relatives from far away places", "family", False),
    FactRecord("Field trips make learning more interesting and memorable", "school", False),
    FactRecord("Stretching before bed helps the body relax and unwind", "health", False),
    FactRecord("Puzzles challenge the mind and provide entertainment", "hobbies", False),
    FactRecord("Pizza restaurants offer many topping choices and combinations", "food", False),
    FactRecord("Wind speed increases during storms and tropical weather events", "weather", False),
    FactRecord("Family recipes are often passed down through generations", "family", False),
    FactRecord("Group projects in school teach teamwork and collaboration", "school", False),
    FactRecord("Deep breathing exercises reduce stress and calm the mind", "health", False),
    FactRecord("Bird watching connects people with nature and wildlife", "hobbies", False),
    FactRecord("Oranges are packed with vitamin C and boost immunity", "food", False),
    FactRecord("Spring weather brings blooming flowers and warmer days", "weather", False),
    FactRecord("Phone calls help family members stay connected", "family", False),
    FactRecord("Flashcards are a popular study tool for memorization", "school", False),
    FactRecord("Laughing with friends releases endorphins and reduces pain", "health", False),
    FactRecord("Swimming is both a fun recreational activity and great exercise", "hobbies", False),
    FactRecord("Chocolate cake is a popular dessert for celebrations", "food", False),
    FactRecord("Fog reduces visibility and requires careful driving", "weather", False),
    FactRecord("Family celebrations bring people together with joy", "family", False),
    FactRecord("Note-taking during class helps retain important information", "school", False),
    FactRecord("Adequate sleep of eight hours supports proper brain function", "health", False),
    FactRecord("Craft projects encourage creativity and fine motor skills", "hobbies", False),
    FactRecord("Tomatoes are technically a fruit used in cooking and salads", "food", False),
    FactRecord("Seasonal weather changes affect daily routines and clothing choices", "weather", False),
    FactRecord("Family pets provide companionship and unconditional love", "family", False),
    FactRecord("The school library has thousands of books across many subjects", "school", False),
    FactRecord("Vitamin D from sunlight supports strong bones and teeth", "health", False),
    FactRecord("Dancing combines physical movement with musical rhythm and expression", "hobbies", False),
]


QUERY_TEMPLATES: list[str] = [
    "what is my favorite food",
    "what is the weather like",
    "what did my mom bake",
    "when is my math test",
    "why do I run in the morning",
    "what sport do I play",
    "tell me about my favorite meal",
    "was it rainy yesterday",
    "who taught me to ride a bike",
    "when is the science fair",
    "how much water should I drink",
    "what do I collect",
    "tell me about my favorite food",
    "what weather is expected",
    "what does my grandma make",
    "how did my essay do",
    "why do I do yoga",
    "what do I build for fun",
    "what is my favorite breakfast",
    "what happened this afternoon",
]


class Evaluator:
    def __init__(self, key_facts: list[FactRecord] = KEY_FACTS, filler_facts: list[FactRecord] = FILLER_FACTS):
        self.key_facts = key_facts
        self.filler_facts = filler_facts
        self.queries: list[QueryRecord] = []
        self._build_queries()

    def _build_queries(self):
        for i, fact in enumerate(self.key_facts):
            template = QUERY_TEMPLATES[i % len(QUERY_TEMPLATES)]
            self.queries.append(QueryRecord(
                text=template,
                expected_topic=fact.topic,
                source_fact_id=i,
                is_hard=False,
            ))

    def generate_stream(self, total: int = 50, seed: int = 42) -> list[FactRecord]:
        random.seed(seed)
        key_copy = list(self.key_facts)
        filler_copy = list(self.filler_facts)
        random.shuffle(key_copy)
        random.shuffle(filler_copy)

        stream: list[FactRecord] = []
        key_idx = 0
        filler_idx = 0
        for i in range(total):
            use_key = i < len(key_copy) and (i % 3 == 0 or key_idx < len(key_copy))
            if use_key and key_idx < len(key_copy):
                stream.append(key_copy[key_idx])
                key_idx += 1
            elif filler_idx < len(filler_copy):
                stream.append(filler_copy[filler_idx])
                filler_idx += 1
            elif key_idx < len(key_copy):
                stream.append(key_copy[key_idx])
                key_idx += 1

        random.shuffle(stream)
        return stream

    def get_test_queries(self, all_facts: list[FactRecord]) -> list[QueryRecord]:
        test_queries: list[QueryRecord] = []
        for i, fact in enumerate(self.key_facts):
            template = QUERY_TEMPLATES[i % len(QUERY_TEMPLATES)]
            test_queries.append(QueryRecord(
                text=template,
                expected_topic=fact.topic,
                source_fact_id=i,
                is_hard=True,
            ))
        return test_queries

    def run_accuracy_test(self, memory, test_queries: list[QueryRecord]) -> dict:
        results: dict[int, bool] = {}
        for q in test_queries:
            returned_topic, confidence = memory.query(q.text)
            correct = returned_topic == q.expected_topic
            if correct:
                memory.record_correct()
            results[q.source_fact_id] = correct
        return results

    def print_results_table(self, stats: list[dict], total_correct: int, total_queries: int, all_pass: bool, threshold: float = 0.65):
        print()
        print("=" * 72)
        print("  PIXEL MEMORY ACCURACY REPORT")
        print("=" * 72)
        print()
        print(f"  {'Window':<10} {'Queries':<10} {'Correct':<10} {'Accuracy':<12} {'Status'}")
        print(f"  {'-'*9:<1} {'-'*9:<1} {'-'*9:<1} {'-'*11:<1} {'-'*7}")
        for s in stats:
            mark = "PASS" if s["accuracy"] >= threshold else "FAIL"
            print(f"  {s['window']:<10} {s['queries']:<10} {s['correct']:<10} {s['accuracy']*100:>6.1f}%    {mark}")

        overall = total_correct / max(1, total_queries)
        mark = "PASS" if overall >= threshold else "FAIL"
        print(f"  {'-'*9:<1} {'-'*9:<1} {'-'*9:<1} {'-'*11:<1} {'-'*7}")
        print(f"  {'OVERALL':<10} {total_queries:<10} {total_correct:<10} {overall*100:>6.1f}%    {mark}")
        print()
        print(f"  Accuracy threshold: {threshold*100:.0f}%")
        print(f"  All windows stable:     {'YES' if all_pass else 'NO'}")
        print()
        if overall >= threshold and all_pass:
            print("  RESULT: PASS - Pixel memory meets all requirements")
        else:
            print("  RESULT: FAIL - Pixel memory did not meet requirements")
        print("=" * 72)
        print()