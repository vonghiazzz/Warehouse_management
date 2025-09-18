from dataclasses import dataclass
from typing import Optional

@dataclass
class MatHang:
    mahang: Optional[int] = None
    tenhang: str = ""

    def validate(self):
        if not self.tenhang.strip():
            raise ValueError("Tên hàng không được rỗng")

    @classmethod
    def from_row(cls, row: tuple):
        return cls(mahang=row[0], tenhang=row[1])

    def to_row_insert(self):
        return (self.tenhang,)
