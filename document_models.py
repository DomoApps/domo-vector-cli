from dataclasses import dataclass
from typing import Dict


@dataclass
class ExtractedDocument:
    text: str
    file_path: str
    metadata: Dict
    source_type: str
