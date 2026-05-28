# Output Templates

Use Chinese by default.

## Fast Diagnosis

```markdown
**一句话诊断**
这是一个[thin-tail/fat-tail/unknown-tail]问题，核心不是预测，而是[避免 ruin / 改造 payoff / 增加 skin in the game / 保留 optionality]。

**最危险的点**
- ...

**最有价值的改造**
- ...

**建议**
[Proceed / Proceed as small experiment / Redesign first / Avoid]
```

## Full Decision Memo

```markdown
**一句话诊断**
...

**1. 领域判断**
- Tail type:
- 是否 Extremistan:
- 数据是否可靠:
- 是否需要预测才能成功:

**2. 随机性与技能**
- 可见成果:
- 可能的运气成分:
- 缺失的失败样本:
- 我会如何验证:

**3. 不对称性表**
| 暴露 | 正常情况 | 压力情况 | 极端情况 | 结论 |
|---|---:|---:|---:|---|

**4. 预测 vs 暴露**
- 预测命题:
- 实际 payoff:
- 小概率大影响:
- 决策含义:

**5. Ruin 检查**
- 破产/出局风险:
- 不可逆损害:
- 单点依赖:
- 杠杆/流动性:

**6. Skin in the game**
| 角色 | 拿到好处 | 承担坏处 | 是否对称 |
|---|---:|---:|---|

**7. 反脆弱改造**
- 移除:
- 保护:
- 小实验:
- 杠铃:

**8. 结论**
我的建议是：...

**9. 会改变我判断的证据**
- ...
```

## Red-Team Memo

```markdown
**反方结论**
这个方案最可能不是因为“方向错”失败，而是因为下面这些隐藏暴露：

**隐藏假设**
1. ...
2. ...
3. ...

**黑天鹅入口**
- ...

**脆弱性**
- Leverage:
- Dependency:
- Tight coupling:
- Reversibility:

**如果非做不可**
1. 把最大损失限制在...
2. 先用...验证...
3. 设置退出条件...
```

## Book Distillation Answer

Use when the user asks "这本书怎么蒸馏到我的决策里?"

```markdown
**这本书在 skill 里的位置**
...

**不要只记观点，要记成问题**
- 观点:
- 决策问题:
- 用在:

**最容易误用的地方**
- ...

**可以直接调用的检查句**
1. ...
2. ...
3. ...
```

## Source-Fidelity Response

Use when the user challenges whether something is genuinely from the books.

```markdown
我把这里分成三层：

- **书中核心概念**: ...
- **我对你场景的应用**: ...
- **推断，不等于原文**: ...

我没有你这版书的原文页码，所以不会编页码或原话。若你给我照片/OCR/摘录，我可以做逐段蒸馏并标注来源。
```

## Per-Book Distillation Status

Use when the user asks whether a book is done.

```markdown
**完成度**
- 当前状态: [Conceptual / Official-anchor / Source-scaffold / Chapter-backed / Page-backed / Operational]
- 已覆盖:
- 未覆盖:
- 不能声称:

**这本书已经能用于**
- ...

**还需要你补的材料**
- ...

**下一步我会做**
- ...
```

## Evidence-Labeled Claim

Use when the user wants rigor.

```markdown
- Claim:
- Evidence level: [official-anchor / source-scaffold / page-backed / inference]
- Source:
- Decision question:
- Misuse warning:
```

## Forecast Versus Exposure

Use when the user asks whether an event will happen but the practical issue is payoff.

```markdown
**先拆开：预测不等于决策**
- 更可能发生的事:
- 更痛/更赚的事:
- payoff 是否对称:

**如果预测对了**
- 收益:
- 代价:

**如果预测错了**
- 损失:
- 是否出局:

**结论**
这个决策不应该只问概率，而要问暴露形状：...
```

## Action Operating Answer

Use when the user has not read the books and wants practical guidance.

```markdown
**一句话判断**
...

**地形**
- Tail:
- 可逆性:
- 路径依赖:
- 规则是否会变:

**先保命**
- 最大可能损失:
- 出局风险:
- 单点依赖:
- 必须先移除的脆弱性:

**暴露形状**
| 情况 | 会发生什么 | 损益 | 是否可逆 |
|---|---|---:|---|
| 正常 | | | |
| 好运 | | | |
| 坏运 | | | |
| 极端 | | | |

**激励**
- 谁拿好处:
- 谁吃坏处:
- 谁可以不负责:
- 信任折扣:

**建议动作**
[Avoid / Redesign / Small experiment / Barbell / Commit]

**下一步做什么**
1. ...
2. ...
3. ...

**停止条件**
- ...

**复盘时看什么**
- ...
```
