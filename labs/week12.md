# 12주차: 개인 기능 추가와 변경 관리

목표: 혼자 기능 하나를 구현하고 Issue·branch·PR·테스트로 변경 근거를 남깁니다. 팀 구성과 짝 리뷰는 없습니다. 이론·시연 20분, 개인 실습 170분, 정리 10분입니다.

## 1. 개인 저장소 준비 — 20분

교수자가 공지한 시작 버전을 확인합니다. 이 저장소의 **Use this template → Create a new repository**에서 Owner를 본인 계정, 이름을 `oss-individual-labs`, 공개 범위를 **Public**으로 선택합니다. 기본 branch만 포함합니다. 같은 이름이 있으면 새 이름을 정합니다. 템플릿은 새 이력을 가진 독립 저장소이므로, 이후 PR은 교수자 원본이 아닌 **내 저장소 main**으로 보냅니다.

새 폴더에 clone하고 README의 가상환경·설치·실행 절차를 따릅니다. README의 저장소 주소와 workflow badge도 자신의 저장소에 맞춥니다. `campus_tool` 모듈명과 배포 이름 `oss-campus-tool`은 자동검사에 맞춰 유지합니다.

```bash
git clone git@github.com:YOUR_GITHUB_ID/oss-individual-labs.git
cd oss-individual-labs
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m campus_tool
python -m unittest discover -s tests -v
```

## 2. 개인 Issue와 완료 기준 — 20분

내 저장소에 이름 검색 기능 Issue를 만듭니다. 기본 과제는 모든 학생에게 같습니다.

- `--keyword 문자열`로 **이름의 부분 문자열**을 검색합니다. 한글을 지원하고 영문 대소문자를 구분하지 않습니다.
- `--category`, `--max-price`와 함께 주면 모든 조건을 만족하는 항목만 출력합니다. 가격 상한은 포함합니다.
- keyword를 생략하거나 빈 문자열로 주면 이름으로 제한하지 않습니다. 기존 출력 형식과 입력 순서를 유지합니다.
- 결과가 없으면 기존 안내 문구와 종료 코드 0을 유지합니다. 기존 예시 데이터 3개는 변경하지 않습니다.
- README 사용 예시, 기능 테스트, `reports/week12.md`의 실제 실행 기록을 추가합니다.

## 3. 구현·테스트 — 80분

```bash
git switch -c feature/keyword-search
```

`src/campus_tool/catalog.py`의 검색 함수와 `src/campus_tool/__main__.py`의 CLI 옵션을 수정합니다. 함수의 기존 호출도 유지합니다. 정상 검색, 대소문자, 조건 조합, 결과 없음, 빈 문자열을 직접 확인합니다. [제출 기록 양식](../docs/submission-template.md)을 `reports/week12.md`에 복사해 채웁니다.

```bash
python -m unittest discover -s tests -v
python tools/autograde.py --week 12 --output output/week12-checks.json
git diff --check
```

Autograder는 기준을 공개한 검사입니다. 시작 코드에는 keyword 기능이 없으므로 구현 전에는 실패하는 것이 정상입니다. 실패한 항목을 읽고 수정합니다. 검사 코드나 기존 테스트를 지워 성공시키지 않습니다.

## 4. PR·피드백 반영 — 35분

변경할 파일만 `git add`하고 commit·push한 뒤 **내 저장소 main ← feature/keyword-search** PR을 만듭니다. 실제 명령·출력과 연결할 내 Issue를 적습니다. 교수자 리뷰 방식이면 교수자 의견을, 자동검사 중심이면 검사 실패 결과를 반영합니다. 타 학생에게 리뷰를 요청하지 않습니다.

## 5. 완료 확인 — 15분

README·프로그램 동작·테스트 결과가 일치하는지 스스로 확인합니다. 교수자가 공지한 방식에 따라 병합하며, 자기 PR의 self-approval은 요구하지 않습니다. 병합 전후 SHA를 구분하고, 실제 제출한 SHA로 검사합니다.

마지막 10분 제출: 개인 Issue·PR URL, 제출 SHA, 검사 결과, `reports/week12.md`, 변경 이유. 기본 과제를 마쳤다면 정렬이나 CSV 저장을 별도 Issue로 선택할 수 있습니다.
