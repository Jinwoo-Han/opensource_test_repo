"""Public formative checks for individual labs; not a final grade or a sandbox."""

import argparse
import csv
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def run(args, cwd, env, timeout=60):
    try:
        result = subprocess.run(args, cwd=cwd, env=env, capture_output=True,
                                text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"Timed out after {timeout} seconds"
    except OSError as error:
        return 127, "", str(error)


def output_names(output):
    return [line.split("\t")[0] for line in output.splitlines()[1:] if "\t" in line]


def evaluate(repo, week, python=sys.executable):
    repo = Path(repo).resolve()
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", PYTHONPATH=str(repo / "src"))
    checks = []

    def record(name, ok, detail=""):
        checks.append({"check": name, "passed": bool(ok), "detail": detail[:3000]})

    def command(name, args, cwd=repo, environment=env, timeout=60):
        code, out, err = run(args, cwd, environment, timeout)
        record(name, code == 0, f"exit={code}\n{out}\n{err}")
        return code, out, err

    _, commit, _ = run(["git", "rev-parse", "HEAD"], repo, env)
    for filename in ("README.md", "LICENSE", "pyproject.toml", "src/campus_tool/__main__.py"):
        record(f"file:{filename}", (repo / filename).is_file())
    code, out, err = command("existing-and-student-tests", [python, "-m", "unittest", "discover", "-s", "tests", "-v"])
    test_count = re.search(r"Ran (\d+) tests?", out + err)
    record("test-discovery-not-empty", bool(test_count and int(test_count[1]) > 0))
    code, out, err = run([python, "-m", "campus_tool"], repo, env)
    record("bundled-sample-data", code == 0 and output_names(out) == ["예시 학생식당", "예시 카페", "예시 공부방"], out + err)

    if week != "baseline":
        for number in range(12, int(week) + 1):
            report = repo / f"reports/week{number}.md"
            record(f"report:week{number}", report.is_file() and bool(report.read_text(encoding="utf-8").strip()))
        with tempfile.TemporaryDirectory(prefix="oss-input-") as tmp:
            data = Path(tmp)
            with (data / "places.csv").open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerows([
                    ["id", "name", "category", "price"],
                    ["a", "가상 숲카페", "음료", 2500],
                    ["b", "CampusCafe", "음료", 3500],
                    ["c", "가상 식당", "식사", 5500],
                    ["d", "QuietRoom", "공간", 0],
                    ["e", "CampusCafe2", "음료", 4500],
                ])
            cases = [
                ("no-keyword-preserves-order", [], ["가상 숲카페", "CampusCafe", "가상 식당", "QuietRoom", "CampusCafe2"]),
                ("keyword-korean", ["--keyword", "가상"], ["가상 숲카페", "가상 식당"]),
                ("keyword-case-insensitive", ["--keyword", "cAfE"], ["CampusCafe", "CampusCafe2"]),
                ("keyword-combined-filters", ["--keyword", "cafe", "--category", "음료", "--max-price", "3500"], ["CampusCafe"]),
                ("keyword-no-match", ["--keyword", "no-such-place"], []),
                ("keyword-empty-means-all", ["--keyword", ""], ["가상 숲카페", "CampusCafe", "가상 식당", "QuietRoom", "CampusCafe2"]),
            ]
            for name, args, expected in cases:
                code, out, err = run([python, "-m", "campus_tool", "--data-dir", str(data), *args], repo, env, 20)
                correct = code == 0 and not err and output_names(out) == expected
                if not expected:
                    correct = correct and "조건에 맞는 항목이 없습니다." in out
                record(name, correct, f"exit={code}\n{out}\n{err}")

            if int(week) >= 13:
                code, out, err = command("week13-tests", [python, "-m", "unittest", "discover", "-s", "tests", "-p", "test_week13.py", "-v"])
                count = re.search(r"Ran (\d+) tests?", out + err)
                record("week13-at-least-two-tests", code == 0 and bool(count and int(count[1]) >= 2), out + err)
                (data / "places.csv").write_text("id,name,category,price\nx,예시,음료,-1\n", encoding="utf-8")
                for name, args in [
                    ("reject-invalid-price-data", ["--data-dir", str(data)]),
                    ("reject-noninteger-option", ["--max-price", "abc"]),
                    ("reject-missing-data-directory", ["--data-dir", str(data / "missing")]),
                ]:
                    code, out, err = run([python, "-m", "campus_tool", *args], repo, env)
                    record(name, code == 2 and bool(err.strip()) and "Traceback" not in err, out + err)
                (data / "places.csv").write_text("id,name,category,price\n", encoding="utf-8")
                code, out, err = run([python, "-m", "campus_tool", "--data-dir", str(data)], repo, env)
                record("empty-catalog-is-success", code == 0 and "조건에 맞는 항목이 없습니다." in out, out + err)

    if week == "14":
        with tempfile.TemporaryDirectory(prefix="oss-wheel-") as tmp:
            root = Path(tmp)
            dist = root / "dist"
            code, _, _ = command("build-wheel-and-sdist", [python, "-m", "build", "--outdir", str(dist)], timeout=180)
            wheels = list(dist.glob("*.whl"))
            record("one-wheel-and-sdist", code == 0 and len(wheels) == 1 and len(list(dist.glob("*.tar.gz"))) == 1)
            if code == 0 and len(wheels) == 1:
                code, _, _ = command("fresh-install-environment", [python, "-m", "venv", str(root / "venv")], timeout=90)
                installed = root / "venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
                clean_env = dict(env)
                clean_env.pop("PYTHONPATH", None)
                if code == 0:
                    code, _, _ = command("install-wheel", [str(installed), "-m", "pip", "install", "--no-deps", str(wheels[0])], root, clean_env, 90)
                    if code == 0:
                        code, out, err = run([str(installed), "-I", "-X", "utf8", "-m", "campus_tool", "--keyword", "학생", "--max-price", "6000"], root, clean_env)
                        record("installed-wheel-behavior-and-data", code == 0 and output_names(out) == ["예시 학생식당"], out + err)
                        expression = "import importlib.metadata as m, campus_tool as c; assert m.version('oss-campus-tool') == c.__version__; print(c.__file__)"
                        command("installed-version-agrees", [str(installed), "-I", "-X", "utf8", "-c", expression], root, clean_env)
    return {"week": week, "submission_commit": commit.strip(), "status": "pass" if all(c["passed"] for c in checks) else "fail", "checks": checks,
            "limits": "Public formative checks, not final grades. Report quality, regression-test meaning, release assets and authorship need instructor judgment."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--week", choices=["baseline", "12", "13", "14"], required=True)
    parser.add_argument("--output", type=Path, default=Path("output/autograde.json"))
    args = parser.parse_args()
    result = evaluate(args.repo, args.week)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    for check in result["checks"]:
        print(f"{'PASS' if check['passed'] else 'FAIL'} {check['check']}")
    print(f"Result: {result['status']} / SHA: {result['submission_commit']} / {args.output}")
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
