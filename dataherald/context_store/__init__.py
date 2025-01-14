import os
from abc import ABC, abstractmethod
from typing import Any, List

from dataherald.config import Component, System
from dataherald.db import DB
from dataherald.types import GoldenRecord, GoldenRecordRequest, NLQuery
from dataherald.vector_store import VectorStore


class ContextStore(Component, ABC):
    DocStore: DB
    VectorStore: VectorStore
    doc_store_collection = "table_meta_data"

    @abstractmethod
    def __init__(self, system: System):
        self.system = system
        self.db = self.system.instance(DB)
        self.golden_record_collection = os.environ.get(
            "GOLDEN_RECORD_COLLECTION", "dataherald-staging"
        )
        self.vector_store = self.system.instance(VectorStore)

    @abstractmethod
    def retrieve_context_for_question(
        self, nl_question: NLQuery, number_of_samples: int = 3
    ) -> List[dict] | None:
        pass

    @abstractmethod
    def add_golden_records(
        self, golden_records: List[GoldenRecordRequest]
    ) -> List[GoldenRecord]:
        pass

    @abstractmethod
    def remove_golden_records(self, ids: List) -> bool:
        pass
