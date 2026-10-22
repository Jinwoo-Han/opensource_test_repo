# 9주차: 오픈소스와 GitHub 연결

목표: 공개와 라이선스의 차이를 설명하고, 개인 저장소를 연결해 첫 push와 branch 생성을 완료합니다. Ubuntu Bash를 사용합니다. 아직 이 공통 저장소를 fork하지 않습니다.

## 1. 개념 활동

이 저장소의 README와 LICENSE를 읽고 프로젝트 목적, 허용 범위, 유지해야 할 고지를 찾습니다. 사용자·기여자·유지관리자가 각각 하는 일을 적습니다. 공개된 코드에 라이선스가 없으면 자유롭게 재사용해도 된다고 단정하지 않습니다.

## 2. 인증 준비

```bash
git --version
python3 --version
ls -al ~/.ssh
```

기존 GitHub용 SSH 키가 있으면 재사용합니다. 없다면 `ssh-keygen -t ed25519 -C "GitHub 연결용"`으로 생성합니다. 기존 파일을 덮어쓰지 않습니다. 지정한 개인키를 `ssh-add`에 등록하고 **`.pub` 공개키**를 GitHub Settings → SSH and GPG keys에 등록합니다. 개인키와 암호는 제출하지 않습니다.

예를 들어 기본 경로 `~/.ssh/id_ed25519`로 새 키를 만들었다면:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
ssh -T git@github.com
```

첫 연결의 호스트 지문은 [공식 지문](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)과 대조합니다. 성공 메시지에 본인 계정명이 있는지 확인합니다. GitHub는 셸 접속을 제공하지 않아 성공 메시지와 종료 코드 1이 함께 나올 수 있습니다. [인증 안내](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

## 3. 로컬과 공개 원격 연결

새 폴더에서만 진행합니다. `oss-week09`가 이미 있으면 다른 이름을 정하고 원격 저장소명도 맞춥니다.

```bash
mkdir -p ~/Workspaces
cd ~/Workspaces
mkdir oss-week09
cd oss-week09
git init -b main
git config user.name "공개 표시 이름"
git config user.email "GitHub에서 확인한 커밋용 이메일"
printf '# OSS Week 09\n' > README.md
printf 'print("Hello, open source")\n' > greet.py
python3 greet.py
git add README.md greet.py
git commit -m "Add first Python example"
```

GitHub에서 본인 계정에 `oss-week09`를 **Public**으로 생성합니다. 이번 연결 경로에서는 README·gitignore·LICENSE 초기화를 선택하지 않습니다. `YOUR_GITHUB_ID`를 바꿔 다음을 실행합니다.

```bash
git remote add origin git@github.com:YOUR_GITHUB_ID/oss-week09.git
git remote -v
git push -u origin main
git log -1 --oneline
```

로컬과 웹의 커밋 해시를 비교합니다. GitHub 저장소 생성과 로컬 `git init`이 같은 작업인지 설명합니다. 이후 자신의 코드를 재사용 가능하게 배포하려면 적절한 LICENSE도 추가해야 합니다.

## 4. branch 도입

```bash
git switch -c docs/run-guide
printf '\nRun: python3 greet.py\n' >> README.md
git add README.md
git commit -m "Document how to run the example"
git log --oneline --graph --decorate --all
```

main과 현재 branch의 위치를 설명합니다. 이 branch를 10주차에 PR로 보냅니다.

제출: LMS에 저장소 URL, 첫 push의 커밋 해시, 커밋 그래프와 설명을 남깁니다. 학번·성적은 GitHub README에 적지 않습니다.

오류가 나면 `git status`, `git remote -v`, 인증 계정부터 확인합니다. 이미 `origin`이 있으면 다시 추가하지 않습니다. push가 거절되면 force push 대신 원격 이력을 확인합니다.
