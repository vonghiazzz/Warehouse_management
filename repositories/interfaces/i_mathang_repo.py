from abc import ABC, abstractmethod
from entities.mathang import MatHang

class IMatHangRepository(ABC):
    @abstractmethod
    def add(self, mat_hang: MatHang):
        pass

    @abstractmethod
    def get_all(self) -> list[MatHang]:
        pass

    @abstractmethod
    def get_by_id(self, ma_hang: int) -> MatHang | None:
        pass

    @abstractmethod
    def update(self, mat_hang: MatHang):
        pass

    @abstractmethod
    def soft_delete(self, ma_hang: int):
        pass