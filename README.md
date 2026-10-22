# 오픈소스프로그래밍 협업 실습

[![Python practice checks](https://github.com/Jinwoo-Han/opensource_test_repo/actions/workflows/tests.yml/badge.svg)](https://github.com/Jinwoo-Han/opensource_test_repo/actions/workflows/tests.yml)

작은 Python 프로그램을 함께 개선하며 **Issue → branch → PR → 리뷰 → 수정 → merge**를 연습합니다. 모든 예시 장소와 금액은 수업을 위해 만든 가상 데이터입니다.

## 어디서 시작하나요?

| 지금 할 일 | 안내 |
|---|---|
| 9~14주차 전체 흐름 확인 | [수업 계획](docs/course-plan.md) |
| GitHub 저장소 처음 연결 | [9주차](labs/week09.md) |
| branch·merge·PR·충돌 연습 | [10주차](labs/week10.md) |
| 이 저장소에 첫 기여 | [11주차](labs/week11.md), [CONTRIBUTING](CONTRIBUTING.md) |
| 맡을 작업 고르기 | [기여 과제](docs/tasks.md), [열린 Issue](https://github.com/Jinwoo-Han/opensource_test_repo/issues) |
| 다른 학생의 PR 검토 | [리뷰 안내](docs/review-guide.md) |
| 팀 프로젝트 진행 | [12주차](labs/week12.md) · [13주차](labs/week13.md) · [14주차](labs/week14.md) |
| 수업 운영 | [교수자 안내](docs/instructor-guide.md) |

## 실행하기

Python 3.10 이상과 Git이 필요합니다. 아래 명령은 **Ubuntu Bash**, 저장소 최상위 폴더 기준입니다. Python 실행 코드에는 별도 외부 라이브러리가 필요하지 않으며, 설치 과정에서는 pip가 빌드 도구를 내려받을 수 있습니다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m campus_tool
python -m campus_tool --category 식사 --max-price 6000
python -m campus_tool --data-dir examples/submissions
python -m unittest discover -s tests -v
```

`venv`가 없다는 오류는 Ubuntu의 `python3-venv` 패키지 설치 상태를 교수자와 확인합니다. 패키지는 활성화한 가상환경 안에 설치합니다. 프로그램 옵션은 `python -m campus_tool --help`로 확인합니다.

기본 프로그램은 CSV 목록을 읽고 **종류 일치 / 최대 금액 이하**로 검색합니다. 첫 명령에는 가상 항목 세 개가 나옵니다. `--data-dir examples/submissions`는 학생 기여 파일을 모두 읽습니다. 필터와 일치하지 않으면 `조건에 맞는 항목이 없습니다.`를 출력합니다. 잘못된 데이터는 오류 메시지와 종료 코드 2로 알립니다.

## 첫 기여

1. 본인 계정으로 **Fork**하고 로컬에 clone합니다.
2. [기여 과제](docs/tasks.md)에서 시작 과제를 고릅니다.
3. 새 branch에서 `examples/submissions/<별칭>.csv` 하나를 추가합니다.
4. 프로그램과 테스트를 실행하고 원본 저장소의 `main`으로 PR을 보냅니다.
5. 짝의 PR을 읽고 실행 결과를 바탕으로 리뷰합니다. 받은 의견을 반영합니다.

9~10주차의 개인 연습 저장소, 이 공통 기여 저장소, 12주차 이후 팀 저장소는 역할이 다릅니다. 11주차에는 **Fork**, 팀 프로젝트를 새로 시작할 때는 **Use this template**을 사용합니다. 팀 저장소에서는 팀의 `main`으로 PR을 보냅니다.

## 공개 범위와 완료 기준

- 수업 안내·예제·학생 기여·팀 프로젝트는 공개를 기본으로 합니다. 학번, 성적, 연락처, 인증 정보는 올리지 않습니다. 제출·평가 정보는 LMS로 전달합니다.
- 코드는 작은 변경 단위로 제안합니다. 공통 `main` 병합은 교수자/관리자가 맡습니다. 일반 기여자는 원본에 직접 push할 필요가 없습니다.
- 완료 증거는 **본인의 PR URL, 다른 학생에게 남긴 리뷰, 실제 실행 결과, 변경 이유 설명**입니다. CI 성공은 성적 확정이나 정식 승인과 같지 않습니다.
- 다른 사람의 코드·데이터는 출처와 이용 조건을 확인합니다. 이번 데이터 과제는 직접 만든 가상 자료를 사용합니다.

코드와 직접 작성한 예시는 기존 [MIT LICENSE](LICENSE)를 따릅니다. 다른 팀이 재사용할 때도 해당 고지를 유지합니다.
