from abc import ABC, abstractmethod
from entities.nhapkho import NhapKho

class INhapKhoRepository(ABC):
    @abstractmethod
    def add(self, nhap_kho: NhapKho) -> int:
        pass

    @abstractmethod
    def get_all(self) -> list[NhapKho]:
        pass

    @abstractmethod
    def get_by_id(self, nhap_kho: int) -> NhapKho | None:
        pass

    @abstractmethod
    def update(self, nhap_kho: NhapKho):
        pass

    @abstractmethod
    def soft_delete(self, nhap_kho: int):
        pass

    @abstractmethod
    def search_nhap_kho(self, keyword: str) -> list[NhapKho]:
        pass

