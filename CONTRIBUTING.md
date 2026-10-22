# 기여 절차

이 저장소는 공개된 수업용 프로젝트입니다. 처음에는 [11주차 안내](labs/week11.md)의 CSV 과제로 전체 흐름을 경험하고, 이후 [기여 과제](docs/tasks.md)에서 코드·문서·테스트 과제를 선택합니다.

## 변경하기 전

- README, LICENSE와 관련 Issue를 읽습니다. 코드 과제는 담당자가 겹치지 않도록 Issue에서 확인합니다.
- 반복형 데이터 과제는 별칭별 파일로 진행합니다. 다른 학생 파일을 임의로 수정하지 않습니다.
- 자신의 fork를 최신화한 뒤 **매 작업마다 새 branch**를 만듭니다. 예: `data/bluebird`, `docs/run-example`, `feature/name-search`.
- 한 PR에는 한 가지 목적을 담고, 이미 통과하는 테스트를 삭제해 실패를 숨기지 않습니다.

## CSV 규격

파일 위치는 `examples/submissions/<별칭>.csv`이고 인코딩은 UTF-8입니다. 파일명은 영어 소문자·숫자·하이픈을 권장합니다. 기존 파일과 겹치지 않는 이름을 사용합니다.

```csv
id,name,category,price
bluebird-meal,가상 나무식당,식사,5000
bluebird-drink,가상 하늘카페,음료,2500
bluebird-study,가상 조용한방,공간,0
```

- 첫 줄은 정확히 `id,name,category,price`입니다. 데이터는 1–3행으로 시작합니다.
- `id`는 전체 기여 파일에서 중복되지 않아야 합니다. `<별칭>-<항목>` 형식을 사용합니다.
- 이름과 종류는 빈 값이 아니어야 합니다. 금액은 0 이상의 정수입니다. 이름에 쉼표를 넣으면 CSV의 큰따옴표 규칙을 적용합니다.
- 실제 개인정보나 다른 사이트에서 수집한 자료 대신 직접 만든 가상 예시를 제출합니다.

## PR에 적을 내용

PR 대상은 **`Jinwoo-Han/opensource_test_repo`의 `main`**, 비교 대상은 **내 fork의 작업 branch**입니다. 12–14주차 개인 실습에서는 원본 대신 본인의 `oss-individual-labs` main을 대상으로 합니다.

목적, 관련 Issue, 바꾼 파일, 실행한 명령과 실제 결과를 적습니다. 예상 결과를 실제 실행한 것처럼 적지 않습니다. 반복형 첫 기여 Issue는 `Refs #번호`로 연결하고 닫지 않습니다. 자신이 맡은 일회성 코드 Issue를 모두 해결했다면 `Closes #번호`를 사용할 수 있습니다.

```bash
python -m campus_tool --data-dir examples/submissions
python -m unittest discover -s tests -v
git diff --check
git status
```

Files changed에 의도한 파일만 있는지 확인합니다. `.venv`, 비밀정보, 생성된 빌드 파일은 PR에 포함하지 않습니다.

## 교수자 검토·자동검사와 병합

1. 학생은 Files changed와 실제 실행 결과를 스스로 확인합니다. 짝 리뷰와 타인 리뷰 URL은 요구하지 않습니다.
2. 공통 기여는 `tests` CI와 교수자 검토, 개인 과제는 공지된 교수자 리뷰 또는 [Autograder](docs/autograding.md) 기준으로 확인합니다.
3. 받은 수정 요청이나 검사 실패는 **같은 branch**에서 수정하고 commit·push합니다. 기존 PR이 갱신됩니다.
4. 공통 원본은 교수자/관리자가 **Create a merge commit**으로 병합합니다. 개인 저장소는 공지된 검토·검사 기준을 충족하면 학생이 병합합니다. self-approval을 요구하지 않습니다.
5. 공통 기여자는 [11주차 안내](labs/week11.md)에 따라 원본 변경을 자기 fork와 로컬에 가져옵니다.

AI 도움을 사용했으면 사용 범위와 직접 검증한 내용을 적고 변경 이유를 본인이 설명합니다. 점수·비공개 피드백은 LMS에서 다룹니다.

CI가 `Awaiting approval`이면 관리자의 실행 확인을 기다립니다. 테스트 실패와 다릅니다. 실패하면 Actions에서 먼저 실패한 단계와 메시지를 읽습니다. [공식 안내](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks)
