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

- 첫 줄은 정확히 `id,name,category,price`입니다. 데이터는 1~3행으로 시작합니다.
- `id`는 전체 기여 파일에서 중복되지 않아야 합니다. `<별칭>-<항목>` 형식을 사용합니다.
- 이름과 종류는 빈 값이 아니어야 합니다. 금액은 0 이상의 정수입니다. 이름에 쉼표를 넣으면 CSV의 큰따옴표 규칙을 적용합니다.
- 실제 개인정보나 다른 사이트에서 수집한 자료 대신 직접 만든 가상 예시를 제출합니다.

## PR에 적을 내용

PR 대상은 **`Jinwoo-Han/opensource_test_repo`의 `main`**, 비교 대상은 **내 fork의 작업 branch**입니다. 팀 과제 단계에서는 원본 대신 팀 저장소를 대상으로 합니다.

목적, 관련 Issue, 바꾼 파일, 실행한 명령과 실제 결과를 적습니다. 예상 결과를 실제 실행한 것처럼 적지 않습니다. 반복형 첫 기여 Issue는 `Refs #번호`로 연결하고 닫지 않습니다. 자신이 맡은 일회성 코드 Issue를 모두 해결했다면 `Closes #번호`를 사용할 수 있습니다.

```bash
python -m campus_tool --data-dir examples/submissions
python -m unittest discover -s tests -v
git diff --check
git status
```

Files changed에 의도한 파일만 있는지 확인합니다. `.venv`, 비밀정보, 생성된 빌드 파일은 PR에 포함하지 않습니다.

## 리뷰와 병합

1. [리뷰 안내](docs/review-guide.md)에 따라 짝의 변경을 읽고 실행합니다.
2. 구체적인 질문 또는 개선 제안을 남깁니다. 문제가 없다면 확인한 입력과 결과를 적습니다. 억지로 오류를 만들 필요는 없습니다.
3. 작성자는 **같은 branch**에서 수정하고 commit·push합니다. 기존 PR이 갱신됩니다.
4. 학생의 의견과 CI 결과를 확인한 교수자/관리자가 **Create a merge commit**으로 병합합니다. 학생의 공개 리뷰가 필수 승인 권한을 자동으로 부여하는 것은 아닙니다.
5. 작성자는 [11주차 안내](labs/week11.md)에 따라 원본의 변경을 자기 fork와 로컬로 가져옵니다.

본인 PR을 스스로 Approve하는 것은 완료 조건이 아닙니다. 리뷰에서는 사람 대신 코드와 실행 결과를 대상으로 설명합니다. AI 도움을 사용했으면 도움받은 범위와 직접 검증한 내용을 PR에 적고 변경 이유를 본인이 설명합니다.

CI가 `Awaiting approval`이면 관리자의 실행 확인을 기다립니다. 이는 테스트 실패와 다릅니다. 실패하면 Actions에서 가장 먼저 실패한 단계와 메시지를 읽습니다. [GitHub 공식 안내](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks)
