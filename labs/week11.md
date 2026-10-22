# 11주차: Fork에서 원본으로 첫 기여

목표: 이 공통 저장소에 작은 PR을 보내고 다른 학생의 변경을 리뷰합니다. GitHub 계정 인증은 9주차에 마쳤다고 가정합니다.

## 1. Fork와 clone

GitHub에서 `Jinwoo-Han/opensource_test_repo`의 **Fork**를 눌러 본인 계정에 만듭니다. 이름은 `opensource_test_repo`, 기본 branch만 복사하는 경로를 사용합니다. 기존 fork가 있으면 다시 만들지 말고 갱신합니다.

아직 같은 이름의 폴더가 없는 위치에서 `YOUR_GITHUB_ID`를 실제 계정명으로 바꿉니다.

```bash
git clone git@github.com:YOUR_GITHUB_ID/opensource_test_repo.git
cd opensource_test_repo
git remote add upstream https://github.com/Jinwoo-Han/opensource_test_repo.git
git remote -v
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m campus_tool --data-dir examples/submissions
python -m unittest discover -s tests -v
```

`origin`은 내 fork, `upstream`은 교수자 원본입니다. 이미 upstream이 있다면 다시 추가하지 말고 URL을 확인합니다.

## 2. 별도 branch에서 기여

[기여 과제](../docs/tasks.md)의 T01과 해당 Issue를 읽습니다. 아래 `YOUR_ALIAS`를 다른 학생과 겹치지 않는 별칭으로 바꿉니다.

```bash
git switch -c data/YOUR_ALIAS
cp examples/submissions/instructor-example.csv examples/submissions/YOUR_ALIAS.csv
```

새 파일을 편집하여 **모든 ID를 본인 별칭으로 바꾸고**, 직접 만든 가상 항목을 1~3개 적습니다. 예제 파일은 수정하지 않습니다. [CSV 규격](../CONTRIBUTING.md)을 확인합니다.

```bash
python -m campus_tool --data-dir examples/submissions
python -m unittest discover -s tests -v
git diff --check
git add examples/submissions/YOUR_ALIAS.csv
git diff --cached
git commit -m "Add fictional campus entries"
git push -u origin data/YOUR_ALIAS
```

## 3. PR과 동료 리뷰

GitHub의 PR 생성 화면에서 **base repository `Jinwoo-Han/opensource_test_repo`, base `main`**, **head repository 내 fork, compare `data/YOUR_ALIAS`**를 확인합니다. 자동으로 채워진 PR 양식에 실제 결과를 적습니다. T01은 여러 학생이 참여하므로 `Refs #번호`로 연결하고 `Closes`는 쓰지 않습니다.

[리뷰 안내](../docs/review-guide.md)에 따라 짝의 PR을 실행·검토합니다. 받은 의견은 같은 branch에서 수정·commit·push해 반영합니다. CI 실행 승인이 대기 중이면 교수자에게 확인합니다.

교수자 병합 대기 자체는 미제출이 아닙니다. 제출은 PR URL, 동료 리뷰 URL, 실행 결과와 변경 이유 설명으로 확인합니다.

## 4. 병합 후 동기화

내 PR이 merge commit으로 병합됐고 로컬 작업 트리가 깨끗한 상태에서 실행합니다.

```bash
git switch main
git fetch upstream
git merge --ff-only upstream/main
git push origin main
git branch -d data/YOUR_ALIAS
git push origin --delete data/YOUR_ALIAS
git fetch --prune origin
```

원격 작업 branch가 이미 삭제됐다면 해당 삭제 명령은 생략합니다. `--ff-only`가 실패하면 개인 main에 별도 커밋이 있는지 확인합니다. 강제 덮어쓰기로 해결하지 않습니다. 다음 과제는 갱신한 main에서 새 branch로 시작합니다.
