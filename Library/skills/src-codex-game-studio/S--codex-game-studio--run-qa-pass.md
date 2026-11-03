---
id: "codex-game-studio/run-qa-pass"
type: skill
category: "src-codex-game-studio"
source: "codex-game-studio"
license: "MIT"
repo_path: "sources/codex-game-studio/skills/run-qa-pass/SKILL.md"
description: "Use when the user needs a smoke pass, regression pass, acceptance review, or defect triage for a game feature or build. 当用户需要对游戏功能或构建进行冒烟测试、回归测试、验收评审或缺陷分级时使用。"
orig_name: "run-qa-pass"
tags: [lib/skill, cat/src-codex-game-studio, src/codex-game-studio]
---

# codex-game-studio/run-qa-pass

> Use when the user needs a smoke pass, regression pass, acceptance review, or defect triage for a game feature or build. 当用户需要对游戏功能或构建进行冒烟测试、回归测试、验收评审或缺陷分级时使用。

Type: skill | Category: [[categories/cat-src-codex-game-studio|src-codex-game-studio]] | Source: [[sources/src-codex-game-studio|codex-game-studio]] | License: MIT
Repo file: `sources/codex-game-studio/skills/run-qa-pass/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Run QA Pass

## 目标

为某个功能或构建定义并执行验证流程。

## 何时使用

- 某个功能已经准备好测试
- 某个构建需要验收或回归检查

## 工作流

1. 定义测试范围
2. 区分冒烟覆盖和回归覆盖
3. 识别阻塞项
4. 如果通过，把发布准备交给 `release-manager`

## 输出要求

- 测试范围
- 冒烟覆盖
- 回归覆盖
- 阻塞项
- 下一步交接对象

## 参考资料

- `../shared/references/qa-checklist-template.md`
- `../shared/references/risk-severity-guide.md`
