from abc import ABC, abstractmethod
from entities.mathang import MatHang

class IMatHangService(ABC):
    @abstractmethod
    def add_mat_hang(self, mat_hang: MatHang) -> bool:
        pass

    @abstractmethod
    def get_all_mat_hang(self) -> list[MatHang]:
        pass

    @abstractmethod
    def get_mat_hang_by_id(self, ma_hang: int) -> MatHang | None:
        pass

    @abstractmethod
    def update_mat_hang(self, mat_hang: MatHang) -> bool:
        pass

    @abstractmethod
    def delete_mat_hang(self, ma_hang: int) -> bool:
        pass

    @abstractmethod
    def validate_mat_hang(self, data: MatHang, create: bool) -> list[str]:
        pass