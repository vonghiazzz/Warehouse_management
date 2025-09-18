from abc import ABC, abstractmethod
from typing import List, Optional
from entities.mathang import MatHang

class IMatHangRepo(ABC):
    @abstractmethod
    def add(self, item: MatHang) -> MatHang: ...
    @abstractmethod
    def get_all(self) -> List[MatHang]: ...
    @abstractmethod
    def get_by_name(self, tenhang: str) -> Optional[MatHang]: ...
