from abc import ABC, abstractmethod
from entities.nhapkho import NhapKho

class INhapKhoService(ABC):
    @abstractmethod
    def add_nhap_kho(self, nhap_kho: NhapKho) -> bool:
        pass

    @abstractmethod
    def get_all_nhap_kho(self) -> list[NhapKho]:
        pass

    @abstractmethod
    def get_nhap_kho_by_id(self, nhap_kho: int) -> NhapKho | None:
        pass

    @abstractmethod
    def update_nhap_kho(self, nhap_kho: NhapKho) -> bool:
        pass

    @abstractmethod
    def delete_nhap_kho(self, nhap_kho: int) -> bool:
        pass

    @abstractmethod
    def search_nhap_kho(self, keyword: str) -> list[NhapKho]:
        pass

    @abstractmethod
    def validate_nhap_kho(self, data: NhapKho):
        pass