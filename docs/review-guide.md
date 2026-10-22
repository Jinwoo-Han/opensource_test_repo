# 동료 PR 리뷰

목표는 상대방의 변경을 이해하고 재현 가능한 피드백을 주는 것입니다. `좋아요` 한 줄보다 **무엇을 실행해서 무엇을 확인했는지**를 적습니다.

## 읽기

1. PR의 목적과 연결된 Issue를 읽습니다.
2. Files changed에서 목적과 무관한 변경이 없는지 확인합니다.
3. CSV 기여라면 파일명·ID 중복·열·금액을 확인합니다. 코드 기여라면 정상 입력과 경계 입력의 결과를 예상합니다.

## 실행

내 작업 폴더를 덮어쓰지 않고, 상대 fork의 PR branch를 **새 폴더**에 clone합니다. 아래 `PEER_ID`, `BRANCH_NAME`, `review-peer`는 PR 화면에서 확인한 값과 아직 없는 폴더명으로 바꿉니다.

```bash
git clone --branch BRANCH_NAME https://github.com/PEER_ID/opensource_test_repo.git review-peer
cd review-peer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m campus_tool --data-dir examples/submissions
python -m unittest discover -s tests -v
```

리뷰가 끝나면 `deactivate` 후 내 원래 저장소로 돌아갑니다. 상대가 수정한 뒤 재확인할 때는 리뷰 폴더에서 `git pull --ff-only`로 갱신합니다. 내 로컬 작업을 상대 branch에 push하지 않습니다.

## 남길 의견

예시 형식은 다음과 같습니다. 괄호 안을 자신의 관찰로 바꿉니다.

```text
확인한 변경: [파일과 동작]
실행한 명령/입력: [명령과 입력값]
관찰한 결과: [출력 또는 실패 메시지]
질문/제안: [근거가 있는 의견. 문제가 없으면 확인한 경계 조건]
```

GitHub의 Files changed에서 해당 줄에 의견을 남기고 Review changes → Comment로 제출할 수 있습니다. 공통 저장소의 쓰기 권한이 없는 학생의 리뷰는 학습용 피드백이며, branch 보호 규칙의 필수 승인은 교수자/관리자가 맡습니다. 팀 저장소에서는 권한을 가진 동료가 정식 승인 역할을 맡을 수 있습니다.

완료 증거는 리뷰 URL과 실행한 입력·결과입니다. 작성자는 받은 의견에 답하고 반영 여부와 이유를 설명합니다.
