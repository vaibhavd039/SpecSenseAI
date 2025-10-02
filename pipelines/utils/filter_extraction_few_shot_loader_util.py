from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
import re
from typing import List, Tuple
FEWSHOTS_DIR   = Path(__file__).parent / "filter_extraction_examples"


USER_RE  = re.compile(r"^\s*USER:\s*(.*)$", re.DOTALL | re.MULTILINE)

ASS_RE   = re.compile(r"^\s*ASSISTANT:\s*(.*)$", re.DOTALL | re.MULTILINE)

def _parse_pair(text: str) -> Tuple[str, str]:

    """Extract (user, assistant) from a simple text file with USER:/ASSISTANT: blocks."""

    u = USER_RE.search(text)

    a = ASS_RE.search(text)

    if not u or not a:

        raise ValueError("Few-shot file must contain USER: and ASSISTANT: blocks.")

    return u.group(1).strip(), a.group(1).strip()


def _load_filter_extraction_few_shot_prompt() -> List[Tuple[str, str]]:

    """Load up to MAX_FEWSHOTS *.txt files from FEWSHOTS_DIR, in name order."""

    if not FEWSHOTS_DIR.exists():

        return []

    pairs: List[Tuple[str, str]] = []

    for p in sorted(FEWSHOTS_DIR.glob("*.txt")):

        try:

            pairs.append(_parse_pair(p.read_text(encoding="utf-8")))

        except Exception as e:

            # Keep it simple: skip bad files but don't crash

            print(f"[fewshots] Skipping {p.name}: {e}")

    return pairs

response = _load_filter_extraction_few_shot_prompt();
print (response)