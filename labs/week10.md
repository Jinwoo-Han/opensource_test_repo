# 10주차: PR, 리뷰, merge와 충돌

목표: 9주차 개인 저장소에서 변경을 제안·검토·병합하고 충돌을 해결합니다. **이 공통 저장소의 main에는 아래 충돌 예제를 실행하지 않습니다.**

## 1. 문서 PR과 교수자 피드백

9주차 `oss-week09`에서 작업 트리가 깨끗한지 확인합니다.

```bash
git status
git switch docs/run-guide
git push -u origin docs/run-guide
```

웹에서 본인 저장소의 `main`을 base, `docs/run-guide`를 compare로 PR을 만듭니다. 목적·변경·실제 실행 결과를 적습니다. 교수자가 Files changed와 실행 안내를 확인해 피드백합니다. 학생은 타인 PR을 리뷰하지 않습니다. 작성자는 필요한 수정을 같은 branch에 commit·push합니다.

본인 저장소에서 **Create a merge commit**으로 병합하고 원격 작업 branch를 삭제합니다. 자기 PR을 스스로 Approve할 필요는 없습니다.

```bash
git switch main
git pull --ff-only origin main
git log --oneline --graph --decorate --all
git branch -d docs/run-guide
git fetch --prune origin
```

## 2. 같은 줄 충돌 만들기

개인 연습 저장소에서만 다음 두 변경을 만듭니다. 첫 merge가 fast-forward인 경우와 두 branch가 갈라진 경우의 그래프 차이를 관찰합니다.

```bash
git switch -c feature/greeting
printf 'print("Hello, contributors")\n' > greet.py
git add greet.py
git commit -m "Greet contributors"
git switch main
printf 'print("Welcome to week 10")\n' > greet.py
git add greet.py
git commit -m "Set week 10 welcome message"
git push origin main
git switch feature/greeting
git fetch origin
git merge origin/main
```

이 단계에서는 충돌이 **예상된 결과**입니다. `git status`와 `greet.py`의 표시자를 읽습니다. `<<<<<<<`, `=======`, `>>>>>>>`를 포함한 상태를 그대로 commit하지 않습니다.

## 3. 의도한 코드로 해결

편집기로 최종 인사말을 정해 표시자와 불필요한 줄을 지웁니다. 예를 들어 `print("Welcome, contributors, to week 10")`로 합칠 수 있습니다.

```bash
python3 greet.py
git diff --check
git add greet.py
git commit -m "Resolve greeting conflict with main"
git push -u origin feature/greeting
```

`feature/greeting → main` PR을 만들고 해결 이유를 적습니다. 교수자가 공지한 검토 기준을 충족한 뒤 merge commit으로 병합합니다.

```bash
git switch main
git pull --ff-only origin main
python3 greet.py
git branch -d feature/greeting
git fetch --prune origin
```

처음에 작업 트리가 깨끗했고 충돌 처리를 취소하고 싶다면 `git merge --abort`를 사용할 수 있습니다. `pull --ff-only`가 실패하면 로컬/원격 양쪽에 새 커밋이 있는지 그래프를 확인하고 교수자와 병합 방향을 정합니다.

제출: PR URL, 제출 SHA와 교수자 피드백 반영 내용, 충돌한 두 변경과 선택한 최종 코드, 최종 그래프. 명령을 외우는 대신 각 변경이 어디에 있는지 설명합니다.

이 주차는 인사말 파일과 Git 기록을 교수자가 확인합니다. 12~14주차 `campus_tool` 전용 Autograder를 이 저장소에 적용하지 않습니다. 교수자 리뷰 대기는 제출 여부와 구분합니다.
