# 14주차: 개인 패키징과 설치 검증

목표: 자신의 결과물을 소스 폴더 밖의 새 환경에서 설치·실행합니다. 교수자는 제출한 릴리스와 SHA를 검토하거나 Autograder로 기능·패키지를 검사합니다. 이론·시연 15분, 개인 실습 175분, 정리 10분입니다.

## 1. 문서·버전 정리 — 30분

개인 저장소에서 `release/week14` branch를 만듭니다. README의 설치·사용 예시, LICENSE, 남은 문제를 정리합니다. 배포 이름 `oss-campus-tool`과 모듈 `campus_tool`은 유지하고, `pyproject.toml`과 `src/campus_tool/__init__.py`의 버전을 함께 갱신합니다. 각 학생이 자기 저장소에서 0.2.0 같은 버전을 사용할 수 있습니다. PyPI 업로드는 하지 않습니다.

## 2. 빌드·새 환경 설치 — 50분

아래 명령은 저장소 최상위, 개발 가상환경을 활성화한 Ubuntu Bash 기준입니다.

```bash
python -m unittest discover -s tests -v
python -m pip install build
python -m build
PACKAGE_ROOT="$PWD"
CHECK_DIR="$(mktemp -d)"
python -m venv "$CHECK_DIR/venv"
"$CHECK_DIR/venv/bin/python" -m pip install --no-deps "$PACKAGE_ROOT"/dist/*.whl
cd "$CHECK_DIR"
"$CHECK_DIR/venv/bin/python" -I -m campus_tool --keyword 학생 --max-price 6000
cd "$PACKAGE_ROOT"
```

이전 wheel이 남아 여러 개면 이번 버전의 파일 하나를 명시합니다. 새 환경에서 예시 학생식당이 출력되어야 합니다. 소스 폴더나 editable 설치의 도움 없이 동봉 데이터와 추가 기능이 작동하는지 확인합니다. 빌드 파일·가상환경을 소스 commit에 넣지 않습니다.

## 3. 검사·PR — 30분

[기록 양식](../docs/submission-template.md)에 따라 `reports/week14.md`를 작성합니다. 앞선 두 주 기록을 보관하고 실행합니다.

```bash
python tools/autograde.py --week 14 --output output/week14-checks.json
git diff --check
```

Autograder는 앞선 주차의 검사, wheel·sdist 빌드, 새 환경 wheel 설치, 동봉 데이터·keyword 동작, 버전 일치를 확인합니다. 본인 저장소 main 대상 PR을 만들고 교수자 피드백 또는 자동검사 결과를 반영합니다.

## 4. 개인 릴리스 — 25분

검토·검사를 마친 코드의 SHA를 정합니다. 병합 후 SHA를 제출한다면 그 SHA로 다시 검사하고 같은 코드를 빌드합니다. 해당 commit에 개인 버전 태그를 붙이고 GitHub Release에 wheel·소스 배포 파일을 첨부합니다. 릴리스 노트에는 변경 내용, 설치 방법, 알려진 제한을 적습니다.

## 5. 전달 확인·개인 설명 — 30분

본인의 Release에 실제로 첨부된 wheel을 내려받아 또 다른 새 환경에 설치합니다. 다운로드한 파일 이름·해시·설치 명령·실행 결과를 **LMS**에 기록합니다. 공개 Autograder의 재빌드 성공만으로 릴리스 첨부 파일까지 검증된 것은 아닙니다. 교수자는 필요시 동일 파일을 재검사합니다.

## 6. 정리 — 10분

남은 문제를 개인 Issue에 적고 branch·PR·테스트·릴리스의 관계를 정리합니다. 마지막 별도 10분에는 릴리스 URL, 제출 SHA, 검사 결과, 다운로드 배포물 검증 기록, 개인 설명을 LMS에 제출합니다. 팀 발표·짝 실행 확인·타인 리뷰는 요구하지 않습니다.
