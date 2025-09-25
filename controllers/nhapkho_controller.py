from CTO.nhapkho_history_dto import NhapKhoHistoryDTO
from services.nhapkho_service import NhapKhoService
from entities.nhapkho import NhapKho

class NhapKhoController:
    def __init__(self):
        self.service = NhapKhoService()

    def validate_nhap_kho(self, data: NhapKho):
        return self.service.validate_nhap_kho(data)

    def add_nhap_kho(self, nhap_kho: NhapKho) -> int:
        return self.service.add_nhap_kho(nhap_kho)
    
    def get_all_nhap_kho(self) -> list[NhapKho]:
        return self.service.get_all_nhap_kho()
    
    def get_nhap_kho_by_id(self, nhap_kho: int) -> NhapKho | None:
        return self.service.get_nhap_kho_by_id(nhap_kho)

    def get_history_by_mat_hang(self, ma_hang: int) -> list[NhapKhoHistoryDTO]:
        return self.service.get_history_by_mat_hang(ma_hang)

    def update_nhap_kho(self, id: int, nhap_kho: NhapKho) -> bool:
        return self.service.update_nhap_kho(id, nhap_kho)
    
    def delete_nhap_kho(self, nhap_kho: int) -> bool:
        return self.service.delete_nhap_kho(nhap_kho)

    def search_nhap_kho(self, keyword: str) -> list[NhapKho]:
        return self.service.search_nhap_kho(keyword)