"""Validate published assets, numerical tables and content exclusions."""

from pathlib import Path
import json
import re
import subprocess
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "paper_assets"
DATA = ASSETS / "summary_csv"
DIRECTIONS = [
    ("dense", "dense"),
    ("sues", "sues"),
    ("dense", "sues"),
    ("sues", "dense"),
]
BASE = "Base (EVA-02 + Label Smoothing)"
HOSTS = [
    "DAC",
    "MEAN",
    BASE,
    "Base + QGIN",
    "Sample4Geo",
    "S4G-QDual",
    "ConGeo",
    "ConGeo-QView",
    "SinGeo",
    "SinGeo-QView",
]
ADAPTERS = ["ConGeo", "SLAug", "PASTA", "AFA", "RaffeSDG", "ConGeo-QView"]
ABLATIONS = [
    "Fixed Zero-Hinge",
    "MeanHinge",
    "Q50",
    "QuantNoStd",
    "MeanNoStd",
    "Base + QGIN",
    "AugMix-Dual",
    "ColorJitter-Dual",
]


def row_in_table(cells, document):
    row = "| " + " | ".join(cells) + " |"
    assert row in document, f"Missing or incorrect table row: {row}"


def value(frame, arm, direction, condition, metric="r1"):
    subset = frame[
        (frame.arm == arm)
        & (frame.train_domain == direction[0])
        & (frame.target == direction[1])
        & (frame.condition == condition)
    ]
    if condition == "UnseenMean":
        subset = subset[subset.level == "all"]
    assert set(subset.seed) == {42, 43, 44} and len(subset) == 3, (
        arm,
        direction,
        condition,
    )
    return 100 * subset[metric].mean(), 100 * subset[metric].std(ddof=1)


def shown(frame, arm, direction, condition, metric="r1"):
    mean, std = value(frame, arm, direction, condition, metric)
    return f"{mean:.2f} ± {std:.2f}"


def delta(frame, new, old, direction, condition="CorrMean6"):
    level = "all" if condition == "UnseenMean" else "original"
    subset = frame[
        (frame.treatment == new)
        & (frame.reference == old)
        & (frame.train_domain == direction[0])
        & (frame.target == direction[1])
        & (frame.condition == condition)
        & (frame.metric == "r1")
        & (frame.level == level)
    ]
    sign = 1
    if subset.empty:
        subset = frame[
            (frame.treatment == old)
            & (frame.reference == new)
            & (frame.train_domain == direction[0])
            & (frame.target == direction[1])
            & (frame.condition == condition)
            & (frame.metric == "r1")
            & (frame.level == level)
        ]
        sign = -1
    assert len(subset) == 1, (new, old, direction, condition)
    rec = subset.iloc[0]
    point = sign * 100 * rec.mean_difference
    low = 100 * (rec.seed_location_ci_low if sign == 1 else -rec.seed_location_ci_high)
    high = 100 * (rec.seed_location_ci_high if sign == 1 else -rec.seed_location_ci_low)
    return f"{point:+.2f} [{low:+.2f}, {high:+.2f}]"


def main():
    tracked = (
        subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
        )
        .decode("utf8")
        .split("\0")
    )
    files = [ROOT / p for p in set(tracked) if p and (ROOT / p).is_file()]
    forbidden_path = re.compile(
        r"layer.?mix|qview-or-augmix|e1_exploratory|per_query_", re.I
    )
    blocked_suffixes = (
        ".pth",
        ".pt",
        ".ckpt",
        ".safetensors",
        ".bin",
        ".tar",
        ".tar.gz",
        ".zip",
        ".npy",
        ".npz",
        ".h5",
        ".log",
    )
    for file in files:
        rel = file.relative_to(ROOT).as_posix()
        assert file.stat().st_size < 10 * 1024 * 1024, f"Large file: {rel}"
        assert not forbidden_path.search(rel), f"Excluded path: {rel}"
        assert not rel.lower().endswith(blocked_suffixes), f"Excluded type: {rel}"
    banned = re.compile(
        r"(?i:layer.?mix|qview-or-augmix|e1_exploratory|awaiting_user_confirmation|go / observe)|-C",
    )
    documents = [
        ROOT / "README.md",
        *ASSETS.rglob("*.md"),
        *DATA.glob("*.csv"),
        *DATA.glob("*.json"),
    ]
    for file in documents:
        text = file.read_text(encoding="utf8")
        assert not banned.search(text), f"Excluded text in {file}"
    bench = pd.read_csv(DATA / "benchmark_metrics.csv")
    intervals = pd.read_csv(DATA / "paired_bootstrap_ci.csv")
    unseen = pd.read_csv(DATA / "unseen_brightness_metrics.csv")
    assert len(bench) == 2016 and len(intervals) == 9846
    assert set(bench.seed) == {42, 43, 44}
    main_doc = (ASSETS / "03_Main_Benchmark_Tables.md").read_text(encoding="utf8")
    ablation_doc = (ASSETS / "04_Ablation_and_Unseen_Eval.md").read_text(
        encoding="utf8"
    )
    for method in HOSTS:
        cells = [method]
        for direction in DIRECTIONS:
            cells.append(
                " / ".join(
                    shown(bench, method, direction, c)
                    for c in ["Clean", "Snow", "CorrMean6"]
                )
            )
        cells.append(
            f"{sum(value(bench, method, d, 'CorrMean6')[0] for d in DIRECTIONS) / 4:.2f}"
        )
        row_in_table(cells, main_doc)
    for method in ADAPTERS:
        for condition, metric in [
            ("CorrMean6", "r1"),
            ("Snow", "r1"),
            ("CorrMean6", "ap"),
        ]:
            cells = [method] + [
                shown(bench, method, d, condition, metric) for d in DIRECTIONS
            ]
            cells.append(
                f"{sum(value(bench, method, d, condition, metric)[0] for d in DIRECTIONS) / 4:.2f}"
            )
            row_in_table(cells, main_doc)
    for method in ABLATIONS:
        cells = [method] + [shown(bench, method, d, "CorrMean6") for d in DIRECTIONS]
        cells.append(
            f"{sum(value(bench, method, d, 'CorrMean6')[0] for d in DIRECTIONS) / 4:.2f}"
        )
        row_in_table(cells, ablation_doc)
    for old, new in [
        (BASE, "Base + QGIN"),
        ("Sample4Geo", "S4G-QDual"),
        ("ConGeo", "ConGeo-QView"),
        ("SinGeo", "SinGeo-QView"),
    ]:
        row_in_table(
            [f"{old} → {new}"] + [delta(intervals, new, old, d) for d in DIRECTIONS],
            main_doc,
        )
    for old in ADAPTERS[1:5]:
        row_in_table(
            [old] + [delta(intervals, "ConGeo-QView", old, d) for d in DIRECTIONS],
            main_doc,
        )
    for direction, label in zip(
        DIRECTIONS, ["Dense→Dense", "SUES→SUES", "Dense→SUES", "SUES→Dense"]
    ):
        row_in_table(
            [
                label,
                shown(unseen, "ConGeo", direction, "UnseenMean"),
                shown(unseen, "ConGeo-QView", direction, "UnseenMean"),
                delta(intervals, "ConGeo-QView", "ConGeo", direction, "UnseenMean"),
            ],
            ablation_doc,
        )
    for cond, metric, expected in [
        ("Snow", "r1", 16),
        ("CorrMean6", "r1", 13),
        ("CorrMean6", "ap", 12),
    ]:
        selection = intervals[
            intervals.treatment.isin(ADAPTERS[1:5])
            & intervals.reference.eq("ConGeo-QView")
            & intervals.condition.eq(cond)
            & intervals.metric.eq(metric)
            & intervals.level.eq("original")
        ]
        assert (
            len(selection) == 16
            and (selection.seed_location_ci_high < 0).sum() == expected
        )
    checksums = pd.read_csv(DATA / "checkpoint_sha256.csv")
    assert (
        len(checksums) == 126
        and checksums.checkpoint_sha256.str.fullmatch(r"[0-9a-f]{64}").all()
    )
    for doc in [ROOT / "README.md", *ASSETS.glob("*.md"), ROOT / "THIRD_PARTY.md"]:
        for link in re.findall(
            r"\]\(([^)#]+)(?:#[^)]*)?\)", doc.read_text(encoding="utf8")
        ):
            if "://" not in link and not link.startswith("mailto:"):
                assert (
                    doc.parent / link
                ).exists(), f"Broken local link {link} in {doc}"
    protocol = json.loads(
        (ROOT / "configs_and_contracts/protocol.json").read_text(encoding="utf8")
    )
    assert protocol["seeds"] == [42, 43, 44]
    print(
        f"Release checks passed: {len(files)} files; host, adapter, ablation and interval tables match the aggregate CSVs; 126 checkpoint hashes; no excluded artifacts."
    )


if __name__ == "__main__":
    main()
