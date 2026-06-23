# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/). This project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-06-23

### Added

- **Vendored the `remember` + `recall` memory skills from eidetic-cli**
  (cite-don't-import) — the write/read halves of eidetic's shared
  `~/.eidetic/memory` surface, so this agent (Claude and its colleague backend)
  can persist facts across sessions and recall them later, sharing one store.
  `remember` drives `eidetic remember` (idempotent upsert of one JSON record or
  an NDJSON batch on stdin, dedup by id + content hash); `recall` drives
  `eidetic recall` with four search modes — exact / approximate / keyword /
  hybrid — each hit carrying text, full provenance metadata, a relevance score,
  and a freshness signal. The `.sh` wrappers are byte-verbatim from eidetic-cli
  (their first-party origin); each `SKILL.md` is localized only in the
  illustrative `--scope <nick>` examples (Provenance keeps "First-party to
  eidetic-cli"). Both default to this agent's PRIVATE scope, reading the suffix
  from `culture.yaml`. Runtime dep: the `eidetic` CLI on PATH (else a local
  eidetic-cli checkout with `uv`). Propagated by rollout-cli's `eidetic-memory`
  recipe.

## [0.1.2] - 2026-05-26

### Added

- **CI-based SonarCloud analysis, activated.** `tests.yml` already had a `SonarCloud Scan` step (gated on `SONAR_TOKEN`) and `sonar-project.properties` already declared the `agentculture_agenda` project, but the scan was dormant: the `SONAR_TOKEN` secret was the empty placeholder created by `guild create`. The SonarCloud project is now registered and the real `SONAR_TOKEN` secret is set, so CI uploads `coverage.xml` and a SonarCloud check runs on each PR — no workflow or `sonar-project.properties` edit required.
- **One-time prerequisite** (mirrors steward 0.9.3): the SonarCloud project must use **CI-based analysis** with Auto-Analysis disabled (Project → Administration → Analysis Method). Otherwise the auto-analysis run races the CI scan and the `coverage.xml` upload is ignored.

## [0.1.1] - 2026-05-26

### Changed

- **Distribution renamed `agenda` → `agenda-cli`** to match the PyPI Trusted
  Publishing project (`pyproject.toml` `name`, `agenda/__init__.py` version
  lookup, and the TestPyPI install hint in `publish.yml`). The import package,
  `agenda` console script, and Sonar project key stay `agenda`.
- **Agent description** set to "Work-state tracking for GitHub issues,
  priorities, blockers, and next actions." (`pyproject.toml`, `README.md`,
  `CLAUDE.md`).

### Fixed

- **markdownlint MD036** in the `CLAUDE.md` seed — the agent name was emitted as
  a standalone emphasized line (`**agenda**`); now inlined in a sentence.
- **README intro** — removed a dangling fragment left by the scaffold's
  single-line description replacement.

## [0.1.0] - 2026-05-26

### Added

- **Onboarded into the AgentCulture mesh** ([issue #1](https://github.com/agentculture/agenda/issues/1)).
- **Agent-first CLI** cited from teken's (`afi-cli`) `python-cli` reference
  (`teken cli cite`) — verbs `whoami`, `learn`, `explain`, `overview`, `doctor`,
  and the `cli` noun group. Runtime is self-contained (`dependencies = []`);
  `teken>=0.8` is a dev dependency only. Passes the seven-bundle agent-first
  rubric (`teken cli doctor . --strict`). `doctor` checks the agent-identity
  invariants (prompt-file-present, backend-consistency, skills-present).
- **Mesh identity**: `culture.yaml` (`suffix: agenda`,
  `backend: claude`) and the matching `CLAUDE.md` prompt file.
- **Canonical guildmaster skill kit** (11 skills) vendored under
  `.claude/skills/` (cite-don't-import): `agent-config`, `assign-to-workforce`,
  `cicd`, `communicate`, `doc-test-alignment`, `pypi-maintainer`, `run-tests`,
  `sonarclaude`, `spec-to-plan`, `think`, `version-bump`. Every `SKILL.md`
  carries `type: command` (load-bearing for the culture/claude backend);
  `cicd` / `communicate` consumer-identifying prose adapted, all script bodies
  verbatim. Provenance in `docs/skill-sources.md`. Three skills (`think`,
  `spec-to-plan`, `assign-to-workforce`) originate in `devague`, re-broadcast
  via guildmaster.
- **Build + deploy baseline**: `pyproject.toml` (hatchling), `tests/` (pytest,
  xdist, coverage), `.github/workflows/{tests,publish}.yml` (CI rubric/lint gate,
  PyPI Trusted Publishing), `.flake8`, `.markdownlint-cli2.yaml`,
  `sonar-project.properties`, and `.claude/skills.local.yaml.example`.

### Changed

### Fixed
