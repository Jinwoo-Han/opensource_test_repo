# 14주차: 패키징, 릴리스와 전달

목표: 다른 팀이 소스 작업 폴더 없이 배포물을 설치·실행할 수 있게 합니다. 자기 팀의 공개 저장소에서 진행합니다.

1. README의 설치·사용 예시, LICENSE, 남은 문제를 정리합니다.
2. 팀 배포 이름과 버전을 `pyproject.toml`에서 정하고 `src/campus_tool/__init__.py`의 버전도 맞춥니다. 시작 버전은 0.1.0입니다.
3. 활성화된 가상환경에서 테스트하고 배포물을 만듭니다.

```bash
python -m unittest discover -s tests -v
python -m pip install build
python -m build
```

`dist/`의 wheel과 소스 배포 파일을 확인합니다. 빌드 결과를 소스 커밋에 넣지 않습니다. 새 가상환경에서 설치를 시험합니다. 아래는 **저장소 최상위 폴더에서 시작**하는 Bash 명령입니다.

```bash
PACKAGE_ROOT="$PWD"
CHECK_DIR="$(mktemp -d)"
python -m venv "$CHECK_DIR/venv"
"$CHECK_DIR/venv/bin/python" -m pip install --no-deps "$PACKAGE_ROOT"/dist/*.whl
cd "$CHECK_DIR"
"$CHECK_DIR/venv/bin/python" -m campus_tool --max-price 6000
cd "$PACKAGE_ROOT"
```

배포 후보 wheel이 여러 개면 설치할 파일 하나를 명시합니다. 소스 폴더 밖에서도 동봉 예시 데이터가 읽히는지 확인합니다.

테스트한 commit에 팀 버전 태그를 만들고 GitHub Release에 wheel과 소스 배포 파일을 첨부합니다. 릴리스 노트에는 기능, 설치 방법, 알려진 제한을 씁니다. PyPI 업로드는 필수가 아닙니다.

다른 팀이 릴리스 파일을 내려받아 새 환경에 설치하고 결과를 전달합니다. 발견한 문제는 수정하거나 후속 Issue로 남깁니다. 발표는 팀 간 교환 시연 중심으로 하고, 각 학생은 자신이 작성·검토한 변경 한 건을 설명합니다.

제출: 릴리스 URL, 테스트한 commit SHA, 다른 팀의 설치·실행 기록, 개인 기여 설명. README와 실제 배포물의 명령이 일치해야 합니다.
