"""실행: python -m campus_tool --category 식사 --max-price 6000"""

import argparse
import sys
from pathlib import Path

from .catalog import filter_places, load_catalog


def main(argv=None):
    parser = argparse.ArgumentParser(description="수업용 가상 캠퍼스 목록 검색")
    parser.add_argument("--data-dir", type=Path,
                        default=Path(__file__).with_name("data"), help="CSV가 있는 폴더")
    parser.add_argument("--category", help="정확히 일치하는 종류")
    parser.add_argument("--max-price", type=int, help="최대 금액(원, 0 이상)")
    args = parser.parse_args(argv)
    try:
        places = filter_places(load_catalog(args.data_dir), args.category, args.max_price)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"오류: {error}", file=sys.stderr)
        return 2
    if not places:
        print("조건에 맞는 항목이 없습니다.")
        return 0
    print("이름\t종류\t금액(원)")
    for place in places:
        print(f"{place.name}\t{place.category}\t{place.price}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
