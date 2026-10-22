"""CSV 목록을 읽고 종류와 가격으로 검색한다. 데이터는 수업용 가상 예시다."""

import csv
from dataclasses import dataclass
from pathlib import Path

COLUMNS = ["id", "name", "category", "price"]


@dataclass(frozen=True)
class Place:
    id: str
    name: str
    category: str
    price: int


def load_catalog(directory: Path) -> list[Place]:
    """directory 바로 아래 CSV를 파일명 순서로 읽는다.

    빈 목록(헤더만 있는 CSV)은 허용한다. 잘못된 형식과 중복 ID는
    ValueError, 존재하지 않는 경로는 FileNotFoundError로 알린다.
    """
    directory = Path(directory)
    if not directory.is_dir():
        raise FileNotFoundError(f"데이터 폴더가 없습니다: {directory}")
    paths = sorted(directory.glob("*.csv"))
    if not paths:
        raise ValueError(f"CSV 파일이 없습니다: {directory}")

    places = []
    seen_ids = set()
    for path in paths:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != COLUMNS:
                raise ValueError(f"{path.name}: 헤더는 {','.join(COLUMNS)}여야 합니다.")
            for row in reader:
                location = f"{path.name}:{reader.line_num}"
                if None in row or any(row.get(key) is None for key in COLUMNS):
                    raise ValueError(f"{location}: 열 개수가 맞지 않습니다.")
                values = {key: row[key].strip() for key in COLUMNS}
                if any(not value for value in values.values()):
                    raise ValueError(f"{location}: 빈 값이 있습니다.")
                try:
                    price = int(values["price"])
                except ValueError as error:
                    raise ValueError(f"{location}: price는 정수여야 합니다.") from error
                if price < 0:
                    raise ValueError(f"{location}: price는 0 이상이어야 합니다.")
                if values["id"] in seen_ids:
                    raise ValueError(f"{location}: 중복 ID {values['id']}")
                seen_ids.add(values["id"])
                places.append(Place(values["id"], values["name"], values["category"], price))
    return places


def filter_places(places: list[Place], category: str | None = None,
                  max_price: int | None = None) -> list[Place]:
    """종류는 정확히 일치하고 가격은 상한값을 포함한다. 원본 순서를 유지한다."""
    if max_price is not None and max_price < 0:
        raise ValueError("최대 금액은 0 이상이어야 합니다.")
    return [place for place in places
            if (category is None or place.category == category)
            and (max_price is None or place.price <= max_price)]
